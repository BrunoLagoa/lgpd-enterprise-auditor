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
- Há decisão automatizada que afete interesses do titular, com direito a revisão assegurado (art. 20)?
- Existe geração ou manipulação sintética de imagem/voz de pessoas (deepfake) sem base legal e sem rotulagem?
- Menores estão expostos a recomendação algorítmica ou perfilamento? Se sim, ativar [[eca-digital]].
- Dados biométricos ou neurodados alimentam o modelo? Se sim, aplicar regime de dado sensível (art. 11).

## Referências técnicas da ANPD
Não vinculantes, mas úteis como parâmetro de boa prática e como evidência documental:
- Radar Tecnológico nº 3 — IA generativa;
- Radar Tecnológico nº 4 — Neurotecnologias;
- Radar Tecnológico nº 6 — Deepfakes;
- Notas técnicas de fiscalização sobre sistemas de IA (ex.: NT nº 1/2026 — Grok; atuações sobre IA generativa da Meta e uso de dados de menores).
Ver [[anpd-guidelines]] para a lista completa e para os temas prioritários de fiscalização 2026-2027.

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

## Em monitoramento (não vigente — não gera não conformidade)
- **PL nº 2338/2023 — Marco Legal da IA**: aprovado no Senado em 10/12/2024, em tramitação na Câmara dos Deputados, sem sanção até 2026-08. Prevê classificação por nível de risco, direitos de transparência/explicação/contestação, governança de IA e sanções próprias.
- Enquanto não sancionado, mapear os controles correspondentes apenas como `recomendacoes_tecnicas` no relatório, rotulados como preparação para norma futura. Nunca gerar `finding` com fundamento no PL.
