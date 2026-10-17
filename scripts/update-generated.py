#!/usr/bin/env python3
"""Regera tudo o que o repositório deriva de outra fonte, para que nada seja mantido em dois lugares.

- SKILL.md, blocos entre "<!-- GERADO:INICIO id ... -->" e "<!-- GERADO:FIM id -->":
    catalogo       tabelas "Checklist atômico" e dependências dos módulos do framework;
    evidencias     core/evidence-engine.md;
    severidade     core/severity-model.md;
    score          core/scoring-engine.md (cálculo, aplicabilidade, mapa de áreas, subtotais, riscos aceitos);
    classificacao  core/scoring-engine.md (faixas, teto e rótulos);
    monitoramento  legal/anpd-guidelines.md, seção "Em monitoramento" (fonte única das normas não vigentes).
- examples/saas-demo/relatorio-auditoria-lgpd.html: reaplica o modelo reports/html-report-template.html,
  mantendo o bloco de dados do exemplo.

Os textos copiados para a skill não podem citar arquivos do framework nem usar [[referências]]: a skill é
instalada sozinha, sem o framework ao lado. O script recusa o bloco que trouxer uma dessas referências.

Uso: scripts/update-generated.py [--check]
  --check  não grava: sai com 1 e lista o que está desatualizado.
"""

import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FRAMEWORK = os.path.join(REPO, ".agents", "lgpd-enterprise-auditor")
SKILL = os.path.join(REPO, "SKILL.md")
TEMPLATE = os.path.join(FRAMEWORK, "reports", "html-report-template.html")
EXAMPLE = os.path.join(REPO, "examples", "saas-demo", "relatorio-auditoria-lgpd.html")
PLACEHOLDER = '{"_modelo": true}'
DATA_OPEN = '<script type="application/json" id="lgpd-dados">'

# A ordem dos arquivos define a ordem dos itens dentro de cada domínio no catálogo da skill.
MODULE_FILES = [
    "legal/legal-bases-engine.md",
    "legal/rights-of-data-subject.md",
    "legal/children-adolescents.md",
    "legal/international-transfer.md",
    "governance/dpo-framework.md",
    "cloud/cloud-audit.md",
    "appsec/owasp-api.md",
    "mobile/mobile-storage.md",
    "devsecops/ci-cd-security.md",
    "ai-llm/llm-audit.md",
    "legal/eca-digital.md",
    "legal/plataformas-digitais.md",
]

# Blocos copiados do framework: (id, arquivo, seções "## Título"). Com body=True, copia só o conteúdo
# da seção, sem o título, e sobe um nível os subtítulos (### vira ##), para caber sob o "# TÍTULO" da skill.
SECTION_BLOCKS = [
    ("evidencias", "core/evidence-engine.md", ["Eixos de classificação", "Regras de validação", "Status do item",
                                               "Escala de confiança da evidência (`evidence_confidence`)",
                                               "Critério de bloqueio"], False),
    ("severidade", "core/severity-model.md", ["Níveis canônicos", "Modulação por porte e exposição", "Regras de uso"], False),
    ("score", "core/scoring-engine.md", ["Cálculo do score (obrigatório)", "Aplicabilidade do item e cobertura",
                                         "Mapa de áreas por domínio", "Score técnico e score documental (informativos)",
                                         "Riscos aceitos"], False),
    ("classificacao", "core/scoring-engine.md", ["Classificação final canônica", "Teto de classificação",
                                                 "Normalização de rótulos"], False),
    ("monitoramento", "legal/anpd-guidelines.md", ["Em monitoramento (não vigente — não gera não conformidade)"], True),
]

FRAMEWORK_REF = re.compile(r"\[\[[^\]]+\]\]|`(?:core|legal|orchestrator|reports|governance|appsec|cloud|mobile|devsecops|"
                           r"ai-llm|templates|validation)/[^`]*`")


class Failure(Exception):
    pass


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def cells(line):
    """Mesmo corte do awk usado antes: separa por "|" e apara os espaços em volta de cada célula."""
    return re.split(r" *\| *", line)


def catalog_block():
    domains, order = {}, []
    for line in read(os.path.join(FRAMEWORK, "core", "scoring-engine.md")).splitlines():
        if re.match(r"^\| `(BL|[0-9]+)` \|", line):
            c = cells(line)
            code = c[1].replace("`", "")
            order.append(code)
            domains[code] = (c[2], c[3])
    rows, deps = {}, []
    for rel in MODULE_FILES:
        path = os.path.join(FRAMEWORK, rel)
        if not os.path.isfile(path):
            raise Failure("módulo não encontrado: %s" % rel)
        for line in read(path).splitlines():
            if re.match(r"^\| `[A-Z][A-Z]+-[0-9]+` \|", line):
                c = cells(line)
                if c[3] not in domains:
                    raise Failure("domínio desconhecido em %s: %s" % (c[1], c[3]))
                rows.setdefault(c[3], []).append("| %s | %s | %s | %s | %s | %s |" % (c[1], c[2], c[4], c[5], c[6], c[7]))
            elif re.match(r"^- `[A-Z][A-Z]+-[0-9]+` depende de `[A-Z][A-Z]+-[0-9]+`", line):
                deps.append(line)
    if not rows:
        raise Failure("nenhum item de catálogo encontrado nos módulos")
    out = []
    for code in order:
        if code not in rows:
            continue
        name, area = domains[code]
        out += ["## %s. %s — área %s" % (code, name, area), "",
                "| ID | Item | Criticidade | Agravante ou atenuante | Controle | Fundamento |",
                "|---|---|---|---|---|---|"] + rows[code] + [""]
    if deps:
        out += ["## Dependências entre itens", "",
                "Com o segundo item `NAO_CONFORME`, o primeiro fica `NAO_APLICAVEL`. A lista é fechada: fora dela, "
                "cada item é avaliado pelo próprio requisito.", ""] + deps + [""]
    return "\n".join(out)


def section_block(block_id, rel, headings, body_only):
    text = read(os.path.join(FRAMEWORK, rel))
    parts = []
    for heading in headings:
        match = re.search(r"^## %s\n(.*?)(?=^## |\Z)" % re.escape(heading), text, re.S | re.M)
        if not match:
            raise Failure("%s: seção \"## %s\" não encontrada em %s" % (block_id, heading, rel))
        content = match.group(1).strip("\n")
        if body_only:
            content = re.sub(r"^###(?=#* )", "##", content, flags=re.M)
            parts.append(content)
        else:
            parts.append("## %s\n%s" % (heading, content))
    block = "\n\n".join(parts) + "\n"
    bad = sorted(set(FRAMEWORK_REF.findall(block)))
    if bad:
        raise Failure("%s: o texto copiado de %s cita o framework (%s); reescreva a fonte sem essas referências"
                      % (block_id, rel, ", ".join(bad)))
    return block


def fill_skill(skill, blocks):
    for block_id, content in blocks:
        start = re.compile(r"^<!-- GERADO:INICIO %s .*-->$" % re.escape(block_id), re.M)
        end = "<!-- GERADO:FIM %s -->" % block_id
        found = start.findall(skill)
        if len(found) != 1 or skill.count("\n" + end + "\n") != 1:
            raise Failure("SKILL.md: marcadores do bloco %s ausentes ou repetidos" % block_id)
        head = start.search(skill)
        tail = skill.index("\n" + end + "\n", head.end())
        skill = skill[:head.end()] + "\n\n" + content.rstrip("\n") + "\n" + skill[tail:]
    return skill


def fill_example():
    template, example = read(TEMPLATE), read(EXAMPLE)
    if template.count(PLACEHOLDER) != 1:
        raise Failure("o modelo HTML deve ter a linha %s uma única vez" % PLACEHOLDER)
    start = example.find(DATA_OPEN)
    if start < 0:
        raise Failure("bloco de dados ausente no exemplo")
    start = example.index("\n", start) + 1
    end = example.index("\n</script>", start)
    data = example[start:end]
    if data.strip() == PLACEHOLDER:
        raise Failure("o exemplo ainda está com o bloco de dados do modelo")
    return template.replace(PLACEHOLDER, data)


def main():
    check = "--check" in sys.argv[1:]
    try:
        blocks = [("catalogo", catalog_block())] + [(b[0], section_block(*b)) for b in SECTION_BLOCKS]
        targets = [(SKILL, fill_skill(read(SKILL), blocks)), (EXAMPLE, fill_example())]
    except Failure as error:
        print("Erro: %s" % error)
        return 1
    stale = [path for path, text in targets if read(path) != text]
    if not stale:
        print("Conteúdo gerado em dia (skill e relatório de exemplo).")
        return 0
    names = ", ".join(os.path.relpath(path, REPO) for path in stale)
    if check:
        print("Desatualizado em relação às fontes: %s (rode scripts/update-generated.py)." % names)
        return 1
    for path, text in targets:
        if path in stale:
            write(path, text)
    print("Atualizado: %s." % names)
    return 0


if __name__ == "__main__":
    sys.exit(main())
