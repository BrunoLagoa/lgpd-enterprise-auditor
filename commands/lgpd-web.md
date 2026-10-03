---
name: lgpd-web
description: Executa auditoria LGPD direcionada para sites e landing pages.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.2.0"
---

# LGPD Web Site / Landing Page

Antes de perguntar, leia o que o projeto ja documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependencias e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou nao puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou juridica, com ou sem fins economicos, porte (agente de pequeno porte, Res. CD/ANPD 2/2022) e se ha tratamento de alto risco;
- tipo de pagina (site institucional, landing page, blog, portal);
- stack e hospedagem (Next.js, React, WordPress, Vercel, Netlify, etc.);
- formularios e dados coletados (nome, email, telefone, empresa);
- cookies e trackers (Google Analytics, Meta Pixel, Hotjar, Google Ads);
- integracoes de marketing/CRM (RD Station, HubSpot, Mailchimp);
- existencia de politica de privacidade e banner de cookies.

Ative o cenario `web_site`:
- `core`, `legal`, `governance`, `appsec`, `cloud`.

Adicione `eca-digital` se o site for direcionado ou provavelmente acessado por menores de 18 anos (gatilho normativo do router — ECA Digital, Lei 15.211/2025).

Adicione `plataformas-digitais` se o site publicar comentarios ou outro conteudo de terceiros com difusao publica, ou vender anuncios/impulsionamento (gatilho normativo do router — Decretos 12.975/2026 e 12.976/2026).

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar base legal de captura de leads, consentimento de cookies e trackers antes do aceite, aplicando a secao de cookies de `.agents/lgpd-enterprise-auditor/appsec/owasp-api.md` e o `.agents/lgpd-enterprise-auditor/templates/cookie-policy-template.md`;
- validar minimizacao de dados no formulario e compartilhamento com terceiros;
- exigir evidencia por requisito;
- produzir relatorio conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
