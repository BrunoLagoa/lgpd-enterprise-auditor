---
name: lgpd-devsecops
description: Executa auditoria LGPD direcionada para pipelines DevSecOps.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.3.2"
---

# LGPD DevSecOps Pipeline

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- plataforma de CI/CD;
- estratégia de containers e Kubernetes;
- gestão de segredos e scans de segurança;
- fluxo de deploy e ambientes.

Ative o cenário `devsecops_pipeline`:
- `core`, `legal`, `devsecops`, `cloud`, `appsec`.

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar segredos, supply chain e hardening de deploy;
- exigir evidência para todos os achados;
- gerar score e relatório técnico/compliance.
