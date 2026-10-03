---
name: lgpd-full-audit
description: Executa auditoria LGPD completa (full_audit), com todos os modulos ativos.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.3.0"
---

# LGPD Full Audit

Antes de perguntar, leia o que o projeto ja documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependencias e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou nao puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou juridica, com ou sem fins economicos, porte (agente de pequeno porte, Res. CD/ANPD 2/2022) e se ha tratamento de alto risco;
- stack completa (frontend, backend, banco, cloud);
- dados pessoais e dados sensiveis tratados;
- integracoes de terceiros;
- contexto de DevSecOps e IA/LLM;
- existencia de usuarios menores de 18 anos (ECA Digital);
- intermediacao de conteudo de terceiros, anuncios/impulsionamento pagos ou IA que gera imagem/voz (plataformas digitais).

Execute no modo `full_audit` com cobertura total:
- `core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- nao assumir conformidade sem evidencia;
- aplicar severidade e score conforme `.agents/lgpd-enterprise-auditor/core/`;
- gerar saida no formato de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
