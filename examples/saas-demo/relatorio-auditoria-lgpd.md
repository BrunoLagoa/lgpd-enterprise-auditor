CONFIDENCIAL — uso interno

> **Exemplo público com dados fictícios.** Este relatório foi produzido sobre o projeto fictício e intencionalmente falho de `examples/saas-demo/` para demonstrar o LGPD Enterprise Auditor. Empresa, pessoas, CNPJ, domínios e dados são inventados. Relatórios reais descrevem falhas que podem estar abertas: são confidenciais, não devem ser versionados em repositório público e seguem a convenção de nome `auditoria-lgpd-AAAA-MM-<cenario>.md` de `core/reporting-engine.md`. Este arquivo foge das duas regras só por ser um exemplo público.

# Relatório de auditoria LGPD — AgendaFácil

| Campo | Valor |
|---|---|
| Projeto auditado | `examples/saas-demo/` — AgendaFácil (fictício) |
| Data da análise | 2026-10-03 |
| Comando | `/lgpd-saas` |
| Cenário | `saas_web` |
| Framework | LGPD Enterprise Auditor 1.4.0, base canônica `.agents/lgpd-enterprise-auditor/` |
| Método | leitura estática dos arquivos do repositório; sem acesso ao ambiente de produção, aos painéis da Vercel, do banco e do GitHub, nem a contratos fora do repositório |

## Contexto e escopo

### O que foi inferido dos arquivos do projeto

Antes de qualquer pergunta, foram lidos `README.md`, `docs/`, `package.json`, `vercel.json`, `.env.example`, `.github/workflows/ci.yml`, `db/schema.sql` e o código de `api/`, `src/` e `public/`.

| Entrada do roteador | Contexto inferido | Fonte |
|---|---|---|
| Natureza do agente | Pessoa jurídica com fins econômicos; microempresa do Simples Nacional, 3 sócios | `README.md:13-14` |
| Papel em cada fluxo | Operadora dos dados dos pacientes; controladora das contas das clínicas e do rastreamento que ela mesma instalou (detalhe abaixo) | `README.md:9` e `:16`, `db/schema.sql:11-39`, `public/index.html:7-15` |
| Stack | Node.js 20 + Express 5, JWT; front-end estático | `README.md:20-21`, `package.json:15-22` |
| Hospedagem e banco | Vercel (funções em `gru1`, CDN para estáticos); Postgres gerenciado em `sa-east-1` | `vercel.json:3-4`, `.env.example:5-6`, `README.md:22-23` |
| Integrações | Meta Pixel na página pública de agendamento, para campanhas da própria AgendaFácil | `public/index.html:7-15`, `README.md:24` |
| IA/LLM | Nenhuma: sem SDK de IA nas dependências e nenhum fluxo de IA declarado | `package.json:15-25`, `README.md:18-25` |
| DevSecOps | GitHub Actions com lint, testes e deploy; sem varreduras de segurança | `.github/workflows/ci.yml` |
| Faixa etária do público | Serviço B2B para clínicas que atendem só adultos; o agendamento bloqueia menores de 18 anos pela data de nascimento informada | `README.md:15`, `src/routes/agendamentos.js:23-27` |
| Dados tratados | Nome, CPF, telefone, e-mail, data de nascimento e motivo da consulta (texto livre) dos pacientes; e-mail e hash de senha dos usuários das clínicas | `db/schema.sql:11-39`, `README.md:29` |

Confirmações pedidas ao fim do levantamento (respostas simuladas para este exemplo). A fundadora:

- confirmou o porte, a ausência de IA e que o Meta Pixel foi instalado por decisão da AgendaFácil, para suas próprias campanhas;
- informou que `docs/lgpd/` reúne toda a documentação de privacidade que a empresa tem;
- informou que não há contrato de proteção de dados assinado com clínicas nem com provedores, e que os termos padrão aceitos no cadastro da Vercel, do banco e da Meta não foram reunidos para análise.

### Natureza e papel do agente de tratamento

- **Pessoa jurídica com fins econômicos**, portanto sujeita à LGPD (a exclusão do art. 4º, I, não se aplica).
- **Agente de tratamento de pequeno porte** (microempresa, Res. CD/ANPD nº 2/2022).
- **Há tratamento de alto risco.** O motivo da consulta (`db/schema.sql:37`, `public/index.html:35`) é **dado pessoal sensível referente à saúde** (art. 5º, II). Pelos critérios da Res. CD/ANPD nº 2/2022 (art. 4º), o uso de dados sensíveis é um critério específico de alto risco. O critério geral também está presente: a exposição de dados de saúde de cerca de 25 mil pacientes pode afetar significativamente seus interesses e direitos fundamentais.

**Papel em cada fluxo de dados** (`legal/legal-bases-engine.md`, seção "Papel do auditado"):

| Fluxo | Papel da AgendaFácil | Consequência na auditoria |
|---|---|---|
| Dados dos pacientes inseridos no agendamento (nome, CPF, contato, data de nascimento, motivo da consulta) | **Operadora**. As clínicas são as controladoras | Base legal, consentimento, política dirigida aos pacientes e canal de direitos são obrigações das clínicas e ficam `NAO_APLICAVEL`. Valem os itens de operador (OP-01 a OP-06), a segurança própria e o registro das operações |
| Rastreamento da página de agendamento pelo Meta Pixel, instalado pela AgendaFácil para suas campanhas | **Controladora** dessa finalidade própria | Precisa de base legal própria; os itens de cookies, transparência, direitos e transferência internacional ficam `APLICAVEL` |
| Contas dos usuários das clínicas (e-mail e senha) e, quando existirem, cobrança e dados de uso do produto | **Controladora** | Base legal, transparência, direitos, retenção e incidentes são obrigações da AgendaFácil. O repositório não tem código de cobrança |

Hoje nenhum documento registra essa divisão (ver OP-01).

**Consequências do porte e do alto risco:**

1. **Nenhuma severidade foi modulada.** O `core/severity-model.md` só permite reduzir a severidade em um nível quando as três condições são verdadeiras ao mesmo tempo: pequeno porte, **ausência** de tratamento de alto risco e ausência de exposição explorável confirmada. A segunda condição falha, então todas as severidades e `criticality` deste relatório são as originais.
2. **As dispensas do pequeno porte não se aplicam.** O tratamento de alto risco está entre as exclusões da Res. CD/ANPD nº 2/2022 (art. 3º). A indicação de encarregado é facultativa para o operador, mas a AgendaFácil também é controladora (contas e rastreamento) e, sem a dispensa, precisa indicá-lo. O registro das operações deve ser o completo, não o simplificado (`governance/dpo-framework.md`). Recomenda-se confirmar o enquadramento com a assessoria jurídica.

### Módulos ativados (saída do roteador)

| Módulo | Ativado | Justificativa |
|---|---|---|
| `core` | sim | obrigatório em todo cenário |
| `legal` | sim | obrigatório em todo cenário; inclui bases legais, papel do auditado, direitos do titular e transferência internacional |
| `governance` | sim | cenário `saas_web` |
| `appsec` | sim | cenário `saas_web`; há API pública (`/api/agendamentos`) |
| `cloud` | sim | cenário `saas_web`; hospedagem em PaaS e banco gerenciado |
| `devsecops` | sim | cenário `saas_web`; CI/CD ativo |

**Escopo excluído explicitamente:**

- `eca-digital`: módulo não ativado. O único controle etário é a data de nascimento **autodeclarada** (`src/routes/agendamentos.js:23-27`). Pelo `orchestrator/router.md`, a autodeclaração não afasta o gatilho quando existe qualquer outro indício da lista. Aqui não existe nenhum: o serviço é B2B, contratado por clínicas que atendem só adultos (`README.md:15`); a página de agendamento não é direcionada a menores nem tem atrativo para eles; não há jogos, itens virtuais, monetização por engajamento nem aplicativo em loja. Sem outro indício, o módulo não é ativado e a decisão fica registrada aqui. Se alguma clínica passar a atender menores, ativar `eca-digital` e reavaliar o art. 14 da LGPD.
- `plataformas-digitais`: não há conteúdo de terceiros com difusão pública, venda de anúncios ou impulsionamento, nem IA que gere ou altere imagem ou som. Como a AgendaFácil é provedora de aplicações de internet, os deveres gerais do art. 16-A do Decreto nº 8.771/2016 foram verificados por `governance` (GV-06), com o mapeamento de severidade de `legal/plataformas-digitais.md`. A guarda de registros de acesso (MCI, art. 15) é avaliada uma única vez, como item de `cloud` (IN-04).
- `ai-llm`: não há IA no produto (ver área `ai_llm` em `score_lgpd`).
- `mobile`: não há aplicativo móvel.

### Limitações e convenções

- **Aplicabilidade** (`core/scoring-engine.md`): cada item é `APLICAVEL`, `NAO_APLICAVEL` ou `NAO_VERIFICADO`. Só o item `APLICAVEL` tem status e entra no score.
  - `NAO_APLICAVEL`: o objeto não existe no projeto, com evidência da inexistência, ou a obrigação é de outro agente (aqui, das clínicas controladoras).
  - `NAO_VERIFICADO`: controle técnico que só pode ser conferido na produção ou no painel de um provedor. Gera uma verificação pendente.
  - Documento que deveria existir e não foi apresentado é `AUSENTE` e reduz o score; nunca é `NAO_VERIFICADO`.
- **Achados** (`core/auditor-core.md`): todo item `NAO_CONFORME` ou `PARCIAL` gera um achado em `nao_conformidades`.
  - No `NAO_CONFORME`, a severidade do achado é a `criticality` do item.
  - No `PARCIAL`, a severidade reflete a lacuna que resta e nunca passa da `criticality`.
- **Contagem única** (`core/scoring-engine.md`): uma mesma falha (mesma causa e mesma evidência) reprova só o item mais específico. Os outros itens afetados a citam e só são reprovados se representarem uma obrigação legal distinta. Neste relatório:
  - O Meta Pixel reprova três itens, por três obrigações distintas: OP-02 (operadora que usa dados dos pacientes para finalidade própria, art. 39), CK-02 (rastreamento antes do consentimento, arts. 7º, I e 8º) e GV-05 (transferência internacional, art. 33). CK-03 cita a mesma falha e só pontua pela lacuna própria da revogação.
  - A CSP enfraquecida pela hospedagem reprova só IN-01; SE-02 a cita.
  - A falta de limitação de tentativas no login reprova só AP-03; SE-04 a cita.
  - A falta de contrato com as clínicas reprova só OP-01; BL-02 e GV-01 a citam.
  - A falta de processo de incidentes reprova só OP-04, que reúne o aviso às clínicas e a comunicação à ANPD dos dados próprios.
- **Evidência:** formato `GRAU (ORIGEM), confiança NIVEL: descrição`, com caminho e linha dos arquivos do projeto; várias evidências são separadas por ponto e vírgula. Confiança, pela escala de `core/evidence-engine.md`:
  - `ALTA`: prova direta e rastreável do que o item exige;
  - `MEDIA`: prova direta de um lado só (por exemplo, o código sem confirmação em produção, ou a ausência constatada no repositório e declarada pela fundadora);
  - `BAIXA`: prova indireta ou incompleta.
- **Prazos:** `IMEDIATO` significa até 7 dias. `IMEDIATO` e `30_DIAS` entram no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo.
- **IDs dos itens:** `BL` bases legais, `CK` cookies, `OP` obrigações de operador, `SE`/`DS` segurança e DevSecOps, `DT` direitos do titular, `GV` governança, `IN` infraestrutura, `AP` APIs e integrações.

---

## 1. Resumo executivo

### Nível geral de conformidade

**Score LGPD: 35/100. Classificação: `CRITICO`.** Cobertura da análise: 88,4% (38 de 43 itens verificáveis), acima do mínimo de 80%; o score não é parcial.

O AgendaFácil tem uma base técnica razoável (senhas com bcrypt, HTTPS, controle de acesso por papel, consultas parametrizadas, segredos fora do código). Dois problemas puxam o resultado para baixo:

1. **A AgendaFácil usa dados de pacientes para fim próprio.** Ela é operadora das clínicas, mas instalou um pixel de publicidade na página em que os pacientes marcam consulta. É o único achado `CRITICO`.
2. **Quase nenhum documento existe.** Não há contrato com as clínicas nem com os provedores, registro das operações, encarregado, processo de incidentes ou aviso de privacidade publicado. O score documental é 10,3; o técnico, 45,6.

Como o produto trata **dados de saúde**, nenhuma severidade pôde ser reduzida pelo porte da empresa. Por outro lado, o papel de operadora tira da AgendaFácil obrigações que são das clínicas: a base legal dos dados dos pacientes, o consentimento, a política dirigida a eles e o canal de direitos ficaram fora do cálculo.

As cinco ações abaixo custam pouco e atacam os riscos mais graves. Três delas se resolvem em menos de uma semana.

### Síntese de riscos por severidade

| Severidade | Achados | Itens |
|---|---|---|
| `CRITICO` | 1 | OP-02 |
| `ALTO` | 17 | CK-02, SE-06, SE-07, DS-02, DT-01, DT-03, GV-01, GV-02, GV-03, GV-05, GV-06, OP-01, OP-03, OP-04, IN-01, AP-01, AP-02 |
| `MEDIO` | 11 | BL-02, CK-03, CK-04, CK-05, SE-04, DT-02, DT-04, GV-04, OP-05, OP-06, AP-03 |
| `BAIXO` | 1 | DS-03 |

Dos 54 itens do checklist, 38 são `APLICAVEL` (8 `CONFORME`, 7 `PARCIAL` e 23 `NAO_CONFORME`), 11 são `NAO_APLICAVEL` e 5 são `NAO_VERIFICADO`.

### O que fazer agora

| # | Ação, em linguagem simples | Por que importa | Esforço | Prazo | Itens |
|---|---|---|---|---|---|
| 1 | Tirar o Meta Pixel da página de agendamento. Se ele for necessário para marketing, usá-lo só no site institucional, e só depois do "Aceitar". | A AgendaFácil trata os dados dos pacientes em nome das clínicas. Usar a visita e o agendamento deles para a própria publicidade foge desse papel, revela que a pessoa procura atendimento de saúde e envia isso à Meta, nos EUA, antes de qualquer escolha. | P | `IMEDIATO` | OP-02, CK-02, CK-03, GV-05 |
| 2 | Parar de gravar CPF e e-mail nos logs e apagar os logs antigos da Vercel. | Qualquer pessoa com acesso aos logs vê CPF e e-mail de pacientes. | P | `IMEDIATO` | SE-06 |
| 3 | Fazer a tela de confirmação receber só data, horário e primeiro nome; dar validade de 8 horas ao login (JWT); corrigir a CSP do `vercel.json`. | A API de confirmação devolve CPF e motivo da consulta a quem tiver o código; um token de login vazado vale para sempre; a CSP atual desliga a proteção contra scripts maliciosos. | P | `IMEDIATO` | AP-02, AP-01, IN-01 |
| 4 | Formalizar os contratos: termos com as clínicas (quem é controlador, quem é operador, instruções, aviso de incidentes) e contratos de proteção de dados com a Vercel e o provedor do banco, conferindo se trazem as cláusulas-padrão da ANPD. | Sem contrato, a AgendaFácil responde junto com as clínicas por qualquer problema e não consegue demonstrar a base dos envios de dados ao exterior. | M | `30_DIAS` | OP-01, OP-03, OP-04, GV-05 |
| 5 | Publicar um aviso de privacidade da própria AgendaFácil (contas das clínicas e cookies), com canal para pedidos e contato do encarregado, e deixar claro que os dados dos pacientes são de responsabilidade das clínicas. | O link do rodapé não leva a página nenhuma, não há canal para pedidos e o texto atual confunde os papéis. | M | `30_DIAS` | DT-01, DT-03, DT-04, GV-02 |

### Riscos aceitos

Nenhum risco `CRITICO` foi aceito. Há um risco `ALTO` aceito (GV-03, RIPD do rastreamento para fins próprios), detalhado em `nao_conformidades` e em `riscos_identificados`. O aceite não altera o score.

### Pontos fortes

Senhas com bcrypt (SE-01), HTTPS com HSTS (SE-02), controle de acesso por papel e isolamento por clínica (SE-03), consultas parametrizadas e saída escapada (SE-05), segredos do pipeline em secrets do CI (DS-01), segredos fora do repositório (IN-02), TLS com o banco (AP-04) e banner com botão "Rejeitar" tão visível quanto "Aceitar" (CK-01). Os dados em repouso ficam no Brasil (`sa-east-1`).

---

## 2. Score LGPD

### Resultado

| Indicador | Valor |
|---|---|
| **Score global** | **35/100** |
| **Classificação final** | **`CRITICO`** (faixa 0-49) |
| Cobertura global | 88,4% (38 itens com status ÷ 43 verificáveis); acima de 80%, o score **não** é parcial |
| `score_tecnico` (informativo) | 45,6 |
| `score_documental` (informativo) | 10,3 |
| Natureza do agente | pessoa jurídica com fins econômicos, de pequeno porte, com tratamento de alto risco (dados de saúde) |
| Papel do agente | operadora dos dados dos pacientes; controladora das contas das clínicas e do rastreamento para fins próprios |
| Modulação de severidade | nenhuma: a condição "sem tratamento de alto risco" de `core/severity-model.md` não é atendida |

### Regras aplicadas (`core/scoring-engine.md`)

- Só itens `APLICAVEL` entram nas somas; `NAO_APLICAVEL` e `NAO_VERIFICADO` ficam fora.
- Valor do item: `CONFORME` = 1; `PARCIAL` = 0,5; `NAO_CONFORME` = 0.
- Peso do item pela `criticality`: `CRITICO` = 4; `ALTO` = 3; `MEDIO` = 2; `BAIXO` = 1 (sem modulação).
- `score_area = 100 × Σ(valor × peso) / Σ(peso)`. Cada item pontua em uma única área, definida pelo domínio, e cada falha é contada uma única vez.
- `score_global = Σ(score_area × peso_ajustado_area)`.
- O cálculo usa valores exatos. O score de cada área aparece com uma casa decimal, e só o score global é arredondado.

### Área não aplicável

| Área | Status | Justificativa |
|---|---|---|
| `ai_llm` | `NAO_APLICAVEL` | O módulo `ai-llm` não é acionado pelo cenário `saas_web`, e a exclusão está registrada no escopo excluído do roteador. Também não há objeto a avaliar: nenhuma dependência de SDK ou provedor de IA (`package.json:15-25`) e nenhum fluxo de IA declarado (`README.md:18-25`). Primeiro critério de `NAO_APLICAVEL` de `core/scoring-engine.md`. |

As seis áreas restantes somam 90%. Cada peso foi dividido por 0,90: `peso_ajustado_area = peso_area / 0,90`.

### Cálculo e cobertura por área

| Área | Itens com status | Σ(valor × peso) | Σ(peso) | `score_area` | Peso original | Peso ajustado | `NAO_VERIFICADO` | Cobertura | `NAO_APLICAVEL` |
|---|---|---|---|---|---|---|---|---|---|
| `bases_legais` | 7 | 6,0 | 19 | 31,6 | 15% | 16,67% | 0 | 100% | 2 |
| `seguranca` | 10 | 18,5 | 30 | 61,7 | 25% | 27,78% | 0 | 100% | 3 |
| `direitos_titular` | 4 | 1,0 | 10 | 10,0 | 15% | 16,67% | 0 | 100% | 2 |
| `governanca` | 11 | 2,5 | 30 | 8,3 | 15% | 16,67% | 0 | 100% | 2 |
| `infraestrutura` | 2 | 4,0 | 7 | 57,1 | 10% | 11,11% | 5 | 28,6% | 2 |
| `apis_integracoes` | 4 | 3,0 | 11 | 27,3 | 10% | 11,11% | 0 | 100% | 0 |
| `ai_llm` | — | — | — | `NAO_APLICAVEL` | 10% | — | — | — | — |
| **Total** | **38** | **35,0** | **107** | | **100%** | **100%** | **5** | **88,4%** | **11** |

**Score global = 35** (valor exato 34,827…, arredondado para o inteiro mais próximo).

Cobertura = itens com status ÷ (itens com status + itens `NAO_VERIFICADO`). A área `infraestrutura` recebe a marca **cobertura baixa** (28,6%, abaixo de 50%): seu score (57,1) se apoia em só 2 dos 7 itens verificáveis e deve ser lido com cautela até as verificações pendentes serem feitas.

**Memória de cálculo** (valor × peso de cada item, na ordem do checklist; frações exatas):

- `bases_legais`: BL-02 0,5×3 + OP-02 0×4 + CK-01 1×2 + CK-02 0×3 + CK-03 0,5×3 + CK-04 0,5×2 + CK-05 0×2 = 1,5 + 0 + 2 + 0 + 1,5 + 1 + 0 = **6 / 19**
- `seguranca`: SE-01 1×4 + SE-02 1×3 + SE-03 1×3 + SE-04 0,5×3 + SE-05 1×3 + SE-06 0×3 + SE-07 0×3 + DS-01 1×4 + DS-02 0×3 + DS-03 0×1 = 4 + 3 + 3 + 1,5 + 3 + 0 + 0 + 4 + 0 + 0 = **18,5 / 30**
- `direitos_titular`: DT-01 0×3 + DT-02 0×2 + DT-03 0×3 + DT-04 0,5×2 = **1 / 10**
- `governanca`: GV-01 0×3 + GV-02 0×3 + GV-03 0×3 + GV-04 0×2 + GV-05 0×3 + GV-06 0,5×3 + OP-01 0×3 + OP-03 0×3 + OP-04 0×3 + OP-05 0,5×2 + OP-06 0×2 = 1,5 + 1 = **2,5 / 30**
- `infraestrutura`: IN-01 0×3 + IN-02 1×4 = **4 / 7**
- `apis_integracoes`: AP-01 0×3 + AP-02 0×3 + AP-03 0×2 + AP-04 1×3 = **3 / 11**
- **Global:** [15 × (600/19) + 25 × (1850/30) + 15 × (100/10) + 15 × (250/30) + 10 × (400/7) + 10 × (300/11)] / 90 = 3.134,51 / 90 = 34,827… → **35 → `CRITICO`**

### Score técnico e score documental (informativos)

Mesma fórmula, aplicada a todos os itens `APLICAVEL` de cada `control_type`. Não entram na classificação final.

| Subtotal | Itens | Σ(valor × peso) | Σ(peso) | Score |
|---|---|---|---|---|
| `score_tecnico` (`TECNICO`) | 24 | 31,0 | 68 | **45,6** |
| `score_documental` (`DOCUMENTAL`) | 14 | 4,0 | 39 | **10,3** |

Itens `DOCUMENTAL`: BL-02, DT-01 a DT-04, GV-01 a GV-06, OP-01, OP-03 e OP-04. Todos os demais são `TECNICO`. Leitura: o código tem falhas pontuais e corrigíveis, mas a lacuna maior é documental. Quase nada do que a LGPD pede por escrito existe hoje.

### Verificações pendentes que podem alterar o score

**Itens `NAO_VERIFICADO`** (fora do cálculo até a verificação; cada um pode entrar como `CONFORME`, `PARCIAL` ou `NAO_CONFORME`):

| Item | O que falta conferir | Acesso necessário |
|---|---|---|
| IN-03 | Criptografia em repouso, proteção dos backups e acesso restrito ao banco (`criticality` `ALTO`) | Painel do provedor do Postgres |
| IN-04 | Guarda dos registros de acesso por 6 meses, sob sigilo (`MEDIO`) | Painel da Vercel: retenção e exportação de logs |
| IN-05 | Membros, privilégio mínimo e MFA nos painéis; escopo dos tokens de deploy (`ALTO`) | Painéis da Vercel, do banco e do GitHub |
| IN-06 | Retenção e acesso aos logs e ao analytics nativos da plataforma (`MEDIO`) | Painel da Vercel |
| IN-07 | Firewall, WAF e monitoramento capazes de detectar acesso indevido (`MEDIO`) | Painel da Vercel |

**Itens cuja severidade ou status dependem de verificação ainda não feita:**

| Item | Situação atual | O que pode mudar | Verificação |
|---|---|---|---|
| GV-05 | `NAO_CONFORME`, `ALTO` (peso 3): mecanismo de transferência não evidenciado; confiança `BAIXA` | Sobe para `CRITICO` (peso 4) se os termos não tiverem CPC nem outro mecanismo. Se as CPC estiverem incorporadas, resta a falta de informação ao titular | Examinar os termos da Meta, da Vercel e do provedor do banco |
| OP-03 | `NAO_CONFORME`, `ALTO`: contratos com suboperadores não evidenciados; confiança `BAIXA` | Passa a `PARCIAL` se os termos padrão já trouxerem DPA; segue faltando informar os suboperadores às clínicas | Reunir os DPAs e os termos aceitos no cadastro |
| DS-02 | `NAO_CONFORME`, `ALTO`: sem varredura no pipeline; confiança `MEDIA` | Passa a `PARCIAL` se alertas do Dependabot ou CodeQL estiverem ligados nas configurações do repositório | Configurações de segurança do GitHub |
| AP-03 | `NAO_CONFORME`, `MEDIO`: sem limitação de taxa no código; confiança `MEDIA` | Passa a `PARCIAL` ou `CONFORME` se houver limitação no firewall da plataforma | Painel da Vercel |
| IN-01 | `NAO_CONFORME`, `ALTO`: CSP fraca no `vercel.json`; confiança `MEDIA` | A coleta dos cabeçalhos confirma o achado e mostra qual política vale nas respostas da API | `curl -I` na página e na API em produção |
| DT-03 | `NAO_CONFORME`, `ALTO`: página da política ausente do deploy; confiança `MEDIA` | Passa a `PARCIAL` se a página existir em produção por outro meio | `curl -I https://<domínio>/privacidade` |
| SE-02 | `CONFORME`, confiança `MEDIA`: HSTS comprovado no código da API | Passa a `PARCIAL` se as páginas estáticas não receberem HSTS | `curl -I` na página em produção |
| OP-02 | `NAO_CONFORME`, `CRITICO`; confiança `MEDIA` | Não muda a severidade; mostra a extensão do que a Meta recebe (por exemplo, campos do formulário pela correspondência avançada automática) | Captura de rede (HAR) antes e depois do aceite; configuração do pixel no Gerenciador de Eventos da Meta |

### Efeito do risco aceito

O item GV-03 (RIPD) tem aceite de risco registrado e continua `NAO_CONFORME`, com valor 0 e peso 3 em `governanca`. Com ou sem o aceite, `governanca` = 2,5 / 30 = 8,3 e o score global = 35. Aceitar um risco não torna o item conforme.

---

## 3. Checklist de conformidade

As tabelas por área listam só os itens `APLICAVEL`. Na coluna **Item**: ID · `criticality` (define o peso) · `control_type` — requisito. Os itens `NAO_APLICAVEL` e `NAO_VERIFICADO` estão na tabela "Itens fora do cálculo", logo depois.

### `bases_legais`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **BL-02** · `ALTO` · `DOCUMENTAL` — Base legal comprovável dos tratamentos em que a AgendaFácil é controladora (contas dos usuários das clínicas) | `bases_legais` | `PARCIAL` | `PARCIAL (TECNICA + DOCUMENTAL)`, confiança `BAIXA`: a relação contratual com as clínicas, que sustentaria o art. 7º, V, aparece só de forma indireta (`README.md:16`; contas ligadas à clínica em `db/schema.sql:11-18`); nenhum documento nomeia a base legal. A falta de termos com as clínicas é contada em OP-01 | Base legal não demonstrável numa fiscalização | Nomear a base de cada tratamento próprio no registro e no aviso de privacidade |
| **OP-02** · `CRITICO` · `TECNICO` — Tratamento dos dados dos pacientes limitado às instruções do controlador, sem uso para finalidade própria | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: o Meta Pixel da própria AgendaFácil ("campanhas de aquisição", `public/index.html:7-15`; `README.md:24`) registra a visita à página da clínica e o evento de agendamento (`public/js/agendar.js:23`); nenhuma instrução ou autorização das clínicas documentada; sem captura de rede em produção | Operadora usa dados dos pacientes para publicidade própria; a visita e o agendamento revelam busca por atendimento de saúde (art. 11, §1º) | Remover o pixel da página de agendamento |
| **CK-01** · `MEDIO` · `TECNICO` — "Rejeitar" na primeira camada, com o mesmo destaque de "Aceitar" | `bases_legais` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: botões lado a lado, com o mesmo elemento e o mesmo estilo (`public/index.html:41-45` e `:22`); ambos gravam a escolha (`public/js/consent.js:24-25`) | — | Manter |
| **CK-02** · `ALTO` · `TECNICO` — Scripts de publicidade e analytics bloqueados até o aceite | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: `public/index.html:8-15` carrega `fbevents.js` e dispara `PageView` no `<head>`, antes de `consent.js` rodar (`public/index.html:53`); nenhuma outra base legal documentada | Rastreamento sem consentimento válido, inclusive de quem clica em "Rejeitar" | Carregar qualquer rastreador só após o aceite |
| **CK-03** · `ALTO` · `TECNICO` — Revogação efetiva das preferências a qualquer momento | `bases_legais` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: o link "Preferências de cookies" reabre o banner (`public/index.html:50`, `public/js/consent.js:26-29`) e a recusa chama `fbq('consent', 'revoke')` (`consent.js:6-9`), o que interrompe os eventos seguintes, mas não remove o cookie `_fbp` nem o script já carregado; o `PageView` enviado antes da escolha é a falha de CK-02 e não é contado de novo aqui | Identificador da Meta continua no navegador depois da revogação | Na revogação, apagar `_fbp` e não recarregar o pixel |
| **CK-04** · `MEDIO` · `TECNICO` — Registro das escolhas como prova do consentimento | `bases_legais` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: a escolha fica só no `localStorage` do navegador, com data, mas sem versão do banner nem categorias (`public/js/consent.js:12`) | A AgendaFácil não consegue provar o consentimento | Registrar no servidor data, versão do banner e categorias |
| **CK-05** · `MEDIO` · `TECNICO` — Consentimento granular por finalidade, com terceiros identificados | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: o banner oferece apenas aceitar ou rejeitar tudo e o texto não cita publicidade nem a Meta (`public/index.html:42`) | Consentimento genérico, sem informação prévia adequada | Separar categorias (necessários, medição, publicidade) e nomear os terceiros |

### `seguranca`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **SE-01** · `CRITICO` · `TECNICO` — Senhas armazenadas com hash forte | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: bcrypt com custo 12 (`src/auth.js:5-8`), comparação em `src/auth.js:19`; coluna `senha_hash` (`db/schema.sql:15`) | — | Manter |
| **SE-02** · `ALTO` · `TECNICO` — HTTPS obrigatório com HSTS | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `MEDIA`: redirecionamento para HTTPS (`api/index.js:14-19`) e HSTS de 1 ano (`api/index.js:32`) no código da API; cabeçalhos das páginas estáticas não coletados em produção; a CSP enfraquecida pela hospedagem é contada em IN-01 | — | Manter; conferir o HSTS das páginas estáticas com `curl -I` |
| **SE-03** · `ALTO` · `TECNICO` — Autorização por papel e isolamento entre clínicas | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: `/api/admin` exige token e papel `admin` (`api/index.js:41`, `src/auth.js:43-50`); as rotas da clínica filtram pelo `clinica_id` do token (`src/routes/clinica.js:13` e `:28`) | — | Manter e cobrir com testes automatizados |
| **SE-04** · `ALTO` · `TECNICO` — Autenticação robusta: segundo fator para quem acessa dados de saúde | `seguranca` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: login por senha bem implementado (`src/auth.js:11-28`), mas sem segundo fator; a falta de limitação de tentativas é contada em AP-03 | Conta de clínica protegida só por senha | MFA para usuários de clínica e de administração |
| **SE-05** · `ALTO` · `TECNICO` — Proteção contra injeção de SQL, XSS e CSRF | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: todas as consultas usam parâmetros (`src/routes/agendamentos.js:31-45` e `:52-58`, `src/routes/clinica.js:9-30`); a confirmação usa `textContent` (`public/js/agendar.js:28`); o token vai no cabeçalho `Authorization`, não em cookie (`src/auth.js:32`) | — | Manter; acrescentar validação de formato (CPF, datas) |
| **SE-06** · `ALTO` · `TECNICO` — Logs da aplicação sem dados pessoais ou com mascaramento | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:29` grava nome, CPF e e-mail do paciente no console, que vira log da Vercel; `src/auth.js:20` grava o e-mail em logins que falham | Dados pessoais legíveis por quem acessa os logs | Registrar só IDs internos; expurgar os logs existentes |
| **SE-07** · `ALTO` · `TECNICO` — Trilha de auditoria de acessos a dados de pacientes | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: nenhum registro de quem consultou ou alterou dados de pacientes (`api/index.js:38-41`, `src/routes/clinica.js:8-33`) | Impossível investigar acesso indevido ou dimensionar um incidente | Registrar usuário, rota, paciente e horário, sem dados pessoais no log |
| **DS-01** · `CRITICO` · `TECNICO` — Segredos do pipeline protegidos e fora dos logs | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: token e IDs da Vercel vêm de secrets do GitHub (`.github/workflows/ci.yml:27-30`), sem eco em log | — | Manter; restringir o deploy ao ambiente protegido da `main` |
| **DS-02** · `ALTO` · `TECNICO` — Varredura de dependências e SAST no CI | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: o pipeline roda só `install`, `lint` e `test` (`.github/workflows/ci.yml:16-18`); não há `npm audit`, configuração do Dependabot nem fluxo de CodeQL no repositório; as configurações de segurança do GitHub não foram vistas | Biblioteca vulnerável chega à produção sem aviso | `npm audit` no CI, Dependabot e SAST |
| **DS-03** · `BAIXO` · `TECNICO` — SBOM gerado e armazenado | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: nenhum SBOM gerado no pipeline (`.github/workflows/ci.yml:9-30`) | Resposta lenta a vulnerabilidades novas | Gerar SBOM CycloneDX a cada build |

### `direitos_titular`

Valem só para os tratamentos em que a AgendaFácil é controladora: contas dos usuários das clínicas e rastreamento para fins próprios.

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **DT-01** · `ALTO` · `DOCUMENTAL` — Canal para exercício de direitos nos tratamentos próprios | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: nenhum canal nem lista de direitos (`docs/lgpd/politica-de-privacidade.md:36`, TODO pendente); o rodapé só oferece um e-mail genérico (`public/index.html:48`) | Usuários das clínicas e visitantes rastreados não conseguem exercer direitos do art. 18 | Publicar canal específico, com prazo de resposta |
| **DT-02** · `MEDIO` · `DOCUMENTAL` — Fluxo de atendimento dos pedidos nos tratamentos próprios, no prazo do art. 19 | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: não há rota para consultar, exportar ou excluir uma conta de usuário (`src/routes/clinica.js:1-55`, `api/index.js:38-41`); nenhum procedimento escrito em `docs/lgpd/` | Pedidos sem prazo, sem registro e sem confirmação de execução | Procedimento simples, com prazo e registro de cada pedido |
| **DT-03** · `ALTO` · `DOCUMENTAL` — Aviso de privacidade dos tratamentos próprios publicado e acessível | `direitos_titular` | `NAO_CONFORME` | `PARCIAL (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: há um rascunho em `docs/lgpd/politica-de-privacidade.md`, mas nenhuma página em `public/`, que é a pasta publicada (`vercel.json:4`), nem rota para `/privacidade`; o link do rodapé e do banner aponta para um endereço inexistente (`public/index.html:49`); produção não consultada | Quem recebe o banner de cookies não tem onde ler sobre o tratamento | Publicar a página e conferir o link em produção |
| **DT-04** · `MEDIO` · `DOCUMENTAL` — Conteúdo do aviso conforme o art. 9º | `direitos_titular` | `PARCIAL` | `PARCIAL (DOCUMENTAL)`, confiança `ALTA`: o rascunho traz identificação, contato e data (`politica-de-privacidade.md:3-9`) e uma menção genérica a cookies (`:28-30`); faltam o tratamento das contas das clínicas, a Meta como destinatária, base legal, retenção, direitos e encarregado; o texto fala aos pacientes como se a AgendaFácil fosse a controladora (`:11-26`); a falta de informação sobre transferência internacional é contada em GV-05 | Transparência insuficiente; consentimento sem informação prévia é nulo (art. 9º, §1º) | Reescrever com `templates/privacy-policy-template.md`, separando os papéis |

### `governanca`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **GV-01** · `ALTO` · `DOCUMENTAL` — Registro das operações de tratamento que realiza, como operadora e como controladora (art. 37) | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: `docs/lgpd/` contém só o rascunho da política; o `README.md:27-29` lista dados, sem finalidade, papel, base, retenção nem compartilhamentos; a fundadora declarou não haver outros documentos | Sem mapa do que é tratado, nada mais se sustenta; com dados sensíveis, `ALTO` | Elaborar o registro completo (a forma simplificada não vale com alto risco) |
| **GV-02** · `ALTO` · `DOCUMENTAL` — Encarregado indicado por ato formal, com contato divulgado | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: nenhum ato de indicação; o próprio rascunho registra a pendência do contato do encarregado (`politica-de-privacidade.md:36`); rodapé sem o contato (`public/index.html:47-51`) | Exigível: a AgendaFácil também é controladora, e a dispensa do pequeno porte não vale com alto risco (Res. CD/ANPD nº 2/2022, art. 3º) | Indicar encarregado (pode ser serviço externo) e divulgar o contato |
| **GV-03** · `ALTO` · `DOCUMENTAL` — RIPD dos tratamentos de alto risco em que é controladora (uso próprio de dados da página de agendamento) | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum RIPD em `docs/lgpd/`; a fundadora declarou não haver outros documentos | Rastreamento que revela busca por atendimento de saúde, sem análise de impacto | Encerrar o tratamento (OP-02) ou elaborar o RIPD (risco aceito até 2026-12-31) |
| **GV-04** · `MEDIO` · `DOCUMENTAL` — Política de retenção dos dados próprios (contas, logs), com prazo por categoria e fundamento no art. 16 | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhuma política de retenção em `docs/lgpd/`; o rascunho da política não fala de prazos | Contas e logs guardados indefinidamente | Definir prazos por categoria |
| **GV-05** · `ALTO` · `DOCUMENTAL` — Transferência internacional com mecanismo do art. 33 e informação ao titular | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `BAIXA`: o fluxo é comprovado no código, pois `public/index.html:13-15` e `public/js/agendar.js:23` enviam dados do navegador do paciente à Meta, nos EUA, sem adequação reconhecida (a mesma evidência de OP-02 e CK-02, reprovada aqui por obrigação distinta, o art. 33); os logs das funções ficam com a Vercel Inc., nos EUA; o mecanismo não está evidenciado, porque os termos desses provedores não foram localizados nem examinados; o rascunho da política não informa a transferência | Dados saem do País sem base demonstrada | Remover o pixel; examinar os termos e incorporar as CPC da Res. CD/ANPD nº 19/2024 onde faltarem |
| **GV-06** · `ALTO` · `DOCUMENTAL` — Deveres gerais de provedor de aplicações: sede e contato no País e canal de denúncia (Dec. nº 8.771/2016, art. 16-A) | `governanca` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: razão social, CNPJ, endereço e contato no rodapé (`public/index.html:48`); não há canal de denúncia permanente | Descumprimento de dever vigente desde 20/07/2026 | Página simples de denúncia, que pode ser a mesma do canal de privacidade |
| **OP-01** · `ALTO` · `DOCUMENTAL` — Contrato ou termo com as clínicas controladoras: objeto, instruções, segurança, suboperadores e devolução ou eliminação (art. 39) | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: a contratação é on-line (`README.md:16`), mas não há termos de uso em `public/` nem contrato em `docs/lgpd/`; a fundadora confirmou que não existe contrato; o rascunho da política apresenta a AgendaFácil como responsável, sem distinguir papéis (`politica-de-privacidade.md:9`) | Operadora de dados de saúde sem instruções documentadas; responsabilidade solidária | Termos de uso com cláusulas de operador |
| **OP-03** · `ALTO` · `DOCUMENTAL` — Suboperadores (Vercel, provedor do banco) informados às clínicas e cobertos por contrato equivalente | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `BAIXA`: nenhum DPA em `docs/lgpd/` (`README.md:22-23` identifica os provedores); os termos padrão aceitos no cadastro não foram reunidos nem examinados; nada informa os suboperadores às clínicas, já que não há contrato (OP-01) | Suboperadores que tratam dados de saúde sem obrigações demonstradas (`ALTO`) | Reunir os DPAs, arquivá-los e listar os suboperadores nos termos com as clínicas |
| **OP-04** · `ALTO` · `DOCUMENTAL` — Processo de incidentes: aviso sem demora às clínicas e, nos dados próprios, comunicação à ANPD e aos titulares em 3 dias úteis | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum plano, runbook ou modelo de aviso no repositório; a fundadora declarou não haver outros documentos | As clínicas não seriam avisadas a tempo de cumprir o prazo da Res. CD/ANPD nº 15/2024 | Adotar `templates/incident-response-template.md`, com o aviso às clínicas |
| **OP-05** · `MEDIO` · `TECNICO` — Apoio às clínicas no atendimento a pedidos dos pacientes (acesso, correção, eliminação, portabilidade) | `governanca` | `PARCIAL` | `PARCIAL (TECNICA)`, confiança `ALTA`: a clínica corrige nome, telefone e e-mail (`src/routes/clinica.js:21-33`); não há rota nem rotina para exportar ou eliminar os dados de um paciente | A clínica depende de pedidos manuais à AgendaFácil para atender o paciente | Rotas autenticadas de exportação e eliminação por paciente |
| **OP-06** · `MEDIO` · `TECNICO` — Devolução ou eliminação dos dados ao fim do contrato e nos prazos instruídos pela clínica (art. 16) | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: o esquema não tem campo de expiração ou exclusão (`db/schema.sql:20-39`); não há rotina de exportação em lote ou de expurgo no código, nem agendamento no `vercel.json` ou no CI; nenhum procedimento escrito | Dados de saúde permanecem depois do fim do contrato; a base só cresce | Rotina de devolução e de expurgo, com registro da execução |

### `infraestrutura`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **IN-01** · `ALTO` · `TECNICO` — A hospedagem não enfraquece os cabeçalhos de segurança do código | `infraestrutura` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `MEDIA`: o código define CSP restritiva (`api/index.js:22-34`), mas as páginas de `public/` são servidas direto pela CDN com a CSP do `vercel.json:12-15` (`default-src * 'unsafe-inline' 'unsafe-eval'`), que libera scripts de qualquer origem e não impede o enquadramento da página por outros sites; respostas de produção não coletadas | A página que coleta CPF e dados de saúde fica sem defesa contra XSS e clickjacking | Igualar a CSP do `vercel.json` à do código e conferir com `curl -I` |
| **IN-02** · `CRITICO` · `TECNICO` — Segredos em variáveis de ambiente, fora do repositório | `infraestrutura` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `MEDIA`: `.env` ignorado (`.gitignore:2-4`); `.env.example` só com marcadores (`.env.example:6` e `:9`); o código lê `process.env` (`src/db.js:4`, `src/auth.js:26` e `:36`); o cofre de variáveis da Vercel não foi visto | — | Manter; separar segredos de produção e de preview no painel |

### `apis_integracoes`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **AP-01** · `ALTO` · `TECNICO` — Tokens JWT com expiração, algoritmo fixo e audiência | `apis_integracoes` | `NAO_CONFORME` | `PARCIAL (TECNICA)`, confiança `ALTA`: a assinatura é verificada, mas `jwt.sign` não define `expiresIn`, `algorithm` nem `audience` (`src/auth.js:24-27`) e `jwt.verify` não restringe algoritmos (`src/auth.js:36`) | Token vazado dá acesso permanente à agenda da clínica | Expiração curta, algoritmo fixo, audiência e revogação |
| **AP-02** · `ALTO` · `TECNICO` — Respostas expõem só os campos necessários | `apis_integracoes` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `ALTA`: `GET /api/agendamentos/:codigo` é público e devolve `SELECT a.*, p.*` (`src/routes/agendamentos.js:51-61`), com CPF, telefone, e-mail, data de nascimento e motivo da consulta; a tela usa só `data_hora` e `nome` (`public/js/agendar.js:25-30`) | Quem tiver o código (link compartilhado, histórico do navegador) lê dados de saúde e CPF | Selecionar só data, horário e primeiro nome |
| **AP-03** · `MEDIO` · `TECNICO` — Limitação de taxa nas APIs | `apis_integracoes` | `NAO_CONFORME` | `AUSENTE (TECNICA)`, confiança `MEDIA`: nenhuma limitação em `/api/login` nem em `POST /api/agendamentos` (`api/index.js:36-41`; nada em `package.json:15-22`); regras do firewall da plataforma não foram vistas | Força bruta no login e agendamentos falsos em massa | `express-rate-limit` nas rotas públicas |
| **AP-04** · `ALTO` · `TECNICO` — Criptografia em trânsito com integrações | `apis_integracoes` | `CONFORME` | `ENCONTRADA (TECNICA)`, confiança `ALTA`: a conexão com o banco exige TLS com verificação de certificado (`src/db.js:5`; `sslmode=require` em `.env.example:6`); front-end e API usam HTTPS (`api/index.js:14-19`) | — | Manter |

### Itens fora do cálculo

| Item | Área | Aplicabilidade | Justificativa ou acesso necessário |
|---|---|---|---|
| **BL-01** — Escolha da base legal e coleta de consentimento para os dados dos pacientes, inclusive o dado de saúde (arts. 7º, 8º e 11) | `bases_legais` | `NAO_APLICAVEL` | Obrigação do controlador. Nesse fluxo a AgendaFácil é operadora, e as clínicas decidem a base legal (em regra, tutela da saúde, art. 11, II, "f"). O uso para finalidade própria é avaliado em OP-02 |
| **BL-03** — Dados de crianças e adolescentes: consentimento parental e verificação de idade (art. 14) | `bases_legais` | `NAO_APLICAVEL` | Obrigação do controlador no fluxo dos pacientes. Além disso, o agendamento recusa menores de 18 anos (`src/routes/agendamentos.js:23-27`) e as clínicas atendem só adultos (`README.md:15`) |
| **DS-04** — Varredura de vulnerabilidades em imagens Docker | `seguranca` | `NAO_APLICAVEL` | Objeto inexistente: não há `Dockerfile` nem arquivo de composição no repositório; o deploy é feito pela Vercel a partir do código (`.github/workflows/ci.yml:26`) |
| **DS-05** — Varredura de infraestrutura como código (Terraform, CloudFormation, Helm) | `seguranca` | `NAO_APLICAVEL` | Objeto inexistente: nenhum arquivo de IaC no repositório. A única configuração de plataforma é o `vercel.json`, avaliado em IN-01 |
| **DS-06** — RBAC e hardening de Kubernetes | `seguranca` | `NAO_APLICAVEL` | Objeto inexistente: nenhum manifesto de orquestração; a aplicação roda em funções da Vercel (`vercel.json:1-7`) |
| **DT-05** — Canal de direitos dos pacientes | `direitos_titular` | `NAO_APLICAVEL` | Obrigação do controlador (clínicas). A AgendaFácil responde pelo apoio a esses pedidos, avaliado em OP-05 |
| **DT-06** — Política de privacidade e avisos de coleta dirigidos aos pacientes, inclusive o aviso sobre o motivo da consulta | `direitos_titular` | `NAO_APLICAVEL` | Obrigação do controlador (clínicas). Recomendação sem efeito no score: oferecer às clínicas um espaço para o aviso delas na página de agendamento |
| **GV-07** — RIPD do tratamento dos dados de saúde dos pacientes | `governanca` | `NAO_APLICAVEL` | Documento do controlador (arts. 5º, XVII e 38). A AgendaFácil deve fornecer às clínicas as informações necessárias, o que entra no contrato (OP-01). O RIPD do uso próprio é avaliado em GV-03 |
| **GV-08** — Comunicação de incidente à ANPD e aos pacientes no fluxo de agendamento | `governanca` | `NAO_APLICAVEL` | Obrigação do controlador (clínicas). O aviso da operadora às clínicas é avaliado em OP-04 |
| **IN-03** — Banco com criptografia em repouso, backups protegidos e acesso restrito | `infraestrutura` | `NAO_VERIFICADO` | Configuração visível só no painel do provedor do Postgres. O repositório mostra apenas a região e o TLS (`.env.example:5-6`, `src/db.js:5`). Acesso necessário: painel do provedor do banco |
| **IN-04** — Registros de acesso guardados por 6 meses, sob sigilo (MCI, art. 15) | `infraestrutura` | `NAO_VERIFICADO` | A retenção e a exportação dos logs são configuradas no painel da Vercel, não no `vercel.json`. O código não mantém guarda própria. Acesso necessário: painel da Vercel |
| **IN-05** — Acesso aos painéis e tokens de deploy com privilégio mínimo e MFA | `infraestrutura` | `NAO_VERIFICADO` | Membros, papéis e MFA só aparecem nos painéis. Acesso necessário: painéis da Vercel, do banco e do GitHub |
| **IN-06** — Logs e analytics nativos da plataforma com retenção e acesso definidos | `infraestrutura` | `NAO_VERIFICADO` | Configuração do painel da Vercel. O código não inclui o script de analytics da plataforma (`public/index.html:1-56`). Acesso necessário: painel da Vercel |
| **IN-07** — Firewall, WAF e monitoramento capazes de detectar acesso indevido | `infraestrutura` | `NAO_VERIFICADO` | Regras e alertas ficam no painel da Vercel. Acesso necessário: painel da Vercel |
| **IN-08** — Armazenamento de objetos (buckets) sem exposição pública | `infraestrutura` | `NAO_APLICAVEL` | Objeto inexistente: nenhuma dependência nem uso de armazenamento de objetos (`package.json:15-25`); o sistema não recebe arquivos |
| **IN-09** — Segmentação de rede e regras de exposição (VPC, security groups) | `infraestrutura` | `NAO_APLICAVEL` | Objeto inexistente: em PaaS sem servidores próprios não há rede gerida pelo cliente (`vercel.json:1-20`) |

---

## 4. Não conformidades

Todos os 30 itens `NAO_CONFORME` ou `PARCIAL` do checklist estão detalhados abaixo, em ordem de severidade. **Nenhum achado teve severidade modulada**, porque há tratamento de alto risco (ver "Natureza e papel do agente de tratamento"). Os prazos seguem `IMEDIATO` (até 7 dias), `30_DIAS`, `90_DIAS` e `180_DIAS`.

### `CRITICO`

#### NC-01 · OP-02 — Operadora usa dados dos pacientes para publicidade própria

- **Problema:** a AgendaFácil trata os dados dos pacientes em nome das clínicas. Mesmo assim, instalou na página de agendamento um pixel de publicidade para as próprias campanhas. O pixel registra a visita à página de uma clínica específica e o evento de agendamento, e associa tudo a um identificador do navegador. Não há instrução nem autorização das clínicas para isso.
- **Severidade:** `CRITICO`. Pelo `legal/legal-bases-engine.md`, o operador que usa os dados para finalidade própria sem base legal é `ALTO`, e `CRITICO` quando há dado sensível. A visita e o agendamento em uma clínica revelam que a pessoa busca atendimento de saúde. O art. 11, §1º, aplica o regime dos dados sensíveis a qualquer tratamento que revele dado sensível e possa causar dano. Na dúvida entre os dois níveis, vale o mais alto (`core/severity-model.md`).
- **Fundamento LGPD:** art. 39 (tratamento segundo as instruções do controlador); art. 5º, VI e VII; art. 11, I e §1º; art. 42, §1º, I.
- **Evidência:** `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`. O uso próprio está no código: `public/index.html:7-15` ("campanhas de aquisição"), `public/js/agendar.js:23` e `README.md:24`. Nenhuma instrução das clínicas documentada. Verificação que elevaria a confiança: captura de rede em produção e configuração do pixel no Gerenciador de Eventos da Meta.
- **Impacto técnico:** dados de navegação dos pacientes saem do controle das clínicas e da AgendaFácil e passam a alimentar perfis de publicidade.
- **Impacto jurídico:** ao decidir essa finalidade, a AgendaFácil deixa de ser só operadora e responde como controladora, sem base legal válida; responde também de forma solidária perante as clínicas.
- **Correção recomendada (esforço P):** remover o pixel da página de agendamento. Publicidade própria só no site institucional, depois do aceite. Se algum uso próprio de dados dos pacientes for mantido, ele precisa de autorização das clínicas no contrato (OP-01), base legal do art. 11 e RIPD (GV-03).
- **Responsável e prazo:** desenvolvedor líder (CTO), com decisão da sócia-fundadora (CEO) · `IMEDIATO`.

### `ALTO`

#### NC-02 · CK-02 — Meta Pixel disparado antes do consentimento

- **Problema:** o pixel é carregado e envia `PageView` no `<head>` da página, antes de o banner aparecer. Quem clica em "Rejeitar" já foi rastreado.
- **Severidade:** `ALTO`. Mapeamento de `appsec/owasp-api.md`: pixels de publicidade de terceiros disparados antes do aceite, sem outra base legal documentada. É uma obrigação distinta da de OP-02: mesmo em uma página institucional, o rastreador não pode disparar antes da escolha.
- **Fundamento LGPD:** art. 7º, I; art. 8º; art. 6º, III (necessidade).
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `public/index.html:8-15`; `consent.js` só roda no fim da página (`public/index.html:53`).
- **Impacto técnico:** cookie `_fbp` gravado e dados enviados à Meta em toda visita.
- **Impacto jurídico:** tratamento sem base legal; consentimento posterior não convalida a coleta anterior.
- **Correção recomendada (esforço P):** carregar qualquer rastreador de forma dinâmica, só depois de "Aceitar" (ver `recomendacoes_tecnicas`).
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-03 · GV-05 — Dados enviados ao exterior sem mecanismo legal demonstrado

- **Problema:** a página de agendamento envia à Meta, nos EUA, identificadores do navegador (cookie `_fbp`, IP, user agent), a URL da clínica e o evento de agendamento. Os logs das funções, que hoje contêm CPF e e-mail (SE-06), ficam com a Vercel Inc., também nos EUA. Os termos desses provedores não foram localizados nem examinados, e nenhum documento informa a transferência.
- **Severidade:** `ALTO`. Os EUA não têm adequação reconhecida pela ANPD. Pelo `legal/international-transfer.md`, o mecanismo **não evidenciado** (termos não examinados) é `ALTO`, com evidência `AUSENTE`, até a verificação. A falta de informação ao titular também é `ALTO`. Se o exame dos termos comprovar que não há CPC nem outro mecanismo, o item passa a `CRITICO` (peso 4).
- **Fundamento LGPD:** arts. 33 a 36; Res. CD/ANPD nº 19/2024 (prazo das CPC encerrado em 23/08/2025); art. 9º, V.
- **Evidência:** `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `BAIXA`. O fluxo está comprovado em `public/index.html:13-15` e `public/js/agendar.js:23`. O mecanismo não está: nenhum contrato, termo ou CPC em `docs/lgpd/`. Verificação que eleva a confiança: examinar os termos da Meta, da Vercel e do provedor do banco.
- **Impacto técnico:** dados ligados a agendamentos de saúde ficam sob controle de terceiros no exterior.
- **Impacto jurídico:** transferência internacional sem base demonstrada, tema prioritário de fiscalização da ANPD no biênio 2026-2027 (Res. CD/ANPD nº 30/2025); sujeita às sanções do art. 52.
- **Correção recomendada (esforço M):**
  1. Remover o pixel da página de agendamento, o que elimina o fluxo para a Meta (OP-02).
  2. Mapear as transferências que restarem (Vercel, provedor do banco, ferramentas futuras).
  3. Examinar os termos padrão aceitos; se incorporarem as CPC, arquivá-los como evidência; se não incorporarem, assiná-las.
  4. Informar a transferência no aviso de privacidade e, para os dados dos pacientes, às clínicas.
- **Responsável e prazo:** CEO, com assessoria jurídica externa · `30_DIAS`.

#### NC-04 · SE-06 — CPF e e-mail gravados nos logs

- **Problema:** cada agendamento grava nome, CPF e e-mail do paciente no console, e cada login com falha grava o e-mail. Na Vercel, o console vira log da plataforma. Exemplo do que aparece hoje: `[agendamento] novo paciente nome=Paciente Exemplo cpf=123.456.789-09 email=paciente@exemplo.example clinica=fisio-exemplo`.
- **Severidade:** `ALTO`. Logs da aplicação com dados pessoais sem mascaramento (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 46; art. 6º, III e VII.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:29`; `src/auth.js:20`.
- **Impacto técnico:** os dados se espalham para um sistema sem controle de acesso fino nem retenção definida.
- **Impacto jurídico:** medida de segurança inadequada, exigível também do operador; agrava qualquer incidente.
- **Correção recomendada (esforço P):** registrar só IDs internos (`paciente_id`, `clinica`); para login, registrar o ID do usuário ou um hash do e-mail; expurgar os logs existentes no painel.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-05 · AP-02 — API de confirmação devolve o cadastro completo do paciente

- **Problema:** a rota pública de confirmação devolve todas as colunas do agendamento e do paciente, incluindo CPF, telefone, e-mail, data de nascimento e motivo da consulta. A tela usa apenas data, horário e nome. Qualquer pessoa com o código (link repassado, histórico do navegador, ferramenta de suporte) obtém tudo.
- **Severidade:** `ALTO`. API com exposição excessiva de dados pessoais (`appsec/owasp-api.md`). Não há exploração confirmada; se houver, a falha se enquadra em "falha explorável com exfiltração" (`CRITICO`).
- **Fundamento LGPD:** art. 6º, III (necessidade); art. 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `src/routes/agendamentos.js:51-61`; uso parcial em `public/js/agendar.js:25-30`.
- **Impacto técnico:** dado de saúde exposto por um endpoint sem autenticação.
- **Impacto jurídico:** potencial incidente com dado sensível, que a AgendaFácil teria de avisar às clínicas.
- **Correção recomendada (esforço P):** selecionar só `a.data_hora` e o primeiro nome; nunca devolver `observacoes`, CPF ou contato em rota pública.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-06 · AP-01 — Token de login sem expiração

- **Problema:** os tokens JWT são emitidos sem validade, algoritmo fixo nem audiência. Um token vazado dá acesso permanente à agenda da clínica, inclusive aos motivos de consulta.
- **Severidade:** `ALTO`. Falha de autenticação sem exploração confirmada (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 46; art. 6º, VII.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/auth.js:24-27` (emissão); `src/auth.js:36` (verificação sem `algorithms`).
- **Impacto técnico:** não há como encerrar sessões nem limitar o uso de um token roubado, a não ser trocando o segredo de todos.
- **Impacto jurídico:** medida de segurança inadequada para dados sensíveis.
- **Correção recomendada (esforço P):** `expiresIn: '8h'`, `algorithm: 'HS256'` e `audience` na emissão; `algorithms` e `audience` na verificação; em seguida, avaliar token de renovação com revogação.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-07 · IN-01 — `vercel.json` anula a CSP definida no código

- **Problema:** o Express define uma CSP restritiva, mas as páginas estáticas, entre elas a que coleta CPF e dados de saúde, são servidas pela CDN da Vercel sem passar pelo Express. O único CSP que recebem é o do `vercel.json`, que permite scripts de qualquer origem, `unsafe-inline` e `unsafe-eval`, e não restringe o enquadramento da página. Para as respostas da API, qual cabeçalho prevalece depende da plataforma.
- **Severidade:** `ALTO`. Hospedagem que remove ou enfraquece cabeçalhos de segurança configurados no código (`cloud/cloud-audit.md`). Pela contagem única, a falha é reprovada só aqui; SE-02 a cita.
- **Fundamento LGPD:** art. 46; art. 6º, VII e VIII.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `MEDIA`: `vercel.json:12-15` contra `api/index.js:22-34`. Respostas de produção não coletadas; `curl -I` na página e na API elevaria a confiança.
- **Impacto técnico:** um XSS ou script de terceiro comprometido conseguiria ler o formulário de agendamento; a página pode ser embutida por outros sites (clickjacking).
- **Impacto jurídico:** medida técnica de segurança neutralizada pela configuração da hospedagem.
- **Correção recomendada (esforço P):** substituir o valor no `vercel.json` pela mesma política do código (`default-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'`), acrescentar `Strict-Transport-Security` e conferir com `curl -I`. A política restritiva só funciona depois de retirar o pixel inline (OP-02).
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-08 · OP-01 — Sem contrato com as clínicas controladoras

- **Problema:** não há termos de uso nem contrato que estabeleça que a clínica é controladora dos dados dos pacientes e que a AgendaFácil trata esses dados por instrução dela. O rascunho da política apresenta a AgendaFácil como responsável por tudo.
- **Severidade:** `ALTO`. Ausência de contrato com o controlador (`legal/legal-bases-engine.md`, seção "Papel do auditado").
- **Fundamento LGPD:** art. 5º, VI e VII; art. 39; art. 42, §1º, I.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `README.md:16`; nenhum termo em `public/` nem em `docs/lgpd/`; declaração da fundadora; `docs/lgpd/politica-de-privacidade.md:9`.
- **Impacto técnico:** não há instruções formais sobre retenção, eliminação, suboperadores e atendimento a pedidos.
- **Impacto jurídico:** sem instruções documentadas, a AgendaFácil pode ser tratada como controladora dos dados de saúde e responde solidariamente por danos.
- **Correção recomendada (esforço M):** termos de uso com cláusulas de operador: objeto, instruções, confidencialidade, segurança, lista de suboperadores, aviso de incidentes, apoio a pedidos de titulares e ao RIPD da clínica, devolução e eliminação ao fim do contrato. Pode partir de `templates/dpa-template.md`.
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-09 · OP-03 — Suboperadores sem contrato demonstrado e não informados às clínicas

- **Problema:** a Vercel processa as requisições com o motivo da consulta, e o provedor do banco armazena esses dados. Não foram localizados contratos de proteção de dados com eles, e as clínicas não são informadas de que eles existem.
- **Severidade:** `ALTO`. Suboperador não informado ou sem contrato é `MEDIO`, e `ALTO` quando trata dado sensível (`legal/legal-bases-engine.md`; mesma regra em `governance/dpo-framework.md` para o provedor de hospedagem).
- **Fundamento LGPD:** art. 39; art. 46.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `BAIXA`: nenhum DPA em `docs/lgpd/`; `README.md:22-23` identifica os provedores; os termos padrão aceitos no cadastro não foram examinados. Verificação que eleva a confiança: reunir os DPAs e os termos da Vercel e do provedor do banco.
- **Impacto técnico:** não há garantia contratual de segurança, aviso de incidentes nem eliminação ao fim do serviço.
- **Impacto jurídico:** a AgendaFácil não consegue demonstrar às clínicas as garantias que deve oferecer como operadora. É uma obrigação distinta do mecanismo de transferência internacional (GV-05), embora os dois costumem estar no mesmo instrumento.
- **Correção recomendada (esforço P):** baixar e arquivar os DPAs que os provedores oferecem, verificar a cobertura de CPC (GV-05) e listar os suboperadores nos termos com as clínicas (OP-01).
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-10 · OP-04 — Sem processo de incidentes

- **Problema:** não há procedimento, responsáveis nem modelo de aviso para incidentes de segurança. Nos dados dos pacientes, a AgendaFácil precisa avisar as clínicas sem demora, para que elas comuniquem a ANPD e os titulares. Nos dados próprios (contas das clínicas), a comunicação é dela.
- **Severidade:** `ALTO`. Ausência de processo de aviso de incidente ao controlador (`legal/legal-bases-engine.md`) e de processo capaz de comunicar em 3 dias úteis (`governance/dpo-framework.md`). O dever não é modulado por porte. As duas faces dependem do mesmo documento e são contadas uma única vez.
- **Fundamento LGPD:** art. 48; art. 39; Res. CD/ANPD nº 15/2024 (comunicação em 3 dias úteis, complementável em 20 dias úteis).
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum plano ou runbook no repositório; declaração da fundadora.
- **Impacto técnico:** reação improvisada, perda de evidências e contenção lenta.
- **Impacto jurídico:** as clínicas perderiam o prazo de comunicação por falta de aviso; incidentes são tema prioritário de fiscalização (Res. CD/ANPD nº 30/2025).
- **Correção recomendada (esforço M):** adotar `templates/incident-response-template.md`, definir quem decide e quem avisa, e fixar no contrato o prazo de aviso às clínicas (por exemplo, 24 horas).
- **Responsável e prazo:** CEO e CTO · `30_DIAS`.

#### NC-11 · SE-07 — Sem trilha de auditoria de acessos a dados de pacientes

- **Problema:** não há registro de qual usuário consultou a agenda ou alterou dados de qual paciente.
- **Severidade:** `ALTO`. Ausência de trilha de auditoria (`cloud/cloud-audit.md`), agravada por envolver dados de saúde.
- **Fundamento LGPD:** art. 46; art. 6º, X; art. 37.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `api/index.js:38-41`; `src/routes/clinica.js:8-33`.
- **Impacto técnico:** acesso indevido por funcionário de clínica ou token vazado passa despercebido.
- **Impacto jurídico:** sem trilha, não se consegue avaliar a extensão de um incidente para avisar as clínicas no prazo.
- **Correção recomendada (esforço M):** middleware que registre usuário, clínica, rota, ID do paciente e horário, sem dados pessoais, em armazenamento com retenção definida.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-12 · DS-02 — Nenhuma varredura de segurança no CI

- **Problema:** o pipeline não verifica vulnerabilidades em dependências nem faz análise estática de segurança.
- **Severidade:** `ALTO`. Ausência total de varredura de segurança (`devsecops/ci-cd-security.md`).
- **Fundamento LGPD:** art. 46; art. 49.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `.github/workflows/ci.yml:16-18`; nenhum `dependabot.yml` nem fluxo de CodeQL no repositório. As configurações de segurança do GitHub não foram vistas.
- **Impacto técnico:** vulnerabilidade conhecida em `express`, `jsonwebtoken` ou `pg` chega à produção sem alerta.
- **Impacto jurídico:** sistemas devem atender a requisitos de segurança desde a concepção (art. 49).
- **Correção recomendada (esforço P):** `npm audit --audit-level=high` no job `build`, Dependabot semanal e CodeQL.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-13 · DT-01 — Sem canal para exercício de direitos nos tratamentos próprios

- **Problema:** nos tratamentos em que é controladora (contas dos usuários das clínicas e rastreamento), a AgendaFácil não informa os direitos nem como exercê-los. O único contato é um e-mail comercial genérico.
- **Severidade:** `ALTO`. Ausência de canal para exercício de direitos (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** arts. 18 e 19; art. 9º, VII.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:36`; `public/index.html:48`.
- **Impacto técnico:** pedidos chegam por canais não monitorados e se perdem.
- **Impacto jurídico:** descumprimento dos arts. 18 e 19. O canal dos pacientes é obrigação das clínicas (DT-05), mas um pedido que chegue à AgendaFácil precisa ser encaminhado a elas (OP-05).
- **Correção recomendada (esforço P):** endereço ou formulário específico de privacidade no aviso e no rodapé, com prazo de resposta (imediato em formato simplificado ou até 15 dias, art. 19).
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-14 · DT-03 — Aviso de privacidade não publicado

- **Problema:** o rodapé e o banner de cookies apontam para `/privacidade`, mas não existe página nesse endereço. O único texto é um rascunho dentro do repositório.
- **Severidade:** `ALTO`. Ausência de política de privacidade (`legal/rights-of-data-subject.md`): para quem acessa o site, ela não existe. O conteúdo do rascunho é avaliado em DT-04.
- **Fundamento LGPD:** art. 9º, caput (acesso facilitado e ostensivo).
- **Evidência:** `PARCIAL (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: `public/index.html:49`; nenhuma página em `public/`, que é a pasta publicada (`vercel.json:4`); rascunho em `docs/lgpd/politica-de-privacidade.md`. Produção não consultada.
- **Impacto técnico:** link quebrado no rodapé.
- **Impacto jurídico:** o consentimento de cookies é pedido sem que o titular tenha acesso às informações do tratamento.
- **Correção recomendada (esforço P):** publicar o aviso revisado (DT-04) em `public/privacidade.html` e testar o link em produção.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-15 · GV-01 — Sem registro das operações de tratamento

- **Problema:** não existe inventário com finalidade, papel, base legal, categorias de titulares, compartilhamentos, retenção e medidas de segurança. O operador também deve manter o registro das operações que realiza.
- **Severidade:** `ALTO`. Ausência de registro com tratamento de dados sensíveis (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 37.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: `docs/lgpd/` contém só o rascunho da política; `README.md:27-29` lista dados, sem os demais elementos; declaração da fundadora.
- **Impacto técnico:** sem mapa de dados, não há como garantir eliminação, responder a pedidos nem dimensionar incidentes.
- **Impacto jurídico:** obrigação legal descumprida. Por haver alto risco, a forma simplificada da Res. CD/ANPD nº 2/2022 não está disponível (art. 3º).
- **Correção recomendada (esforço M):** registro versionado em `docs/lgpd/`, separando o que a AgendaFácil trata como operadora (pacientes) do que trata como controladora (contas, logs, rastreamento).
- **Responsável e prazo:** CEO, com o encarregado · `30_DIAS`.

#### NC-16 · GV-02 — Encarregado não indicado

- **Problema:** não há encarregado indicado nem contato divulgado.
- **Severidade:** `ALTO`. Pelo `governance/dpo-framework.md`, a falta de encarregado quando ele é exigível é `ALTO`. Para o operador a indicação é facultativa, mas a AgendaFácil também é controladora (contas e rastreamento), e a dispensa do pequeno porte não vale para quem faz tratamento de alto risco (Res. CD/ANPD nº 2/2022, art. 3º).
- **Fundamento LGPD:** art. 41; Res. CD/ANPD nº 18/2024.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:36`; `public/index.html:47-51`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** falta o canal formal com titulares e ANPD.
- **Correção recomendada (esforço P):** indicar encarregado por ato escrito, datado e assinado (pode ser pessoa jurídica, como um serviço de DPO externo) e divulgar o contato no site.
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-17 · GV-03 — Sem RIPD para o uso próprio de dados da página de agendamento (risco aceito)

- **Problema:** como controladora do rastreamento para fins próprios, a AgendaFácil faz um tratamento de alto risco (revela busca por atendimento de saúde, em escala relevante) sem relatório de impacto. O RIPD dos dados de saúde inseridos no agendamento é das clínicas (GV-07).
- **Severidade:** `ALTO`. Ausência de RIPD em tratamento de alto risco pelos critérios da Res. CD/ANPD nº 2/2022 (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 38; art. 5º, XVII.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nenhum RIPD em `docs/lgpd/`; declaração da fundadora.
- **Impacto técnico:** os riscos do rastreamento não foram analisados.
- **Impacto jurídico:** se a ANPD solicitar o RIPD, a AgendaFácil não terá como apresentá-lo.
- **Correção recomendada (esforço G):** encerrar o tratamento, removendo o pixel da página de agendamento (OP-02). Encerrado o uso próprio, o item deixa de ser aplicável. Se algum uso próprio for mantido, elaborar o RIPD com `templates/ripd-template.md`.
- **Aceite de risco:**
  - `accepted_by`: Ana Exemplo, sócia-administradora e CEO (pessoa fictícia);
  - `accepted_at`: 2026-10-03;
  - `justification`: o pixel será removido da página de agendamento em até 7 dias (ação 1), o que encerra o tratamento. Elaborar um RIPD, com esforço de mais de uma semana, para um tratamento em extinção não se justifica para uma equipe de 3 pessoas. Se em 90 dias ainda houver qualquer uso próprio de dados da página de agendamento, o RIPD será elaborado;
  - `deadline_suggestion`: `30_DIAS` (mantido);
  - `accepted_deadline`: `90_DIAS`;
  - `review_at`: 2026-12-31.
  - O aceite **não** altera status, severidade nem score: o item segue `NAO_CONFORME`, `ALTO`, com valor 0 e peso 3.
- **Responsável e prazo:** CEO, com o encarregado · `30_DIAS` (adiado pelo aceite para `90_DIAS`).

#### NC-18 · GV-06 — Sem canal de denúncia de provedor de aplicações

- **Problema:** sede e contato estão no rodapé, mas não há canal permanente de denúncia, exigido de todo provedor de aplicações de internet desde 20/07/2026.
- **Severidade:** `ALTO`. O item é `PARCIAL`; a lacuna que resta é a ausência de canal de denúncia permanente, `ALTO` no mapeamento de `legal/plataformas-digitais.md`, aplicado por `governance` mesmo com aquele módulo inativo.
- **Fundamento:** Decreto nº 8.771/2016, art. 16-A, II (redação do Decreto nº 12.975/2026). Correlato LGPD: art. 6º, VI (transparência).
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `public/index.html:48`.
- **Impacto técnico:** nenhum, além da criação de um canal.
- **Impacto jurídico:** descumprimento de dever geral fiscalizado pela ANPD (Decreto nº 8.771/2016, art. 19-A).
- **Correção recomendada (esforço P):** página "Fale conosco sobre privacidade e denúncias" com formulário ou e-mail monitorado, que preveja expressamente a notificação de conteúdo ilícito.
- **Responsável e prazo:** CEO · `30_DIAS`.

### `MEDIO`

#### NC-19 · BL-02 — Base legal dos tratamentos próprios não documentada

- **Problema:** a AgendaFácil é controladora dos dados das contas dos usuários das clínicas, mas nenhum documento diz qual base legal sustenta esse tratamento.
- **Severidade:** `MEDIO`. O item é `PARCIAL`, com `criticality` `ALTO`: a base é plausível (execução de contrato, art. 7º, V) e a lacuna que resta é nomeá-la e comprová-la. A falta do contrato em si é contada em OP-01.
- **Fundamento LGPD:** art. 7º; art. 6º, X.
- **Evidência:** `PARCIAL (TECNICA + DOCUMENTAL)`, confiança `BAIXA`: `README.md:16`; `db/schema.sql:11-18`; nenhum documento nomeia a base.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** base legal não demonstrável numa fiscalização.
- **Correção recomendada (esforço P):** indicar a base de cada tratamento próprio no registro das operações (GV-01) e no aviso de privacidade (DT-04).
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-20 · CK-03 — Revogação que não apaga o identificador da Meta

- **Problema:** o usuário consegue rever a escolha, e a recusa chama `fbq('consent', 'revoke')`, o que interrompe os eventos seguintes. Mas o cookie `_fbp` e o script já carregado permanecem no navegador.
- **Severidade:** `MEDIO`. O item é `PARCIAL`, com `criticality` `ALTO`: o mecanismo de revogação existe, e a lacuna que resta é a limpeza do identificador. O envio do `PageView` antes da escolha é a falha de CK-02 e não é contado de novo aqui.
- **Fundamento LGPD:** art. 8º, §5º; art. 18, IX.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `public/js/consent.js:6-9` e `:26-29`; `public/index.html:50`.
- **Impacto técnico:** o identificador persistente da Meta segue disponível após a revogação.
- **Impacto jurídico:** revogação incompleta.
- **Correção recomendada (esforço P):** na revogação, apagar o cookie `_fbp` e não recarregar o pixel.
- **Responsável e prazo:** CTO · `90_DIAS` (resolvido na prática junto com OP-02, `IMEDIATO`).

#### NC-21 · CK-04 — Escolha de cookies sem prova

- **Problema:** a escolha fica apenas no navegador, sem versão do banner nem categorias.
- **Severidade:** `MEDIO`. Ausência de registro das escolhas (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 8º, §2º.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `public/js/consent.js:12`.
- **Impacto técnico:** limpar o navegador apaga a prova.
- **Impacto jurídico:** o ônus de provar o consentimento é do controlador.
- **Correção recomendada (esforço M):** registrar no servidor um identificador aleatório, data, versão do banner e categorias aceitas.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-22 · CK-05 — Consentimento de cookies genérico

- **Problema:** o banner oferece só "Aceitar" ou "Rejeitar" tudo e diz apenas "melhorar sua experiência", sem mencionar publicidade nem a Meta.
- **Severidade:** `MEDIO`. Consentimento pouco granular (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 8º, §4º; art. 9º.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `public/index.html:42`.
- **Impacto técnico:** não há como aceitar medição e recusar publicidade.
- **Impacto jurídico:** autorização genérica é nula (art. 8º, §4º).
- **Correção recomendada (esforço M):** categorias separadas, sem pré-marcação, com nome dos terceiros e link para a política de cookies (`templates/cookie-policy-template.md`).
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-23 · SE-04 — Login sem segundo fator

- **Problema:** usuários de clínica acessam motivos de consulta apenas com senha.
- **Severidade:** `MEDIO`. O item é `PARCIAL`, com `criticality` `ALTO`: a senha é bem armazenada e verificada, e a lacuna que resta é o segundo fator (ausência parcial de hardening, `appsec/owasp-api.md`). A falta de limitação de tentativas é contada em AP-03.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/auth.js:11-28`.
- **Impacto técnico:** senhas fracas ou reutilizadas dão acesso à agenda.
- **Impacto jurídico:** medida de segurança aquém do adequado para dado sensível.
- **Correção recomendada (esforço M):** MFA por aplicativo autenticador para usuários de clínica e de administração.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-24 · DT-02 — Sem fluxo para atender pedidos nos tratamentos próprios

- **Problema:** não há procedimento nem recurso do sistema para consultar, exportar ou excluir os dados de uma conta de usuário de clínica, com prazo e registro.
- **Severidade:** `MEDIO`. Inexistência de fluxo de exclusão e portabilidade (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 18, II, V e VI; art. 19.
- **Evidência:** `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: nenhuma rota de conta em `src/routes/clinica.js:1-55` e `api/index.js:38-41`; nenhum procedimento em `docs/lgpd/`.
- **Impacto técnico:** pedidos exigem alterações manuais no banco, sem registro.
- **Impacto jurídico:** risco de descumprir o prazo do art. 19.
- **Correção recomendada (esforço P):** procedimento de uma página (quem recebe, como executa, prazo, registro), suficiente para o volume atual.
- **Responsável e prazo:** CEO · `90_DIAS`.

#### NC-25 · DT-04 — Aviso de privacidade incompleto e com papéis trocados

- **Problema:** o rascunho identifica a empresa e menciona cookies de forma genérica. Faltam o tratamento das contas das clínicas, a Meta como destinatária, base legal, retenção, direitos e encarregado. Além disso, o texto fala aos pacientes como se a AgendaFácil fosse a controladora dos dados do agendamento.
- **Severidade:** `MEDIO`. Política incompleta frente ao art. 9º (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 9º; art. 6º, I (finalidade específica).
- **Evidência:** `PARCIAL (DOCUMENTAL)`, confiança `ALTA`: `docs/lgpd/politica-de-privacidade.md:3-36`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** consentimento obtido sem informação prévia transparente é nulo (art. 9º, §1º); assumir por escrito o papel de controladora dos dados dos pacientes amplia a responsabilidade da AgendaFácil.
- **Correção recomendada (esforço M):** reescrever com `templates/privacy-policy-template.md`: tratar das contas e dos cookies e explicar que, nos agendamentos, a controladora é a clínica.
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-26 · GV-04 — Sem política de retenção dos dados próprios

- **Problema:** não há prazo definido para manter contas de usuários das clínicas e logs, nem fundamento do art. 16 para o que é conservado. Os prazos dos dados dos pacientes são definidos pelas clínicas e entram no contrato (OP-01) e na rotina de expurgo (OP-06).
- **Severidade:** `MEDIO`. Retenção sem prazo definido (`governance/dpo-framework.md`).
- **Fundamento LGPD:** arts. 15 e 16.
- **Evidência:** `AUSENTE (DOCUMENTAL)`, confiança `MEDIA`: nada em `docs/lgpd/`; declaração da fundadora.
- **Impacto técnico:** acúmulo indefinido de contas inativas e de logs.
- **Impacto jurídico:** conservação além da finalidade viola os arts. 15 e 16.
- **Correção recomendada (esforço P):** prazos por categoria. Exemplos:
  - contas: até o fim do contrato, mais o prazo legal;
  - logs de aplicação: 90 dias;
  - registros de acesso: 6 meses (MCI, art. 15; ver IN-04).
- **Responsável e prazo:** CEO · `90_DIAS`.

#### NC-27 · OP-05 — Apoio incompleto às clínicas nos pedidos dos pacientes

- **Problema:** a clínica consegue corrigir dados cadastrais, mas não há como gerar cópia, exportar ou eliminar o cadastro de um paciente.
- **Severidade:** `MEDIO`. O módulo não traz regra própria para o apoio ao controlador; por analogia com a inexistência de fluxo de exclusão e portabilidade (`legal/rights-of-data-subject.md`), `MEDIO`.
- **Fundamento LGPD:** art. 39; art. 18, II, V e VI.
- **Evidência:** `PARCIAL (TECNICA)`, confiança `ALTA`: `src/routes/clinica.js:21-33`.
- **Impacto técnico:** cada pedido exige uma consulta manual no banco pela equipe da AgendaFácil.
- **Impacto jurídico:** a clínica pode perder o prazo do art. 19 por depender da operadora.
- **Correção recomendada (esforço M):** rotas autenticadas para a clínica exportar (JSON ou CSV) e eliminar ou anonimizar um paciente, com registro da execução.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-28 · OP-06 — Sem devolução ou eliminação dos dados ao fim do contrato

- **Problema:** o sistema não tem rotina para devolver ou eliminar os dados de uma clínica que encerra o contrato, nem para expurgar registros nos prazos que a clínica definir.
- **Severidade:** `MEDIO`. O módulo não traz regra própria para este item; por analogia com a retenção sem prazo definido (`governance/dpo-framework.md`), `MEDIO`.
- **Fundamento LGPD:** arts. 15 e 16; art. 39.
- **Evidência:** `AUSENTE (TECNICA + DOCUMENTAL)`, confiança `MEDIA`: `db/schema.sql:20-39`; nenhuma rotina no código nem agendamento no `vercel.json` ou no CI; nenhum procedimento escrito.
- **Impacto técnico:** a base só cresce, e com ela o impacto de um vazamento.
- **Impacto jurídico:** conservação de dados de saúde sem instrução do controlador.
- **Correção recomendada (esforço M):** exportação em lote por clínica e job agendado que elimine ou anonimize registros vencidos, gravando o que foi feito e alcançando os backups conforme a política do provedor.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-29 · AP-03 — APIs sem limitação de taxa

- **Problema:** login e agendamento público aceitam requisições ilimitadas, o que também deixa o login sem proteção contra força bruta.
- **Severidade:** `MEDIO`. Ausência parcial de hardening (`appsec/owasp-api.md`). Item mais específico para essa falha; SE-04 o cita.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `MEDIA`: `api/index.js:36-41`; `package.json:15-22`. As regras do firewall da plataforma não foram vistas.
- **Impacto técnico:** força bruta de senhas e criação massiva de agendamentos falsos.
- **Impacto jurídico:** medida de segurança insuficiente.
- **Correção recomendada (esforço P):** `express-rate-limit` em `/api/login` e `POST /api/agendamentos`, ou o firewall da plataforma.
- **Responsável e prazo:** CTO · `90_DIAS`.

### `BAIXO`

#### NC-30 · DS-03 — Sem SBOM

- **Problema:** não há inventário das dependências gerado a cada build.
- **Severidade:** `BAIXO`. Melhoria com baixo risco imediato.
- **Fundamento LGPD:** art. 46; art. 6º, X.
- **Evidência:** `AUSENTE (TECNICA)`, confiança `ALTA`: `.github/workflows/ci.yml:9-30`.
- **Impacto técnico:** diante de uma vulnerabilidade nova, leva mais tempo saber se o projeto é afetado.
- **Impacto jurídico:** baixo; reforça a prestação de contas.
- **Correção recomendada (esforço P):** gerar SBOM CycloneDX no CI e guardá-lo como artefato.
- **Responsável e prazo:** CTO · `180_DIAS`.

---

## 5. Itens obrigatórios ausentes

Requisitos sem nenhuma evidência (`AUSENTE`) que a LGPD, a ANPD ou o MCI exigem de forma direta da AgendaFácil:

| Requisito | Norma | Item |
|---|---|---|
| Contrato com as clínicas controladoras | LGPD, art. 39 | OP-01 |
| Contratos com os suboperadores e sua indicação às clínicas | LGPD, art. 39 | OP-03 |
| Tratamento limitado às instruções do controlador | LGPD, art. 39 | OP-02 |
| Processo de incidentes, com aviso às clínicas | LGPD, arts. 39 e 48; Res. CD/ANPD nº 15/2024 | OP-04 |
| Rotina de devolução ou eliminação ao fim do contrato | LGPD, arts. 15 e 16 | OP-06 |
| Registro das operações de tratamento (forma completa) | LGPD, art. 37; Res. CD/ANPD nº 2/2022, art. 3º | GV-01 |
| Encarregado indicado e contato divulgado | LGPD, art. 41; Res. CD/ANPD nº 18/2024 | GV-02 |
| RIPD do tratamento de alto risco próprio (risco aceito até 2026-12-31) | LGPD, arts. 5º, XVII e 38 | GV-03 |
| Política de retenção dos dados próprios | LGPD, arts. 15 e 16 | GV-04 |
| Mecanismo de transferência internacional (não evidenciado) e informação ao titular | LGPD, arts. 33 e 9º; Res. CD/ANPD nº 19/2024 | GV-05 |
| Canal de exercício de direitos e fluxo de atendimento nos tratamentos próprios | LGPD, arts. 18 e 19 | DT-01, DT-02 |
| Aviso de privacidade publicado | LGPD, art. 9º | DT-03 |
| Canal de denúncia de provedor de aplicações | Decreto nº 8.771/2016, art. 16-A, II | GV-06 |
| Bloqueio de rastreamento antes do consentimento | LGPD, arts. 7º, I e 8º | CK-02 |
| Mascaramento de dados pessoais em logs | LGPD, art. 46 | SE-06 |

A guarda dos registros de acesso por 6 meses (MCI, art. 15) não está nesta lista porque não pôde ser verificada (IN-04).

---

## 6. Riscos identificados

### Técnicos

- Exposição de CPF, contato e motivo da consulta pela API pública de confirmação (AP-02).
- Tokens de login sem validade: um vazamento dá acesso permanente (AP-01).
- Dados pessoais espalhados nos logs da plataforma (SE-06).
- Página de coleta sem CSP efetiva, vulnerável a XSS e clickjacking (IN-01).
- Dependências vulneráveis sem detecção (DS-02, DS-03).
- Acesso indevido sem rastro (SE-07); contas protegidas só por senha e sem limite de tentativas (SE-04, AP-03).
- Cinco controles de infraestrutura ainda não verificados (IN-03 a IN-07): a proteção real do banco, dos painéis e dos logs é desconhecida.

### Jurídicos

- Uso de dados dos pacientes para publicidade própria: a AgendaFácil sai do papel de operadora, passa a responder como controladora sem base legal e responde solidariamente perante as clínicas, art. 42, §1º, I (OP-02).
- Operadora de dados de saúde sem contrato com os controladores nem com os suboperadores (OP-01, OP-03).
- Transferência internacional sem mecanismo do art. 33 demonstrado, tema prioritário de fiscalização. Pode subir a `CRITICO` se o exame dos termos comprovar ausência de CPC (GV-05).
- Rastreamento sem consentimento válido (CK-02, CK-03, CK-05).
- Obrigações documentais básicas ausentes, agravadas pela perda das dispensas do pequeno porte: registro completo, encarregado, processo de incidentes, retenção, canal de direitos, aviso de privacidade e canal de denúncia (seção 5).
- Exposição às sanções do art. 52 da LGPD (advertência; multa de até 2% do faturamento, limitada a R$ 50 milhões por infração; publicização; bloqueio e eliminação dos dados), com dosimetria pela Res. CD/ANPD nº 4/2023. Some-se a isso o MCI (art. 12) para os deveres de provedor de aplicações.

### Operacionais

- Equipe de 3 pessoas sem processo de incidentes: um vazamento pararia o produto e deixaria as clínicas sem aviso dentro do prazo (OP-04).
- Pedidos de pacientes atendidos à mão, a pedido das clínicas, sem rotina de exportação ou eliminação (OP-05, OP-06).
- Base de dados crescendo sem limite (OP-06, GV-04).
- Clínicas mais estruturadas devem exigir contrato de operador e evidências de segurança na contratação; sem eles, vendas travam (OP-01, OP-03).

### Reputacionais

- Pixel de publicidade em página de agendamento de saúde é o tipo de caso que costuma virar notícia e afastar clínicas e pacientes (OP-02, CK-02, GV-05).
- Um vazamento de motivos de consulta atinge a confiança das clínicas, que respondem perante seus pacientes e conselhos profissionais (AP-02, SE-06).

### Riscos aceitos

| Item | Severidade | Aceito por | Data do aceite | Justificativa | Prazo sugerido | Prazo aceito | Revisão |
|---|---|---|---|---|---|---|---|
| GV-03 — RIPD do uso próprio de dados da página de agendamento | `ALTO` | Ana Exemplo, sócia-administradora e CEO (fictícia) | 2026-10-03 | O pixel será removido em até 7 dias, o que encerra o tratamento; não se justifica um RIPD para um tratamento em extinção. Se em 90 dias ainda houver uso próprio, o RIPD será elaborado | `30_DIAS` | `90_DIAS` | 2026-12-31 |

O aceite fica registrado para prestação de contas. O item continua pontuando como `NAO_CONFORME` e deve ser reavaliado na data de revisão.

---

## 7. Plano de adequação

Esforço: `P` até 1 dia; `M` até 1 semana; `G` mais de 1 semana. `IMEDIATO` significa até 7 dias. `IMEDIATO` e `30_DIAS` ficam no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo.

### Curto prazo (0-30 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 1 | Remover o Meta Pixel da página de agendamento; se mantido no site institucional, carregar só após o aceite e apagar `_fbp` na revogação | OP-02, CK-02, CK-03, GV-05 | CTO | P | `IMEDIATO` |
| 2 | Retirar CPF, nome e e-mail dos logs e expurgar os logs existentes | SE-06 | CTO | P | `IMEDIATO` |
| 3 | Reduzir a resposta da confirmação a data, horário e primeiro nome | AP-02 | CTO | P | `IMEDIATO` |
| 4 | Expiração, algoritmo e audiência no JWT | AP-01 | CTO | P | `IMEDIATO` |
| 5 | Corrigir a CSP e acrescentar HSTS no `vercel.json`; conferir com `curl -I` | IN-01 | CTO | P | `IMEDIATO` |
| 6 | Fazer as verificações pendentes nos painéis da Vercel, do banco e do GitHub e guardar as evidências | IN-03 a IN-07, DS-02, AP-03 | CTO | P | `30_DIAS` |
| 7 | Termos de uso com cláusulas de operador para as clínicas, com a lista de suboperadores | OP-01, OP-03 | CEO + jurídico | M | `30_DIAS` |
| 8 | Reunir e arquivar os DPAs da Vercel e do provedor do banco; examinar os termos e incorporar CPC onde faltarem | OP-03, GV-05 | CEO + jurídico | M | `30_DIAS` |
| 9 | Processo de incidentes, com prazo de aviso às clínicas | OP-04 | CEO + CTO | M | `30_DIAS` |
| 10 | Indicar encarregado (interno ou serviço externo) | GV-02 | CEO | P | `30_DIAS` |
| 11 | Reescrever e publicar o aviso de privacidade dos tratamentos próprios, com canal de direitos e canal de denúncia | DT-01, DT-03, DT-04, BL-02, GV-06 | CEO + jurídico; publicação pelo CTO | M | `30_DIAS` |
| 12 | Registro das operações de tratamento, na forma completa, separando os papéis | GV-01, BL-02 | CEO + encarregado | M | `30_DIAS` |
| 13 | `npm audit`, Dependabot e SAST no CI | DS-02 | CTO | P | `30_DIAS` |
| 14 | Trilha de auditoria de acessos a dados de pacientes | SE-07 | CTO | M | `30_DIAS` |

### Médio prazo (30-90 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 15 | Confirmar que não resta uso próprio de dados da página de agendamento; se restar, elaborar o RIPD (prazo sugerido `30_DIAS`, adiado pelo aceite de risco) | GV-03 | CEO + encarregado | P (G, se o RIPD for necessário) | `90_DIAS` |
| 16 | Rotas de exportação e eliminação por paciente, para uso das clínicas | OP-05 | CTO | M | `90_DIAS` |
| 17 | Devolução em lote e expurgo automático conforme os prazos das clínicas | OP-06 | CTO | M | `90_DIAS` |
| 18 | Política de retenção dos dados próprios e procedimento de atendimento a pedidos | GV-04, DT-02 | CEO | P | `90_DIAS` |
| 19 | Banner com categorias e registro das escolhas no servidor | CK-04, CK-05 | CTO | M | `90_DIAS` |
| 20 | MFA e limitação de tentativas no login e nas rotas públicas | SE-04, AP-03 | CTO | M | `90_DIAS` |
| 21 | Corrigir o que as verificações pendentes revelarem (por exemplo, exportar os registros de acesso para guarda de 6 meses) | IN-03 a IN-07 | CTO | M | `90_DIAS` |

### Longo prazo (90-180 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 22 | Gerar SBOM a cada build | DS-03 | CTO | P | `180_DIAS` |
| 23 | Revisar o aceite de risco do RIPD e repetir esta auditoria (`/lgpd-saas`), agora com acesso aos painéis, para medir a evolução | GV-03 e todos | CEO + encarregado | P | `180_DIAS` |
| 24 | Revisão semestral do aviso, dos contratos e do registro; treinamento básico de privacidade para a equipe; orientação às clínicas sobre o aviso delas na página de agendamento | DT-04, GV-01, OP-01 | Encarregado | M | `180_DIAS` |

---

## 8. Recomendações técnicas

**Logs sem dados pessoais** (`src/routes/agendamentos.js:29`, `src/auth.js:20`):

```js
console.log(`[agendamento] criado paciente_id=${paciente.rows[0].id} clinica=${clinica}`);
console.warn('[login] falha de autenticação', { usuarioEncontrado: Boolean(usuario) });
```

**JWT com validade, algoritmo e audiência** (`src/auth.js:24-27` e `:36`):

```js
const OPCOES = { algorithm: 'HS256', expiresIn: '8h', audience: 'agendafacil-painel' };
const token = jwt.sign({ sub: usuario.id, clinica: usuario.clinica_id, papel: usuario.papel },
  process.env.JWT_SECRET, OPCOES);

req.usuario = jwt.verify(token, process.env.JWT_SECRET, {
  algorithms: ['HS256'], audience: 'agendafacil-painel',
});
```

**Confirmação com o mínimo necessário** (`src/routes/agendamentos.js:53`):

```sql
SELECT a.data_hora, split_part(p.nome, ' ', 1) AS primeiro_nome
  FROM agendamentos a JOIN pacientes p ON p.id = a.paciente_id
 WHERE a.codigo = $1
```

**Pixel fora da página de agendamento.** Remover o bloco `public/index.html:7-16` e a chamada de `public/js/agendar.js:23`. Em páginas institucionais, carregar o script a partir de `aplicar('aceito')` em `consent.js`, por um arquivo próprio (não inline), para manter a CSP restritiva. Na revogação, apagar o cookie `_fbp` (`document.cookie = '_fbp=; Max-Age=0; path=/'`, com o domínio usado pelo pixel).

**CSP coerente entre código e hospedagem** (`vercel.json:12-15`):

```json
{ "key": "Content-Security-Policy",
  "value": "default-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'" },
{ "key": "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains" }
```

Validar em produção: `curl -sI https://<domínio>/ | grep -i -E 'content-security|strict-transport'` e o mesmo para `/api/agendamentos/<código-de-teste>`.

**Varreduras no CI** (`.github/workflows/ci.yml`, job `build`):

```yaml
      - run: npm audit --audit-level=high
      - run: npx @cyclonedx/cyclonedx-npm --output-file sbom.json
```

Acrescentar `.github/dependabot.yml` (ecossistema `npm`, frequência semanal) e, se possível, CodeQL.

**Limitação de taxa:** `express-rate-limit` com janela de 15 minutos em `/api/login` (ex.: 10 tentativas) e em `POST /api/agendamentos` (ex.: 20 por IP).

**Trilha de auditoria:** middleware nas rotas `/api/clinica` e `/api/admin` que registre `usuario`, `clinica`, `metodo`, `rota`, `paciente_id` e horário em tabela própria, com retenção definida na política (GV-04).

**Apoio às clínicas e fim de contrato:** rotas `GET /api/clinica/pacientes/:id/exportar` e `DELETE /api/clinica/pacientes/:id`, restritas à clínica do token; rotina administrativa de exportação em lote por clínica; job agendado que execute, conforme os prazos instruídos pelas clínicas, `DELETE` ou anonimização (`nome = 'removido'`, `cpf = NULL`, `observacoes = NULL`) e grave quantos registros foram afetados.

**Aviso da clínica na página de agendamento:** campo configurável por clínica para o aviso de privacidade dela, exibido junto ao formulário e ao campo "Motivo da consulta". A obrigação é da clínica (DT-06); oferecer o espaço é uma boa prática da operadora.

**Em monitoramento (norma não vigente, não gera não conformidade):** a revisão da Res. CD/ANPD nº 1/2021 (fiscalização e processo sancionador) está em consulta pública até 26/10/2026. Até a publicação da norma final, a Res. CD/ANPD nº 1/2021 segue vigente e é a referência de risco sancionatório deste relatório.

---

## Glossário

- **ANPD:** Agência Nacional de Proteção de Dados, que regula e fiscaliza a LGPD.
- **Agente de pequeno porte:** microempresa, empresa de pequeno porte, startup e equivalentes, com regras simplificadas pela Res. CD/ANPD nº 2/2022, salvo nas exclusões da própria resolução, como o tratamento de alto risco.
- **Tratamento de alto risco:** tratamento em larga escala ou com impacto significativo para os titulares, combinado com fatores como dados sensíveis; impede as simplificações do pequeno porte.
- **Controlador:** quem decide por que e como os dados são tratados e responde por base legal, transparência, direitos e comunicação de incidentes (aqui, a clínica, para os dados dos pacientes; a AgendaFácil, para as contas das clínicas e para o rastreamento que instalou).
- **Operador:** quem trata dados em nome do controlador e segundo as instruções dele (aqui, a AgendaFácil, para os dados dos pacientes).
- **Suboperador:** fornecedor contratado pelo operador para tratar os mesmos dados (aqui, a Vercel e o provedor do banco).
- **Finalidade própria:** uso que o operador faz dos dados por decisão sua, fora das instruções do controlador; nesse uso ele passa a ser controlador.
- **Dado pessoal sensível:** dado sobre saúde, origem racial, religião, vida sexual, biometria e outros do art. 5º, II, com regras mais rígidas.
- **Base legal:** hipótese da lei que autoriza um tratamento (arts. 7º e 11).
- **Encarregado (DPO):** pessoa ou empresa que faz a ponte entre a organização, os titulares e a ANPD.
- **Registro das operações de tratamento:** inventário do que é tratado, para quê, com qual base, por quanto tempo e com quem é compartilhado (art. 37).
- **RIPD:** relatório de impacto à proteção de dados, documento do controlador que analisa riscos e salvaguardas de um tratamento.
- **DPA (contrato de operador):** contrato que fixa as obrigações de proteção de dados de quem trata dados em nome de outro.
- **CPC (cláusulas-padrão contratuais):** cláusulas aprovadas pela ANPD que autorizam enviar dados a países sem adequação reconhecida.
- **Transferência internacional:** envio ou acesso a dados pessoais a partir de outro país.
- **Mecanismo não evidenciado:** contrato ou termos não localizados ou não examinados; diferente de mecanismo comprovadamente ausente, que é mais grave.
- **Aplicabilidade:** situação de cada item do checklist: aplicável (avaliado e pontuado), não aplicável ou não verificado.
- **Não aplicável (`NAO_APLICAVEL`):** item cujo objeto não existe no projeto ou cuja obrigação é de outro agente; também vale para uma área inteira do score (aqui, IA). Fica fora do cálculo.
- **Não verificado (`NAO_VERIFICADO`):** controle técnico que só pode ser conferido na produção ou no painel de um provedor, a que a auditoria não teve acesso; fica fora do cálculo e vira verificação pendente.
- **Cobertura:** parcela dos itens verificáveis que a auditoria conseguiu avaliar; abaixo de 80%, o score é parcial.
- **Confiança da evidência:** quão direta e completa é a prova de um item (alta, média ou baixa); não muda o score.
- **Contagem única:** regra pela qual uma mesma falha reprova um só item, o mais específico; outros itens só a repetem se forem uma obrigação legal diferente.
- **Aceite de risco:** decisão registrada do controlador de adiar ou não corrigir um item; não muda o score.
- **Meta Pixel:** script da Meta que registra visitas e eventos para campanhas de publicidade.
- **Banner de cookies:** aviso que pede a escolha do visitante sobre cookies e rastreadores não essenciais.
- **CSP:** cabeçalho que diz ao navegador de onde a página pode carregar scripts e outros recursos.
- **HSTS:** cabeçalho que obriga o navegador a usar sempre HTTPS.
- **JWT:** token assinado que identifica o usuário logado em cada chamada à API.
- **RBAC:** controle de acesso por papel (ex.: `admin`, `clinica`).
- **bcrypt:** algoritmo próprio para guardar senhas de forma irreversível.
- **Exposição excessiva de dados:** API que devolve mais campos do que a tela precisa.
- **Mascaramento:** ocultar parte de um dado (ex.: `***.456.***-**`) antes de gravá-lo ou exibi-lo.
- **Trilha de auditoria:** registro de quem acessou ou alterou o quê, e quando.
- **Limitação de taxa (rate limiting):** limite de requisições por período, contra abuso e força bruta.
- **MFA:** autenticação com mais de um fator (senha e código do celular, por exemplo).
- **Varredura de dependências:** verificação automática de vulnerabilidades conhecidas nas bibliotecas usadas.
- **SAST:** análise automática do código-fonte em busca de falhas de segurança.
- **SBOM:** lista de todos os componentes de software de uma versão.
- **MCI:** Marco Civil da Internet (Lei nº 12.965/2014).
- **Registros de acesso a aplicações:** data, hora, IP e porta lógica de cada acesso, que o provedor guarda por 6 meses (MCI, art. 15).
- **PaaS:** plataforma que hospeda e executa a aplicação sem que a empresa administre servidores (aqui, a Vercel).
- **`score_tecnico` e `score_documental`:** subtotais informativos do score, só com itens de código e infraestrutura ou só com itens de documentos e processos.

---

> Este relatório foi gerado com apoio de IA pelo LGPD Enterprise Auditor, a partir das evidências disponíveis no momento da análise. Ele apoia, mas não substitui, a avaliação do encarregado (DPO) e a assessoria jurídica especializada. As conclusões dependem da completude e da atualidade das evidências fornecidas.
