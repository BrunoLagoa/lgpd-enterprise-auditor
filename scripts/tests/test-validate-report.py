#!/usr/bin/env python3
"""Confere que scripts/validate-report.py reprova o que deve reprovar.

O exemplo público passa no validador; isso não prova que ele pega erros. Cada caso abaixo parte
dos dados do exemplo, quebra uma regra do framework e exige a mensagem de erro correspondente.
Uso: scripts/tests/test-validate-report.py
"""

import copy
import importlib.util
import json
import os
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True  # importar o validador não deve deixar __pycache__ no repositório

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FRAMEWORK = os.path.join(REPO_ROOT, ".agents", "lgpd-enterprise-auditor")
EXAMPLE_HTML = os.path.join(REPO_ROOT, "examples", "saas-demo", "relatorio-auditoria-lgpd.html")
EXAMPLE_MD = os.path.join(REPO_ROOT, "examples", "saas-demo", "relatorio-auditoria-lgpd.md")

spec = importlib.util.spec_from_file_location("validate_report", os.path.join(REPO_ROOT, "scripts", "validate-report.py"))
vr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vr)

WEIGHTS, _DOMAINS, MODULES, CATALOG, DEPENDS = vr.load_framework(FRAMEWORK)
BASE = vr.load_data(EXAMPLE_HTML)
BASE_MD = vr.read(EXAMPLE_MD)


def run(data, md_text=None):
    errors, _warnings, _summary = vr.validate(data, WEIGHTS, MODULES, CATALOG, md_text, DEPENDS)
    return errors


def items_by_id(data):
    return {item["id"]: item for item in data["checklist_conformidade"]}


def first(data, **conditions):
    for item in data["checklist_conformidade"]:
        if all(item.get(key, "APLICAVEL" if key == "applicability" else None) == value for key, value in conditions.items()):
            return item
    raise AssertionError("o exemplo não tem item com %s" % conditions)


def finding_for(data, item_id):
    return next(f for f in data["nao_conformidades"] if f["item_id"] == item_id)


class ValidatorCatchesErrors(unittest.TestCase):
    def setUp(self):
        self.data = copy.deepcopy(BASE)

    def assertError(self, fragment, md_text=None):
        errors = run(self.data, md_text)
        self.assertTrue(any(fragment in message for message in errors),
                        "esperado erro com %r; erros: %s" % (fragment, errors or "nenhum"))

    def test_example_passes(self):
        self.assertEqual(run(self.data, BASE_MD), [])

    def test_missing_section(self):
        self.data["riscos_identificados"] = []
        self.assertError("seção ausente ou vazia: riscos_identificados")

    def test_declared_score_differs(self):
        self.data["score_lgpd"]["score"] += 1
        self.assertError("score global: declarado")

    def test_declared_area_score_differs(self):
        area = next(a for a in self.data["score_lgpd"]["areas"] if a.get("score") is not None)
        area["score"] = float(area["score"]) + 5
        self.assertError("área %s: score declarado" % area["id"])

    def test_wrong_classification(self):
        self.data["score_lgpd"]["classification"] = "EXCELENTE"
        self.assertError("classificação: declarada EXCELENTE")

    def test_classification_cap(self):
        # Todos os itens conformes menos um CRITICO: o score cai na faixa alta, mas o teto limita.
        critical = first(self.data, status="NAO_CONFORME", criticality="CRITICO")
        for item in self.data["checklist_conformidade"]:
            if item.get("applicability", "APLICAVEL") == "APLICAVEL" and item is not critical:
                item.update(status="CONFORME", evidence_type="ENCONTRADA")
        self.data["nao_conformidades"] = [finding_for(self.data, critical["id"])]
        self.data["score_lgpd"]["classification"] = "EXCELENTE"
        self.assertError("(teto por achado crítico)")

    def test_unknown_item_id(self):
        first(self.data, status="CONFORME")["id"] = "ZZ-99"
        self.assertError("ZZ-99: ID fora do catálogo")

    def test_catalog_item_missing(self):
        removed = self.data["checklist_conformidade"].pop()
        self.assertError("itens do catálogo ausentes do checklist: %s" % removed["id"])

    def test_criticality_not_in_catalog(self):
        item = first(self.data, status="CONFORME")
        entry = CATALOG[item["id"]]
        item["criticality"] = next(level for level in vr.LEVELS if level not in entry["allowed"])
        self.assertError("%s: criticality" % item["id"])

    def test_conforme_without_found_evidence(self):
        item = first(self.data, status="CONFORME")
        item["evidence_type"] = "AUSENTE"
        self.assertError("%s: CONFORME exige evidence_type ENCONTRADA" % item["id"])

    def test_documental_not_verified(self):
        item = first(self.data, status="CONFORME", control_type="DOCUMENTAL")
        item["applicability"] = "NAO_VERIFICADO"
        item["justification"] = "sem acesso"
        del item["status"]
        self.assertError("%s: controle DOCUMENTAL nunca é NAO_VERIFICADO" % item["id"])

    def test_partial_severity_one_level_below(self):
        item = first(self.data, status="PARCIAL")
        finding_for(self.data, item["id"])["severity"] = item["criticality"]
        self.assertError("um nível abaixo da criticality")

    def test_non_conformity_severity_equals_criticality(self):
        item = first(self.data, status="NAO_CONFORME", criticality="ALTO")
        finding_for(self.data, item["id"])["severity"] = "MEDIO"
        self.assertError("severity MEDIO difere da criticality")

    def test_deadline_longer_than_maximum(self):
        item = first(self.data, status="NAO_CONFORME", criticality="CRITICO")
        finding_for(self.data, item["id"])["deadline_suggestion"] = "30_DIAS"
        self.assertError("prazo 30_DIAS é mais longo que o máximo")

    def test_failed_item_without_finding(self):
        item = first(self.data, status="NAO_CONFORME")
        self.data["nao_conformidades"] = [f for f in self.data["nao_conformidades"] if f["item_id"] != item["id"]]
        self.assertError("%s: item NAO_CONFORME sem achado" % item["id"])

    def test_dependency_must_be_not_applicable(self):
        by_id = items_by_id(self.data)
        pairs = [(d, t) for d, t in DEPENDS if d in by_id and t in by_id and by_id[t].get("status") == "NAO_CONFORME"]
        self.assertTrue(pairs, "o exemplo não tem dependência com o alvo NAO_CONFORME")
        dependent = by_id[pairs[0][0]]
        dependent.update(applicability="APLICAVEL", status="CONFORME", evidence_type="ENCONTRADA",
                         evidence_source="DOCUMENTAL", evidence_confidence="ALTA", evidence="x")
        self.assertError("%s: depende de %s" % pairs[0])

    def test_always_applicable_area(self):
        area = next(a for a in self.data["score_lgpd"]["areas"] if a["id"] == "seguranca")
        area["applicability"] = "NAO_APLICAVEL"
        self.assertError("área seguranca é sempre aplicável")

    def test_markdown_missing_item(self):
        item = first(self.data, status="CONFORME")
        self.assertError("relatório .md: itens do checklist ausentes: %s" % item["id"], BASE_MD.replace(item["id"], "XX-00"))

    def test_markdown_missing_score(self):
        score = "%d/100" % self.data["score_lgpd"]["score"]
        self.assertError("relatório .md: não traz o score", BASE_MD.replace(score, "?/100"))

    def test_framework_file_cited_is_a_warning(self):
        finding = self.data["nao_conformidades"][0]
        finding["severity_note"] = "Mapeamento de `appsec/owasp-api.md` e régua de `core/evidence-engine.md`."
        errors, warnings, _summary = vr.validate(self.data, WEIGHTS, MODULES, CATALOG, None, DEPENDS)
        self.assertEqual(errors, [])
        self.assertTrue(any("appsec/owasp-api.md" in w and "core/evidence-engine.md" in w for w in warnings), warnings)

    def test_example_cites_no_framework_file(self):
        _errors, warnings, _summary = vr.validate(self.data, WEIGHTS, MODULES, CATALOG, BASE_MD, DEPENDS)
        self.assertEqual([w for w in warnings if "arquivos de regras" in w], [])

    def test_html_block_with_raw_lt(self):
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as handle:
            handle.write('%s\n{"meta": {"note": "<b>"}}\n</script>\n' % vr.DATA_OPEN)
        try:
            with self.assertRaises(SystemExit) as raised:
                vr.load_data(handle.name)
            self.assertIn("\\u003c", str(raised.exception))
        finally:
            os.unlink(handle.name)

    def test_template_placeholder_rejected(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as handle:
            json.dump({"_modelo": True}, handle)
        try:
            with self.assertRaises(SystemExit):
                vr.load_data(handle.name)
        finally:
            os.unlink(handle.name)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(argv=[sys.argv[0], "-q"], exit=False).result.wasSuccessful() else 1)
