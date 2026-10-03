---
name: lgpd-mobile
description: Executa auditoria LGPD direcionada para aplicacoes mobile.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.2.0"
---

# LGPD Mobile App

Antes de perguntar, leia o que o projeto ja documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependencias e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou nao puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou juridica, com ou sem fins economicos, porte (agente de pequeno porte, Res. CD/ANPD 2/2022) e se ha tratamento de alto risco;
- plataforma mobile (iOS, Android, Flutter, React Native);
- uso de Firebase e servicos cloud;
- SDKs de tracking/analytics;
- dados pessoais/sensiveis tratados no app.

Ative o cenario `mobile_app`:
- `core`, `legal`, `governance`, `mobile`, `appsec`, `cloud`.

Adicione `eca-digital` se o app for classificado para faixa etaria inferior a 18 anos nas lojas ou tiver usuarios menores (gatilho normativo do router — ECA Digital, Lei 15.211/2025).

Adicione `plataformas-digitais` se o app intermediar conteudo de terceiros com difusao publica, oferecer anuncios/impulsionamento pagos ou gerar/alterar imagem ou som de pessoas (gatilho normativo do router — Decretos 12.975/2026 e 12.976/2026).

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar permissoes, storage local e tracking;
- exigir evidencia por requisito;
- consolidar score e relatorio final padrao.
