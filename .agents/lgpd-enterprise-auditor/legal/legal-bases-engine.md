# Legal Bases Engine (V2)

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
Dados sensíveis (origem racial/étnica, convicção religiosa, opinião política, filiação sindical, dado referente a saúde, vida sexual, dado genético ou biométrico) possuem rol **próprio e mais restrito**:
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

## Resultado da validação
- `CONFORME`: base legal válida para o tipo de dado + evidência suficiente.
- `PARCIAL`: base legal indicada, mas sem comprovação robusta.
- `NAO_CONFORME`: ausência de base legal, base incompatível com a finalidade, ou base do art. 7º aplicada indevidamente a dado sensível.
