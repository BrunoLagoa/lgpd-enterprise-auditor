# AI-LLM Module - AI Governance and Privacy

## Escopo
Auditar uso de IA/LLM com foco em privacidade, segurança e conformidade regulatória.

## Checklist atômico
- Prompts contêm dados pessoais/sensíveis sem anonimização?
- Há política de retenção para prompts, logs e embeddings?
- Existe risco de prompt injection e vazamento contextual?
- Há transferência internacional de dados com base legal válida?
- O uso de dados para treinamento/fine-tuning possui fundamento e consentimento quando necessário?
- Vetor de memória/RAG expõe dados além da finalidade?

## Critérios de evidência
- política de uso de IA e governança;
- configuração de retenção no provedor de LLM;
- evidência de anonimização/redação;
- documentação de fluxo internacional de dados;
- controles de segurança para RAG/vector database.

## Mapeamento para severidade e score
- Dado sensível enviado a LLM externo sem proteção/base legal: `CRITICO`.
- Retenção inadequada de prompts e embeddings: `ALTO`.
- Ausência parcial de política de IA: `MEDIO`.
- Área de scoring primária: `ai_llm` (10%), `bases_legais` (15%) e `governanca` (15%).
