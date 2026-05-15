# LGPD Enterprise Auditor

<p align="left">
  <img src="./assets/logo-lgpd-enterprise-auditor.webp" alt="LGPD Enterprise Auditor Logo" width="355" />
</p>

<p align="center">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/stargazers"><img src="https://img.shields.io/github/stars/BrunoLagoa/lgpd-enterprise-auditor?style=social" alt="GitHub stars" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/blob/main/LICENSE"><img src="https://img.shields.io/github/license/BrunoLagoa/lgpd-enterprise-auditor" alt="License" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor"><img src="https://hits.sh/github.com/BrunoLagoa/lgpd-enterprise-auditor.svg?label=Project%20views&color=f1c40f" alt="Project views" /></a>
</p>

<!-- README-I18N:START -->

**English** | [Português (Brasil)](./README.pt-BR.md)

<!-- README-I18N:END -->


An evidence-driven LGPD auditing framework focused on security, governance, and AI usage in software engineering.

This project was designed to operate as an auditable and modular system, ready to be reused across products and teams.

## What this project is

`lgpd-enterprise-auditor` is a framework that combines:

- legal auditing (LGPD + ANPD);
- technical auditing (appsec, cloud, mobile, devsecops, AI/LLM);
- severity and scoring model;
- standardized reporting format;
- practical commands for scenario-based execution.

In practice, it enables complete or targeted audits with consistent criteria, evidence, and remediation planning.

## Legal basis and updates

This framework uses the **General Data Protection Law (LGPD)** as its primary legal reference:

- **Official text (Planalto):** [Law No. 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- **Regulatory authority:** [ANPD](https://www.gov.br/anpd/)

| Item | Value |
|------|--------|
| Last synchronization | `2026-05` |

## How the project is organized

```text
.
├── SKILL.md
├── commands/
│   ├── lgpd-full-audit.md
│   ├── lgpd-saas.md
│   ├── lgpd-mobile.md
│   ├── lgpd-ai-llm.md
│   └── lgpd-devsecops.md
└── .agents/
    └── lgpd-enterprise-auditor/
        ├── core/
        ├── legal/
        ├── governance/
        ├── cloud/
        ├── appsec/
        ├── mobile/
        ├── devsecops/
        ├── ai-llm/
        ├── orchestrator/
        ├── templates/
        ├── reports/
        ├── validation/
        └── legacy/
```

### Canonical source

The canonical base path for the modular framework is:

`.agents/lgpd-enterprise-auditor/`

This is the expected standard for projects that adopt the same structure.

## How it works

The audit workflow follows 5 steps:

1. **Project context**: stack, processed data, integrations, and operational setup.
2. **Smart routing**: the orchestrator activates modules by scenario.
3. **Evidence-based checklist**: nothing is marked compliant without proof.
4. **Consolidation**: severity, score, and final classification.
5. **Standardized output**: executive/technical/compliance report + remediation plan.

## Usage modes

### 1) Full audit

Use when you need full coverage:

- command: `commands/lgpd-full-audit.md`
- scenario: `full_audit`

Activated modules: `core`, `legal`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

### 2) Scenario-based audit

Use for focused scope:

- `lgpd-saas` -> web SaaS
- `lgpd-mobile` -> mobile app
- `lgpd-ai-llm` -> AI/LLM systems
- `lgpd-devsecops` -> pipelines and supply chain

## Available commands

Commands in `commands/` are execution shortcuts for the agent.

All commands include:

- metadata (`name`, `description`, `license`, `author`, `version`);
- minimum context collection when not mapped yet;
- mandatory evidence and consistency rules aligned with the modular framework.

## Audit contracts (summary)

Core contracts are located at `.agents/lgpd-enterprise-auditor/core/`:

- `auditor-core.md`: canonical structures (`finding`, `check_item`, `module_output`);
- `evidence-engine.md`: evidence rules;
- `severity-model.md`: severity classification;
- `scoring-engine.md`: score calculation;
- `reporting-engine.md`: mandatory output format.

## Who this project is for

- engineering and platform teams;
- information security and AppSec teams;
- compliance and privacy teams;
- LGPD readiness consultancies;
- squads using generative AI in production.

## Adoption best practices

- keep `.agents/lgpd-enterprise-auditor/` versioned together with the product;
- adapt commands by domain without breaking core contracts;
- record technical and documentary evidence per item;
- review score and non-conformities per release;
- treat auditing as a continuous process, not a one-time event.

## Suggested roadmap

- richer templates by industry (healthtech, fintech, gov);
- evidence collection automation;
- environment-based risk matrix generation;
- comparative reports between releases;
- CI/CD pipeline integration.

## People Behind Memflow

This project evolves with contributions from people who believe in disciplined, practical, and auditable AI software engineering.

<p align="left">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=BrunoLagoa/lgpd-enterprise-auditor&max=100" alt="Project contributors" width="45" />
  </a>
</p>

Want to appear here too? Open an issue, suggest improvements, or submit a PR.

## Support

For support, open an issue on GitHub. Bug reports, feature requests, and usage questions are welcome.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for full terms.
