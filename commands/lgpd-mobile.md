---
name: lgpd-mobile
description: Executa auditoria LGPD direcionada para aplicacoes mobile.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.0.0"
---

# LGPD Mobile App

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- plataforma mobile (iOS, Android, Flutter, React Native);
- uso de Firebase e servicos cloud;
- SDKs de tracking/analytics;
- dados pessoais/sensiveis tratados no app.

Ative o cenario `mobile_app`:
- `core`, `legal`, `governance`, `mobile`, `appsec`, `cloud`.

Adicione `eca-digital` se o app for classificado para faixa etaria inferior a 18 anos nas lojas ou tiver usuarios menores (gatilho normativo do router — ECA Digital, Lei 15.211/2025).

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- validar permissoes, storage local e tracking;
- exigir evidencia por requisito;
- consolidar score e relatorio final padrao.
