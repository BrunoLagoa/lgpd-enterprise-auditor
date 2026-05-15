---
name: lgpd-ai-llm
description: Executa auditoria LGPD direcionada para sistemas com IA/LLM.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.0.0"
---

# LGPD AI/LLM

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- provedores de IA/LLM utilizados;
- uso de prompts, embeddings, RAG e fine-tuning;
- politica de retencao e transferencia internacional;
- tipos de dados pessoais/sensiveis enviados para IA.

Ative o cenario `ai_llm_system`:
- `core`, `legal`, `governance`, `ai-llm`, `appsec`.

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- validar risco de prompt injection e vazamento contextual;
- exigir base legal para tratamento de dados em IA;
- consolidar score e relatorio no padrao V2.
