# Bases legais do tratamento (arts. 7º e 11, LGPD)

## Objetivo
Definir validação de base legal por operação de tratamento, distinguindo dados pessoais (art. 7º) de dados pessoais sensíveis (art. 11).

## Bases legais para dados pessoais (art. 7º, LGPD)
- consentimento (art. 7º, I);
- obrigação legal/regulatória (art. 7º, II);
- execução de políticas públicas pela administração pública (art. 7º, III);
- estudos por órgão de pesquisa, com anonimização sempre que possível (art. 7º, IV);
- execução de contrato ou de procedimentos preliminares a contrato (art. 7º, V);
- exercício regular de direitos em processo judicial, administrativo ou arbitral (art. 7º, VI);
- proteção da vida ou incolumidade física do titular ou de terceiro (art. 7º, VII);
- tutela da saúde, em procedimento realizado por profissionais/serviços de saúde (art. 7º, VIII);
- legítimo interesse do controlador ou de terceiro (art. 7º, IX);
- proteção do crédito (art. 7º, X).

## Bases legais para dados sensíveis (art. 11, LGPD)
Dados sensíveis (art. 5º, II: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural) possuem rol **próprio e mais restrito**:
- consentimento específico e destacado, para finalidades específicas (art. 11, I);
- sem consentimento, apenas nas hipóteses do art. 11, II: obrigação legal/regulatória; políticas públicas; estudos por órgão de pesquisa (anonimizando quando possível); exercício regular de direitos; proteção da vida/incolumidade física; tutela da saúde por profissionais de saúde; garantia da prevenção à fraude e à segurança do titular.

### Regra crítica de dados sensíveis
- **Legítimo interesse (art. 7º, IX) NÃO é base legal válida para dados sensíveis.** Seu uso para tratar dado sensível deve ser classificado como `NAO_CONFORME` com severidade `CRITICO`.
- "Proteção ao crédito" e "execução de contrato" também não constam do rol do art. 11; tratar dado sensível com essas bases é não conformidade.

## Regras de auditoria
- toda finalidade deve mapear para ao menos uma base legal do artigo aplicável (7º ou 11);
- antes de validar a base, classificar se a operação envolve dado pessoal comum ou sensível;
- base legal deve ser comprovável por evidência técnica e/ou documental;
- consentimento (art. 7º) deve ser específico, granular e revogável; consentimento para dado sensível (art. 11, I) deve ser, ainda, específico e destacado;
- uso de legítimo interesse deve ter justificativa formal documentada e teste de proporcionalidade/balanceamento (LIA).

## Dados de acesso público e dados manifestamente públicos (art. 7º, §§ 3º, 4º e 7º)
Dado público não é dado livre: estar acessível muda a análise, mas não afasta a LGPD.
- **Dados de acesso público** (ex.: diários oficiais, portais de transparência, dados abertos de órgãos como o TSE): o tratamento deve considerar a finalidade, a boa-fé e o interesse público que justificaram sua disponibilização (art. 7º, §3º).
- **Dados tornados manifestamente públicos pelo próprio titular**: dispensa-se apenas o **consentimento**, resguardados os direitos do titular e os princípios do art. 6º (art. 7º, §4º). Documentar qual base legal sustenta o tratamento (com frequência o legítimo interesse, com teste de balanceamento).
- **Tratamento posterior para novas finalidades** é possível se houver propósito legítimo e específico e se forem preservados os direitos do titular, os fundamentos e os princípios (art. 7º, §7º).
- **Dado sensível de acesso público** (ex.: filiação partidária ou dados de candidatos divulgados pelo TSE): não presumir dispensa. Enquadrar em uma hipótese do art. 11 e demonstrar compatibilidade com a finalidade da divulgação oficial (art. 7º, §3º); reutilização alinhada a essa finalidade, como transparência e controle social, com minimização, tende a ser legítima. Perfilamento ou combinação com outras bases para fins diversos exige avaliação de risco (RIPD).

Checklist:
- A origem pública de cada conjunto de dados está identificada (fonte, data de coleta, finalidade original da divulgação)?
- A finalidade do tratamento é compatível com a que justificou a divulgação, ou a nova finalidade é legítima e específica (art. 7º, §§ 3º e 7º)?
- Há base legal documentada (a dispensa do §4º é só do consentimento) e, para dado sensível, enquadramento no art. 11?
- Os dados são minimizados e os direitos do titular (correção, oposição, eliminação quando cabível) seguem atendidos?

Severidade: reutilização compatível e minimizada **não é achado por si só**. Ausência de análise documentada da compatibilidade: `MEDIO`. Uso incompatível com a finalidade da divulgação ou sem base legal: `ALTO`. `CRITICO` apenas com perfilamento discriminatório ou exposição indevida de dado sensível.

## Checklist atômico de consentimento (art. 8º)
Aplicável sempre que o consentimento (art. 7º, I ou art. 11, I) for a base legal indicada. Para cookies e tracking no front-end, ver a seção de cookies de [[owasp-api]].
- O consentimento é fornecido por escrito ou por outro meio que demonstre a manifestação de vontade (opt-in explícito, sem checkbox pré-marcado) (art. 8º, caput)?
- Em contrato escrito, consta de cláusula destacada das demais (art. 8º, §1º)?
- Há registro que permita ao controlador provar a obtenção regular do consentimento (art. 8º, §2º)?
- Refere-se a finalidades determinadas, sem autorizações genéricas (art. 8º, §4º)?
- A revogação é possível a qualquer momento, por procedimento gratuito e facilitado (art. 8º, §5º)?
- Alterações de finalidade, forma, duração ou compartilhamento são informadas com destaque, permitindo revogar (art. 8º, §6º e art. 9º, §2º)?
- Quando o tratamento é condição para o serviço, o titular é informado com destaque sobre isso e sobre como exercer seus direitos (art. 9º, §3º)?

## Mapeamento para severidade e score
- Legítimo interesse ou outra base do art. 7º aplicada a dado sensível: `CRITICO`.
- Consentimento genérico ou com checkbox pré-marcado: `ALTO`.
- Ausência de mecanismo de revogação do consentimento: `ALTO`.
- Ausência de registro que prove o consentimento ou consentimento pouco granular: `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `bases_legais` para todos os itens deste módulo.

## Resultado da validação
- `CONFORME`: base legal válida para o tipo de dado + evidência suficiente.
- `PARCIAL`: base legal indicada, mas sem comprovação robusta.
- `NAO_CONFORME`: ausência de base legal, base incompatível com a finalidade, ou base do art. 7º aplicada indevidamente a dado sensível.
