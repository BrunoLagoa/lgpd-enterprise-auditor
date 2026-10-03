---
name: lgpd-devsecops
description: Executa auditoria LGPD direcionada para pipelines DevSecOps.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.3.0"
---

# LGPD DevSecOps Pipeline

Antes de perguntar, leia o que o projeto ja documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependencias e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou nao puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou juridica, com ou sem fins economicos, porte (agente de pequeno porte, Res. CD/ANPD 2/2022) e se ha tratamento de alto risco;
- plataforma de CI/CD;
- estrategia de containers e Kubernetes;
- gestao de segredos e scans de seguranca;
- fluxo de deploy e ambientes.

Ative o cenario `devsecops_pipeline`:
- `core`, `legal`, `devsecops`, `cloud`, `appsec`.

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar segredos, supply chain e hardening de deploy;
- exigir evidencia para todos os achados;
- gerar score e relatorio tecnico/compliance.
