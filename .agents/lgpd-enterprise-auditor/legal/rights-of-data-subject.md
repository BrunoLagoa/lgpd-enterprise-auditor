# Rights of Data Subject

## Objetivo
Padronizar avaliação dos direitos do titular (arts. 17 a 22 da LGPD) e da transparência devida a ele (art. 9º).

## Direitos mínimos a validar (art. 18)
- confirmação da existência de tratamento (I);
- acesso aos dados (II);
- correção de dados incompletos, inexatos ou desatualizados (III);
- anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade (IV);
- portabilidade (V);
- eliminação dos dados tratados com consentimento (VI);
- informação sobre entidades públicas e privadas com as quais houve uso compartilhado (VII);
- informação sobre a possibilidade de não fornecer consentimento e as consequências da negativa (VIII);
- revogação do consentimento, nos termos do art. 8º, §5º (IX);
- oposição a tratamento fundado em hipótese de dispensa de consentimento, em caso de descumprimento da Lei (§2º);
- revisão de decisões tomadas unicamente com base em tratamento automatizado (art. 20) — ver [[llm-audit]].

## Prazos e forma de atendimento
- Requerimento expresso do titular ou de representante legalmente constituído, atendido **sem custos** (art. 18, §§3º e 5º).
- Confirmação de existência ou acesso (art. 19): **imediatamente**, em formato simplificado; ou por declaração clara e completa (origem dos dados, inexistência de registro, critérios e finalidade) em até **15 dias** contados do requerimento.
- Se não for possível adotar a providência de imediato, responder indicando as razões de fato ou de direito, ou o agente de tratamento efetivo quando o destinatário não o for (art. 18, §4º).
- Comunicar de imediato correção, eliminação, anonimização ou bloqueio aos agentes com quem os dados foram compartilhados (art. 18, §6º).

## Transparência e política de privacidade (art. 9º)
O titular tem direito ao acesso facilitado às informações sobre o tratamento, disponibilizadas de forma clara, adequada e ostensiva. Validar na política de privacidade (ver [[privacy-policy-template]]):
- finalidade específica do tratamento (I);
- forma e duração do tratamento (II);
- identificação e contato do controlador (III e IV);
- uso compartilhado e sua finalidade (V);
- responsabilidades dos agentes que realizarão o tratamento (VI);
- direitos do titular, com menção explícita aos do art. 18 (VII);
- base legal por finalidade e política de retenção;
- identidade e contato do encarregado (art. 41, §1º);
- cookies e transferência internacional, quando houver;
- linguagem acessível e indicação de versão/data de atualização.

Quando o consentimento é requerido, ele é nulo se as informações tiverem conteúdo enganoso ou abusivo ou não tiverem sido apresentadas previamente com transparência (art. 9º, §1º).

## Critérios de conformidade
- canal de atendimento claro e funcional;
- prazo de resposta definido e compatível com o art. 19;
- trilha de atendimento auditável;
- confirmação de execução da solicitação.

## Não conformidade comum
- ausência de canal de solicitação;
- falta de processo para exclusão/portabilidade;
- revogação de consentimento não operacional;
- política de privacidade genérica, sem finalidade e base legal por operação.

## Mapeamento para severidade e score
- Ausência de canal para exercício de direitos: `ALTO`.
- Revogação de consentimento não operacional: `ALTO`.
- Ausência de política de privacidade: `ALTO`.
- Resposta fora do prazo do art. 19 ou inexistência de fluxo de exclusão/portabilidade: `MEDIO`.
- Política de privacidade incompleta frente ao art. 9º: `MEDIO`.
- Problemas de clareza ou linguagem da política: `BAIXO`.
- Área de scoring primária: `direitos_titular` (15%); transparência contribui para `bases_legais` (15%).
