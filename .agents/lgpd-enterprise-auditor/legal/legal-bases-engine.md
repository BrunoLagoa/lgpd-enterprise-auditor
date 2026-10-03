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

## Papel do auditado: controlador ou operador
Antes de exigir base legal, identificar o papel do auditado **em cada fluxo de dados** (art. 5º, VI e VII):
- **Controlador**: decide sobre o tratamento. Responde por base legal, transparência, direitos do titular e comunicação de incidentes.
- **Operador**: trata dados em nome do controlador e segundo as instruções dele (art. 39). Um SaaS B2B costuma ser operador dos dados que seus clientes inserem (ex.: pacientes de uma clínica) e controlador dos dados das contas, de cobrança e de uso do próprio produto.
- Quem usa os dados recebidos para **finalidade própria** (ex.: analytics de produto, treino de modelo, marketing) passa a ser controlador dessa finalidade e precisa de base legal própria.

Quando o auditado é operador de um fluxo, **não** são achado dele, e ficam `NAO_APLICAVEL` com essa justificativa: a escolha da base legal, a coleta de consentimento, a política de privacidade dirigida aos titulares, o canal de direitos, o relatório de impacto (art. 38) e a comunicação de incidente à ANPD e aos titulares (art. 48) — obrigações do controlador. Agente com papel misto segue as regras do controlador nos fluxos em que é controlador (inclusive encarregado e RIPD) e as do operador nos demais. Continuam exigíveis do operador:
- Há contrato ou termo com o controlador que defina objeto, instruções, segurança, suboperadores e devolução ou eliminação dos dados ao fim (art. 39)?
- O tratamento se limita às instruções documentadas, sem uso dos dados para finalidade própria?
- Suboperadores (hospedagem, e-mail, analytics) são informados ao controlador e cobertos por contrato equivalente?
- Há medidas de segurança próprias (art. 46) e registro das operações que realiza (art. 37)?
- Existe processo para avisar o controlador sem demora em caso de incidente e para apoiá-lo no atendimento a titulares?
- Ao fim do contrato, os dados são devolvidos ou eliminados conforme instrução do controlador (art. 16)?

Contagem única: a segurança e o registro das operações do operador são avaliados nos itens de segurança e de registro já existentes, e o contrato com suboperador é o mesmo item do DPA com operadores de `governance/dpo-framework.md` — não criar item duplicado.

A indicação de encarregado pelo operador é facultativa (Res. CD/ANPD nº 18/2024). O operador responde solidariamente quando descumpre a LGPD ou as instruções lícitas do controlador (art. 42, §1º, I).

Severidade: operador que usa os dados para finalidade própria sem base legal: `ALTO` (`CRITICO` com dado sensível ou de crianças e adolescentes). Ausência de contrato com o controlador ou de processo de aviso de incidente: `ALTO`. Suboperador não informado ou sem contrato: `MEDIO` (`ALTO` com dado sensível ou de crianças e adolescentes). Sem processo de apoio ao controlador nos pedidos de titulares, ou sem devolução ou eliminação definida para o fim do contrato: `MEDIO`. Para essas regras, conta como dado sensível também o dado que **revele** informação sensível e possa causar dano ao titular (art. 11, §1º) — ex.: o registro de que alguém agendou consulta numa clínica. Área de score: `governanca` (domínio 14); o uso para finalidade própria pontua em `bases_legais`.

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
