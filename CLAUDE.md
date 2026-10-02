# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

`lgpd-enterprise-auditor` is **not application code** — it is a prompt/instruction framework that turns an LLM agent into an evidence-driven LGPD (Brazilian data protection law, Lei nº 13.709/2018) compliance auditor. Every file is Markdown: agent instructions, audit contracts, scenario manifests, report formats, and slash commands. There is no build, no test suite, no package manager, and no runtime to execute. "Working" on this repo means editing Markdown specifications so the agent behaves consistently.

## Language convention

Documentation is bilingual but the split is deliberate:
- **User-facing docs** (`README.md`, `README.pt-BR.md`) are maintained in English + Brazilian Portuguese. The English README is canonical; keep both in sync. The `<!-- README-I18N:START -->` / `END` markers delimit the language-switcher block — don't break them.
- **Framework internals** (everything under `.agents/`, `SKILL.md`, and `commands/`) are written in **Brazilian Portuguese**. Match this when editing framework files — do not translate them to English.
- Note the diacritics split inside the framework: files under `.agents/` and `SKILL.md` use full Portuguese accentuation, while `commands/*.md` are currently written without diacritics ("cenario", "obrigatorias"). Match the style of the file you are editing instead of normalizing across the tree.

## Two parallel implementations (V1 and V2)

The repository contains two versions of the same auditor; both must stay functionally equivalent ("parity"):

- **V1 — monolith**: `SKILL.md` (~900 lines). A single self-contained prompt covering the full checklist, severity, scoring, and report format. It is the actual V1 source of truth. It starts with the same YAML frontmatter as `commands/*.md` (`name: lgpd-enterprise-auditor`) so it can be installed as a Claude Code skill (`.claude/skills/lgpd-enterprise-auditor/SKILL.md`); keep `name` equal to that directory name.
- **V2 — modular**: `.agents/lgpd-enterprise-auditor/` decomposed into layers. This is the canonical structure to extend.
- `.agents/lgpd-enterprise-auditor/legacy/v1-monolith.md` is **not** a copy of `SKILL.md` — it is a short compatibility bridge that points back to `SKILL.md` and enumerates the **17 V1 domains** that `full_audit` must cover (mapeamento de dados, consentimento, direitos do titular, política de privacidade, cookies e tracking, segurança da informação, cloud security, mobile security, APIs e integrações, DevSecOps, logs e observabilidade, IA/LLM, governança, compartilhamento de dados, retenção e exclusão, ECA Digital, plataformas digitais).

When you change audit logic (a checklist item, severity rule, scoring weight, or report field), check whether it must change in **both** V1 and V2. `validation/parity-checklist.md` and `validation/v1-to-v2-traceability.md` track this equivalence — update them when coverage shifts.

## V2 architecture

Canonical base path (referenced literally inside commands and meant to be copied into audited projects): `.agents/lgpd-enterprise-auditor/`

- `README.md` — the V2 overview (structure, execution flow, scenarios, naming conventions). It duplicates facts that live in `orchestrator/` and `core/`; keep it in sync when those change.
- `core/` — the canonical **contracts** all other modules depend on. Edit these first; downstream modules and reports must conform:
  - `auditor-core.md` defines the data shapes `finding`, `check_item`, `module_output` (their fields and enum values).
  - `evidence-engine.md` (evidence rules and confidence scale), `severity-model.md` (CRITICO/ALTO/MEDIO/BAIXO), `scoring-engine.md` (per-area weights + final 0–100 classification), `reporting-engine.md` (mandatory report format).
- `legal/` — LGPD/ANPD normative basis (`lgpd-legal-framework.md`, `anpd-guidelines.md`), legal bases for processing (`legal-bases-engine.md`, art. 7º vs art. 11), data-subject rights, children/adolescents (art. 14), international transfer (arts. 33–36), and `eca-digital.md`. Note the exception: `eca-digital.md` lives under `legal/` but is a **module of its own** (ID `eca-digital`, with `orchestrator/manifests/eca-digital.manifest.md`) because it implements a separate statute (Lei nº 15.211/2025), not an LGPD chapter. `plataformas-digitais.md` follows the same exception (ID `plataformas-digitais`, with its own manifest): it implements Decretos nº 12.975/2026 and nº 12.976/2026, the Marco Civil da Internet regulation that ANPD now enforces.
- `governance/`, `cloud/`, `appsec/`, `mobile/`, `devsecops/`, `ai-llm/` — specialist audit modules, one per domain.
- `orchestrator/` — scenario-based module activation. `router.md` holds the activation rules, `activation-matrix.md` the scenario→module table, and `manifests/*.manifest.md` declare each module's `required` flag, inputs, prerequisites, `activates_when`, and `primary_outputs`.
- `templates/` — reusable compliance artifacts (RIPD, DPA, privacy/cookie policy, incident response, ECA Digital semiannual transparency report, age-assurance checklist).
- `reports/` — output formats per audience (executive, technical, compliance, risk-matrix).
- `validation/` — V1↔V2 parity checklist and the domain→module traceability matrix.

## Canonical scenarios

The scenario IDs are snake_case and must stay identical across `orchestrator/router.md`, `orchestrator/activation-matrix.md`, the V2 `README.md`, and each `commands/*.md`:

| Scenario | Modules |
|---|---|
| `saas_web` | core, legal, governance, appsec, cloud, devsecops |
| `web_site` | core, legal, governance, appsec, cloud |
| `mobile_app` | core, legal, governance, mobile, appsec, cloud |
| `ai_llm_system` | core, legal, governance, ai-llm, appsec |
| `devsecops_pipeline` | core, legal, devsecops, cloud, appsec |
| `eca_digital_platform` | core, legal, eca-digital, governance, appsec, mobile |
| `digital_platform` | core, legal, plataformas-digitais, governance, appsec, cloud |
| `full_audit` | all modules (V1 parity) |

`eca-digital` is also added to **any** scenario by the normative trigger in `router.md` whenever minors are (or plausibly are) among the users. Likewise, `plataformas-digitais` is added to any scenario when the audited provider hosts publicly shared third-party content, sells ads/boosts, or offers AI that generates or alters people's image or voice.

## Critical naming rule

Module IDs and score-area IDs use **different casing on purpose** — do not unify them:
- **Module IDs** (routing, file/dir names): kebab-case → `ai-llm`
- **Score-area IDs** (scoring engine): snake_case → `ai_llm`

The orchestrator activates by module ID; the scoring engine computes by area ID. Mixing the two breaks routing/scoring alignment.

## Scoring and reporting shapes

- Score areas and weights (`core/scoring-engine.md`) must always sum to 100%: `bases_legais` 15, `seguranca` 25, `direitos_titular` 15, `governanca` 15, `infraestrutura` 10, `apis_integracoes` 10, `ai_llm` 10.
- An area may be `NAO_APLICAVEL` only when its object does not exist in scope (never for missing evidence); its weight is redistributed proportionally across the applicable areas. `bases_legais`, `seguranca`, `direitos_titular` and `governanca` are always applicable. This rule lives in `core/scoring-engine.md` and the V1 scoring section of `SKILL.md`.
- Final classification labels are exactly `CRITICO` (0–49), `BAIXO_NIVEL` (50–69), `PARCIALMENTE_CONFORME` (70–84), `ALTA_CONFORMIDADE` (85–94), `EXCELENTE` (95–100).
- The report (`core/reporting-engine.md`) has 8 mandatory sections in this order: `resumo_executivo`, `score_lgpd`, `checklist_conformidade`, `nao_conformidades`, `itens_obrigatorios_ausentes`, `riscos_identificados`, `plano_adequacao`, `recomendacoes_tecnicas`. Every non-conformity in the checklist must reappear detailed in `nao_conformidades`.

## Commands (slash commands)

`commands/*.md` are execution shortcuts (`lgpd-full-audit`, `lgpd-saas`, `lgpd-web`, `lgpd-mobile`, `lgpd-ai-llm`, `lgpd-devsecops`, `lgpd-eca-digital`, `lgpd-plataformas-digitais`). Each has YAML frontmatter (`name`, `description`, `license`, `metadata.author`, `metadata.version`) and then instructions that ask for missing context, select a scenario, list the modules to activate, and reference the canonical base path. When adding a command, mirror this frontmatter and keep the activated-module list consistent with `orchestrator/activation-matrix.md` and `orchestrator/router.md`.

## Sync-date maintenance (required on every framework update)

Whenever you make a substantive update to the framework (audit logic, modules, contracts, commands, templates, or report formats), you **must** update the synchronization date in both READMEs to the current month (`YYYY-MM` format):
- `README.md` → the `| Last synchronization | \`YYYY-MM\` |` row
- `README.pt-BR.md` → the `| Última sincronização | \`YYYY-MM\` |` row

Keep the value identical in both files (currently `2026-10`). This row signals when the framework was last aligned with LGPD/ANPD; a stale date is misleading, so never skip it.

## Where normative changes ripple

A change to LGPD/ANPD coverage rarely touches one file. Typical fan-out for a new legal requirement:
1. the relevant `legal/*.md` (or a new file there);
2. the V1 monolith `SKILL.md` (parity);
3. `orchestrator/manifests/legal.manifest.md` → `primary_outputs`;
4. `validation/parity-checklist.md` (+ `v1-to-v2-traceability.md` if a domain moves module);
5. both READMEs (legal-basis section + sync date).

Concrete example already in the tree: Resolução CD/ANPD nº 15/2024 (3 business days to report an incident) appears in `legal/anpd-guidelines.md`, `governance/dpo-framework.md`, `templates/incident-response-template.md`, `validation/parity-checklist.md`, and both READMEs — change it in all of them or nowhere.

## Invariants to preserve when editing

These rules are load-bearing across the whole framework — keep them intact:
- Never mark anything compliant without evidence; every `finding` cites the applicable LGPD article.
- Severity values are exactly `CRITICO | ALTO | MEDIO | BAIXO`; `check_item.status` is `CONFORME | PARCIAL | NAO_CONFORME`; deadlines `IMEDIATO | 30_DIAS | 90_DIAS | 180_DIAS`.
- Evidence is classified on **two independent axes**, never mixed: `evidence_type` (degree of proof) is `ENCONTRADA | PARCIAL | AUSENTE`, and `evidence_source` (origin) is `TECNICA | DOCUMENTAL`. `CONFORME` requires `ENCONTRADA`; `CRITICO`/`ALTO` findings require an explicit `TECNICA` or `DOCUMENTAL` source. Both axes exist in V1 (`SKILL.md`, "SISTEMA DE EVIDÊNCIAS") and V2 (`core/evidence-engine.md` + `core/auditor-core.md`).
- The `full_audit` scenario must activate every module (`core, legal, eca-digital, plataformas-digitais, governance, cloud, appsec, mobile, devsecops, ai-llm`) to preserve V1 parity.
- Only **norms in force** produce `finding`s or a `NAO_CONFORME` status. Bills and draft guidance (e.g. PL nº 2338/2023) live in "Em monitoramento" sections and may only feed `recomendacoes_tecnicas`.
- `core` and `legal` are always required regardless of scenario.
- No module may redefine severity, scoring, or report format locally — those live only in `core/`.

## Evidence model (reconciled 2026-08)

`evidence_type` and `evidence_source` used to be a single flat enum, which made the engine's "every `CONFORME` needs `ENCONTRADA`" rule unsatisfiable from the `finding` contract. They are now two separate fields on both `finding` and `check_item`. When touching evidence rules, keep these five files aligned: `core/evidence-engine.md`, `core/auditor-core.md`, `core/reporting-engine.md`, `reports/technical-report.md`, and `SKILL.md` (V1) — plus the parity checklist item that asserts both axes exist in V1 and V2.
