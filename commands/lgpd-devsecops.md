---
name: lgpd-devsecops
description: Executa auditoria LGPD direcionada para pipelines DevSecOps.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.5.0"
---

# LGPD DevSecOps Pipeline

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- plataforma de CI/CD;
- estratégia de containers e Kubernetes;
- gestão de segredos e scans de segurança;
- fluxo de deploy e ambientes.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `devsecops_pipeline`:
- `core`, `legal`, `devsecops`, `cloud`, `appsec`.

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar segredos, supply chain e hardening de deploy;
- exigir evidência para todos os achados;
- gerar score e relatório técnico/compliance;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
