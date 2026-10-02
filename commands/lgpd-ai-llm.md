---
name: lgpd-ai-llm
description: Executa auditoria LGPD direcionada para sistemas com IA/LLM.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.2.0"
---

# LGPD AI/LLM

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- provedores de IA/LLM utilizados;
- uso de prompts, embeddings, RAG e fine-tuning;
- politica de retencao e transferencia internacional;
- tipos de dados pessoais/sensiveis enviados para IA.

Ative o cenario `ai_llm_system`:
- `core`, `legal`, `governance`, `ai-llm`, `appsec`.

Adicione `eca-digital` se menores forem expostos a recomendacao algoritmica, perfilamento ou conteudo gerado por IA (gatilho normativo do router — ECA Digital, Lei 15.211/2025).

Adicione `plataformas-digitais` se a IA puder gerar ou alterar imagem ou som de pessoas (vedacao de conteudo intimo do art. 9 do Decreto 12.976/2026) ou moderar conteudo de terceiros (gatilho normativo do router — Decretos 12.975/2026 e 12.976/2026).

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar risco de prompt injection e vazamento contextual;
- exigir base legal para tratamento de dados em IA;
- consolidar score e relatorio no padrao de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
