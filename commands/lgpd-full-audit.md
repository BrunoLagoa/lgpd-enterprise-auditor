---
name: lgpd-full-audit
description: Executa auditoria LGPD completa em modo full_audit na V2 modular.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.1.0"
---

# LGPD Full Audit

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- stack completa (frontend, backend, banco, cloud);
- dados pessoais e dados sensiveis tratados;
- integracoes de terceiros;
- contexto de DevSecOps e IA/LLM;
- existencia de usuarios menores de 18 anos (ECA Digital);
- intermediacao de conteudo de terceiros, anuncios/impulsionamento pagos ou IA que gera imagem/voz (plataformas digitais).

Execute no modo `full_audit` com cobertura total da V2:
- `core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- nao assumir conformidade sem evidencia;
- aplicar severidade e score conforme `.agents/lgpd-enterprise-auditor/core/`;
- gerar saida no formato de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
