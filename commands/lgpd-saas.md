---
name: lgpd-saas
description: Executa auditoria LGPD direcionada para SaaS web.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.0.0"
---

# LGPD SaaS Web

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- stack web e backend;
- banco de dados e cloud provider;
- integracoes (analytics, pagamentos, CRM, etc.);
- dados pessoais/sensiveis tratados.

Ative o cenario `saas_web`:
- `core`, `legal`, `governance`, `appsec`, `cloud`, `devsecops`.

Adicione `eca-digital` se houver usuarios menores de 18 anos, ainda que o produto nao seja direcionado a eles (gatilho normativo do router — ECA Digital, Lei 15.211/2025).

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- exigir evidencia por item auditado;
- gerar score e classificacao final;
- produzir relatorio conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
