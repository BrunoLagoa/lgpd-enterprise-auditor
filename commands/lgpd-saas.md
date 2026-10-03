---
name: lgpd-saas
description: Executa auditoria LGPD direcionada para SaaS web.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.4.0"
---

# LGPD SaaS Web

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- stack web e backend;
- banco de dados e cloud provider;
- integrações (analytics, pagamentos, CRM, etc.);
- dados pessoais/sensíveis tratados.

Ative o cenário `saas_web`:
- `core`, `legal`, `governance`, `appsec`, `cloud`, `devsecops`.

Adicione `eca-digital` se houver usuários menores de 18 anos, ainda que o produto não seja direcionado a eles (gatilho normativo do router — ECA Digital, Lei nº 15.211/2025).

Adicione `plataformas-digitais` se houver conteúdo gerado por usuários com difusão pública, anúncios/impulsionamento pagos ou IA que gere ou altere imagem ou som de pessoas (gatilho normativo do router — Decretos nº 12.975/2026 e nº 12.976/2026).

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- exigir evidência por item auditado;
- gerar score e classificação final;
- produzir relatório conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
