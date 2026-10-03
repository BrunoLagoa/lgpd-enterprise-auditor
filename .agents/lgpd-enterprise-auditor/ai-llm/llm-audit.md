# Módulo IA/LLM — governança e privacidade em inteligência artificial

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
- Existe geração ou manipulação sintética de imagem/voz de pessoas (deepfake) sem base legal?
- A funcionalidade de IA pode gerar ou alterar imagem ou som de terceiros? Se sim, há salvaguardas que bloqueiem a geração de conteúdo íntimo (vedação do art. 9º e salvaguardas do art. 10 do Decreto nº 12.976/2026)? Ativar [[plataformas-digitais]].
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
- Geração ou modificação de conteúdo íntimo de terceiro por IA (Decreto nº 12.976/2026, art. 9º): `CRITICO` — detalhado em [[plataformas-digitais]].
- Retenção inadequada de prompts e embeddings: `ALTO`.
- Ausência parcial de política de IA: `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `ai_llm` (domínio 12) para todos os itens deste módulo.

## Em monitoramento (não vigente — não gera não conformidade)
- **PL nº 2338/2023 — Marco Legal da IA**: aprovado no Senado em 10/12/2024, em tramitação na Câmara dos Deputados, sem sanção até 2026-09 (em set/2026, aguardando parecer do relator na Comissão Especial). Prevê classificação por nível de risco, direitos de transparência/explicação/contestação, governança de IA e sanções próprias.
- Enquanto não sancionado, mapear os controles correspondentes apenas como `recomendacoes_tecnicas` no relatório, rotulados como preparação para norma futura. Nunca gerar `finding` com fundamento no PL.
- **Rotulagem de conteúdo sintético** (identificação de imagem, voz ou vídeo gerados por IA): sem dever geral na base normativa vigente deste módulo; registrar apenas como `recomendacoes_tecnicas`.
