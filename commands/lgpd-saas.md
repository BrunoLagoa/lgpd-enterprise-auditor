---
name: lgpd-saas
description: Executa auditoria LGPD direcionada para SaaS web.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.3.0"
---

# LGPD SaaS Web

Antes de perguntar, leia o que o projeto ja documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependencias e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou nao puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou juridica, com ou sem fins economicos, porte (agente de pequeno porte, Res. CD/ANPD 2/2022) e se ha tratamento de alto risco;
- stack web e backend;
- banco de dados e cloud provider;
- integracoes (analytics, pagamentos, CRM, etc.);
- dados pessoais/sensiveis tratados.

Ative o cenario `saas_web`:
- `core`, `legal`, `governance`, `appsec`, `cloud`, `devsecops`.

Adicione `eca-digital` se houver usuarios menores de 18 anos, ainda que o produto nao seja direcionado a eles (gatilho normativo do router — ECA Digital, Lei 15.211/2025).

Adicione `plataformas-digitais` se houver conteudo gerado por usuarios com difusao publica, anuncios/impulsionamento pagos ou IA que gere ou altere imagem ou som de pessoas (gatilho normativo do router — Decretos 12.975/2026 e 12.976/2026).

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- exigir evidencia por item auditado;
- gerar score e classificacao final;
- produzir relatorio conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
