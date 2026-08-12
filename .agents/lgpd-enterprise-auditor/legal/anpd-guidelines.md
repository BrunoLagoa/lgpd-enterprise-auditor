# ANPD Guidelines (V2)

## Objetivo
Guiar a aderência regulatória contínua com foco em evidência auditável.

## Natureza jurídica da ANPD (atualizado pela Lei nº 15.352/2026)
- A **Lei nº 15.352/2026** (25/02/2026, conversão da MP nº 1.317/2025) alterou a LGPD e transformou a ANPD em **agência reguladora**, submetida à Lei nº 13.848/2019, vinculada ao Ministério da Justiça e Segurança Pública, com autonomia funcional, técnica, decisória, administrativa e financeira (art. 55-A).
- O art. 5º, XIX passou a definir a ANPD como **entidade da administração pública** responsável por zelar, implementar e fiscalizar o cumprimento da LGPD.
- O art. 55-J vinculou a atuação normativa da ANPD ao rito da Lei nº 13.848/2019, exigindo **consulta pública e Análise de Impacto Regulatório (AIR)**.
- Nomenclatura correta em relatórios: **Agência Nacional de Proteção de Dados (ANPD)**. Evitar "Autoridade Nacional" em textos novos.
- Efeito prático para auditoria: ampliação da capacidade fiscalizatória (carreira própria de regulação e fiscalização, com 200 vagas) e nova competência sobre o **ECA Digital** — ver [[eca-digital]].

## Regulamentos vinculantes da ANPD a considerar
- **Resolução CD/ANPD nº 1/2021** — Regulamento do Processo de Fiscalização e do Processo Administrativo Sancionador (base do risco sancionatório).
- **Resolução CD/ANPD nº 2/2022** — regulamento de aplicação da LGPD para agentes de tratamento de pequeno porte.
- **Resolução CD/ANPD nº 4/2023** — regulamento de dosimetria e aplicação de sanções administrativas (parâmetros de cálculo de multas).
- **Resolução CD/ANPD nº 15/2024** — Regulamento de Comunicação de Incidente de Segurança (RCIS).
- **Resolução CD/ANPD nº 18/2024** — Regulamento sobre a atuação do **encarregado** pelo tratamento de dados pessoais — ver [[dpo-framework]].
- **Resolução CD/ANPD nº 19/2024** — Regulamento de Transferência Internacional de Dados e **cláusulas-padrão contratuais (CPC)** — ver [[international-transfer]].
- **Resolução CD/ANPD nº 30/2025** — Mapa de Temas Prioritários de fiscalização para o biênio 2026-2027.
- **Resolução CD/ANPD nº 31/2025** — atualização da Agenda Regulatória 2025-2026.
- **Resolução CD/ANPD nº 32/2026** (26/01/2026) — reconhece a **União Europeia** como organismo internacional com grau adequado de proteção de dados.

## Comunicação de incidente de segurança (Res. CD/ANPD nº 15/2024)
- Comunicar à ANPD e aos titulares incidente que possa acarretar **risco ou dano relevante**.
- **Prazo: 3 (três) dias úteis** contados do conhecimento do incidente, podendo ser complementado em até **20 (vinte) dias úteis** a partir da primeira comunicação.
- A não comunicação ou comunicação fora do prazo sujeita o agente a processo administrativo sancionador (art. 52, LGPD).

## Priorização de risco por temas de fiscalização (Res. CD/ANPD nº 30/2025)
Ao priorizar não conformidades no plano de adequação, considerar que a ANPD sinalizou foco fiscalizatório em:
- proteção de crianças e adolescentes no ambiente digital (LGPD art. 14 + ECA Digital);
- tratamento de dados por sistemas de inteligência artificial;
- transferência internacional de dados;
- comunicação de incidentes de segurança;
- dados biométricos e reconhecimento facial.

Essa priorização **não cria requisito legal novo** — ela apenas eleva a urgência do item já não conforme no plano de adequação.

## Documentos técnicos e orientativos de referência
Não são vinculantes, mas expressam o entendimento da ANPD e servem como **evidência documental** de boa prática:
- Radar Tecnológico nº 6 — Deepfakes;
- Radar Tecnológico nº 5 — Mecanismos de aferição de idade;
- Radar Tecnológico nº 4 — Neurotecnologias;
- Radar Tecnológico nº 3 — IA generativa;
- Radar Tecnológico nº 2 — Biometria e reconhecimento facial;
- Estudos técnicos sobre anonimização e sobre tratamento de dados de crianças e adolescentes;
- Notas técnicas de fiscalização (ex.: NT nº 1/2026 sobre sistema de IA Grok; NT nº 58/2025 sobre compartilhamento WhatsApp/Grupo Meta).

## Diretrizes operacionais
- Documentar decisões de tratamento e bases legais.
- Manter registro de operações de tratamento atualizado.
- Definir procedimento de resposta ao titular e a incidentes, com prazo de comunicação alinhado à Res. 15/2024.
- Demonstrar accountability com trilha de auditoria e governança ativa.

## Evidências recomendadas
- políticas internas versionadas;
- registro de revisão jurídica;
- fluxo de atendimento ao titular;
- atas/comitês de privacidade;
- histórico de incidentes e tratativas.

## Em monitoramento (não vigente — não gera não conformidade)
Itens abaixo **não podem** originar `finding` nem `check_item` com status `NAO_CONFORME`. Usar apenas na seção `recomendacoes_tecnicas` do relatório, sempre rotulados como norma não vigente:
- **PL nº 2338/2023 — Marco Legal da IA**: aprovado no Senado em 10/12/2024, em tramitação na Câmara dos Deputados. Prevê classificação por nível de risco, direitos dos afetados e governança de IA.
- **Guias orientativos da ANPD em tomada de subsídios** (ex.: aferição de idade e fornecedores de tecnologia no âmbito do ECA Digital): a versão final pode alterar parâmetros; tratar a versão em consulta como referência preliminar.
- **Normas complementares do ECA Digital ainda não publicadas**: parâmetros definitivos de aferição de idade previstos para a etapa regulatória iniciada em agosto/2026 — ver [[eca-digital]].
