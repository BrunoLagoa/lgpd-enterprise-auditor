---
name: lgpd-web
description: Executa auditoria LGPD direcionada para sites e landing pages.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.0.0"
---

# LGPD Web Site / Landing Page

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- tipo de pagina (site institucional, landing page, blog, portal);
- stack e hospedagem (Next.js, React, WordPress, Vercel, Netlify, etc.);
- formularios e dados coletados (nome, email, telefone, empresa);
- cookies e trackers (Google Analytics, Meta Pixel, Hotjar, Google Ads);
- integracoes de marketing/CRM (RD Station, HubSpot, Mailchimp);
- existencia de politica de privacidade e banner de cookies.

Ative o cenario `web_site`:
- `core`, `legal`, `governance`, `appsec`, `cloud`.

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar base legal de captura de leads, consentimento de cookies e trackers antes do aceite;
- validar minimizacao de dados no formulario e compartilhamento com terceiros;
- exigir evidencia por requisito;
- produzir relatorio conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
