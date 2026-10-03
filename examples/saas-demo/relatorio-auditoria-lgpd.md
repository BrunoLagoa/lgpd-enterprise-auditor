CONFIDENCIAL — uso interno

> **Exemplo público com dados fictícios.** Este relatório foi produzido sobre o projeto fictício e intencionalmente falho de `examples/saas-demo/` para demonstrar o LGPD Enterprise Auditor. Empresa, pessoas, CNPJ, domínios e dados são inventados. Relatórios reais descrevem falhas que podem estar abertas: são confidenciais, não devem ser versionados em repositório público e seguem a convenção de nome `auditoria-lgpd-AAAA-MM-<cenario>.md` de `core/reporting-engine.md`. Este arquivo foge das duas regras só por ser um exemplo público.

# Relatório de auditoria LGPD — AgendaFácil

| Campo | Valor |
|---|---|
| Projeto auditado | `examples/saas-demo/` — AgendaFácil (fictício) |
| Data da análise | 2026-10-02 |
| Comando | `/lgpd-saas` |
| Cenário | `saas_web` |
| Framework | LGPD Enterprise Auditor 1.2.0, base canônica `.agents/lgpd-enterprise-auditor/` |
| Método | leitura estática dos arquivos do repositório; sem acesso ao ambiente de produção, ao painel da Vercel, ao banco de dados nem a contratos fora do repositório |

## Contexto e escopo

### O que foi inferido dos arquivos do projeto

Antes de qualquer pergunta, foram lidos `README.md`, `docs/`, `package.json`, `vercel.json`, `.env.example`, `.github/workflows/ci.yml`, `db/schema.sql` e o código de `api/`, `src/` e `public/`.

| Entrada do roteador | Contexto inferido | Fonte |
|---|---|---|
| Natureza do agente | Pessoa jurídica com fins econômicos; microempresa do Simples Nacional, 3 sócios | `README.md:13-14` |
| Stack | Node.js 20 + Express 5, JWT; front-end estático | `README.md:20-21`, `package.json:15-22` |
| Hospedagem e banco | Vercel (funções em `gru1`, CDN para estáticos); Postgres gerenciado em `sa-east-1` | `vercel.json:3-4`, `.env.example:5-6`, `README.md:22-23` |
| Integrações | Meta Pixel na página pública de agendamento | `public/index.html:7-15`, `README.md:24` |
| IA/LLM | Nenhuma: sem SDK de IA nas dependências e nenhum fluxo de IA declarado | `package.json:15-25`, `README.md:18-25` |
| DevSecOps | GitHub Actions com lint, testes e deploy; sem varreduras de segurança | `.github/workflows/ci.yml` |
| Faixa etária do público | Pacientes adultos; o agendamento bloqueia menores de 18 anos no servidor | `README.md:15`, `src/routes/agendamentos.js:23-27` |
| Dados tratados | Nome, CPF, telefone, e-mail, data de nascimento e motivo da consulta (texto livre) dos pacientes; e-mail e hash de senha dos usuários das clínicas | `db/schema.sql:11-39`, `README.md:29` |

Confirmações pedidas ao fim do levantamento (respostas simuladas para este exemplo): a fundadora confirmou o porte e a ausência de IA, informou que não há contratos de proteção de dados assinados com clínicas ou provedores e que os termos padrão aceitos no cadastro da Vercel, do banco e da Meta não foram reunidos para análise.

### Natureza do agente de tratamento

- **Pessoa jurídica com fins econômicos**, portanto sujeita à LGPD (a exclusão do art. 4º, I, não se aplica).
- **Agente de tratamento de pequeno porte** (microempresa, Res. CD/ANPD nº 2/2022).
- **Papéis:** para os dados dos pacientes, a AgendaFácil atua, em regra, como **operadora** das clínicas, que são as controladoras (art. 5º, VI e VII). Para os dados do próprio site, do Meta Pixel e dos usuários das clínicas, atua como **controladora**. Hoje nenhum documento registra essa divisão (ver GV-07).
- **Há tratamento de alto risco.** O motivo da consulta (`db/schema.sql:37`, `public/index.html:35`) é **dado pessoal sensível referente à saúde** (art. 5º, II). Pelos critérios da Res. CD/ANPD nº 2/2022 (art. 4º), o uso de dados sensíveis é um critério específico de alto risco. O critério geral também está presente: a exposição de dados de saúde de cerca de 25 mil pacientes pode afetar significativamente seus interesses e direitos fundamentais (discriminação e dano moral, por exemplo).

**Consequências:**

1. **Nenhuma severidade foi modulada.** O `core/severity-model.md` só permite reduzir a severidade em um nível quando as três condições são verdadeiras ao mesmo tempo: pequeno porte, **ausência** de tratamento de alto risco e ausência de exposição explorável confirmada. A segunda condição falha, então todas as severidades e `criticality` deste relatório são as originais.
2. **As dispensas do pequeno porte não se aplicam.** O tratamento de alto risco está entre as exclusões da Res. CD/ANPD nº 2/2022 (art. 3º). Por isso a AgendaFácil precisa indicar formalmente um encarregado e manter o registro completo, não o simplificado (`governance/dpo-framework.md`). Recomenda-se confirmar o enquadramento com a assessoria jurídica.

### Módulos ativados (saída do roteador)

| Módulo | Ativado | Justificativa |
|---|---|---|
| `core` | sim | obrigatório em todo cenário |
| `legal` | sim | obrigatório em todo cenário; inclui bases legais, direitos do titular e transferência internacional |
| `governance` | sim | cenário `saas_web` |
| `appsec` | sim | cenário `saas_web`; há API pública (`/api/agendamentos`) |
| `cloud` | sim | cenário `saas_web`; hospedagem em PaaS e banco gerenciado |
| `devsecops` | sim | cenário `saas_web`; CI/CD ativo |

**Escopo excluído explicitamente:**

- `eca-digital`: o gatilho normativo não dispara. O serviço não é direcionado a menores, não é do tipo provavelmente acessado por eles (agendamento em clínicas que atendem só adultos) e o único cadastro bloqueia menores de 18 anos no servidor (`src/routes/agendamentos.js:23-27`). Ponto de atenção: o bloqueio usa a data de nascimento informada pelo próprio paciente. Se as clínicas passarem a atender menores, ativar `eca-digital` e reavaliar o art. 14 da LGPD.
- `plataformas-digitais`: não há conteúdo de terceiros com difusão pública, venda de anúncios ou impulsionamento, nem IA que gere ou altere imagem ou som. Como a AgendaFácil é provedora de aplicações de internet, os deveres gerais do art. 16-A do Decreto nº 8.771/2016 foram verificados por `governance` (GV-10), com o mapeamento de severidade de `legal/plataformas-digitais.md`. A guarda de registros de acesso (MCI, art. 15) é avaliada uma única vez, como item de `cloud` (IN-04).
- `ai-llm`: não há IA no produto (ver área `ai_llm` em `score_lgpd`).
- `mobile`: não há aplicativo móvel.

### Limitações e convenções

- **Sem acesso à produção.** Os cabeçalhos HTTP efetivos (`curl -I`), o painel da Vercel (membros, MFA, retenção de logs), a configuração do banco (criptografia em repouso, backups) e os termos padrão dos provedores não foram verificados. O que depende deles aparece como `PARCIAL` ou `AUSENTE`, nunca como `CONFORME`.
- **Achados** (`core/auditor-core.md`): todo item `NAO_CONFORME` ou `PARCIAL` gera um achado em `nao_conformidades`.
  - No `NAO_CONFORME`, a severidade do achado é a `criticality` do item.
  - No `PARCIAL`, a severidade reflete a lacuna que resta e nunca passa da `criticality` (ex.: CK-03, DT-03).
- **Contagem única** (`core/scoring-engine.md`): uma mesma falha (mesma causa e mesma evidência) reprova só o item mais específico. Os outros itens afetados a citam e só são reprovados se representarem uma obrigação legal distinta. Neste relatório:
  - O pixel disparado antes do consentimento reprova CK-02. CK-03 cita essa falha e só pontua pela própria lacuna da revogação. GV-09 também é reprovado, porque a transferência internacional é uma obrigação distinta.
  - A CSP enfraquecida pela hospedagem reprova só IN-01; SE-02 a cita.
  - A falta de limitação de tentativas no login reprova só AP-03; SE-04 a cita.
  - A falta de registro e de contratos reprova GV-01 e GV-07; BL-01 os cita.
  - A falta de informação sobre transferência internacional na política reprova GV-09; DT-04 a cita.
- **Prazos:** `IMEDIATO` significa até 7 dias. `IMEDIATO` e `30_DIAS` entram no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo.
- **Evidência:** formato `GRAU (ORIGEM): descrição`, com caminho e linha dos arquivos do projeto.
- **IDs dos itens:** `BL`/`CK` bases legais e cookies, `SE`/`DS` segurança e DevSecOps, `DT` direitos do titular, `GV` governança, `IN` infraestrutura, `AP` APIs e integrações.

---

## 1. Resumo executivo

### Nível geral de conformidade

**Score LGPD: 39/100. Classificação: `CRITICO`.**

O AgendaFácil tem uma base técnica razoável (senhas com bcrypt, HTTPS, controle de acesso por papel, consultas parametrizadas, segredos fora do código), mas a documentação de proteção de dados praticamente não existe e há falhas técnicas pontuais que expõem dados de pacientes. O score técnico é 47,2 e o documental, 15,8. O número baixo vem, sobretudo, da governança (5,4): não há registro das operações, contratos, encarregado, RIPD, plano de incidentes nem política de retenção. Como o produto trata **dados de saúde**, nenhuma severidade pôde ser reduzida pelo porte da empresa, e as dispensas da Res. CD/ANPD nº 2/2022 não se aplicam.

A boa notícia: as cinco ações abaixo custam pouco e atacam os riscos mais graves. Quatro delas se resolvem em menos de uma semana.

### Síntese de riscos por severidade

| Severidade | Achados | Itens |
|---|---|---|
| `CRITICO` | 0 | — |
| `ALTO` | 17 | BL-01, CK-02, SE-06, SE-07, DS-02, DT-01, GV-01, GV-02, GV-03, GV-04, GV-07, GV-08, GV-09, GV-10, IN-01, AP-01, AP-02 |
| `MEDIO` | 13 | CK-03, CK-04, CK-05, SE-04, DT-02, DT-03, DT-04, DT-05, GV-05, GV-06, IN-03, IN-04, AP-03 |
| `BAIXO` | 1 | DS-03 |

Dos 39 itens avaliados, 8 estão `CONFORME`, 10 `PARCIAL` e 21 `NAO_CONFORME`. Não há achado `CRITICO`, mas um item pode chegar a esse nível: se o exame dos termos da Meta e da Vercel mostrar que eles não têm cláusulas-padrão da ANPD nem outro mecanismo legal, GV-09 passa a `CRITICO`.

### O que fazer agora

| # | Ação, em linguagem simples | Por que importa | Esforço | Prazo | Itens |
|---|---|---|---|---|---|
| 1 | Tirar o Meta Pixel da página de agendamento. Se ele for necessário para marketing, carregá-lo só depois do "Aceitar", e só nas páginas institucionais. | Hoje o pixel envia dados de quem está marcando consulta para a Meta, nos EUA, antes de qualquer escolha, inclusive de quem clica em "Rejeitar". | P | `IMEDIATO` | CK-02, CK-03, GV-09 |
| 2 | Parar de gravar CPF e e-mail nos logs e apagar os logs antigos da Vercel. | Qualquer pessoa com acesso aos logs vê CPF e e-mail de pacientes. | P | `IMEDIATO` | SE-06 |
| 3 | Fazer a tela de confirmação receber só data, horário e primeiro nome; dar validade de 8 horas ao login (JWT); corrigir a CSP do `vercel.json`. | A API de confirmação devolve CPF e motivo da consulta a quem tiver o código; um token de login vazado vale para sempre; a CSP atual desliga a proteção contra scripts maliciosos. | P | `IMEDIATO` | AP-02, AP-01, IN-01 |
| 4 | Publicar a política de privacidade completa no site, com um canal para os pacientes pedirem acesso, correção ou exclusão dos dados, e indicar um encarregado. | Sem canal, o paciente não consegue exercer direitos garantidos por lei; a política atual nem está publicada; com dados de saúde, o encarregado é obrigatório. | M | `30_DIAS` | DT-01, DT-03, DT-04, GV-02 |
| 5 | Formalizar os contratos: termos com as clínicas dizendo quem é controlador e quem é operador, e contratos de proteção de dados (DPA) com a Vercel e o provedor do banco, conferindo se trazem as cláusulas-padrão da ANPD para envios ao exterior. | Sem contrato, a AgendaFácil responde junto com as clínicas por qualquer problema e não consegue demonstrar base para os envios de dados ao exterior. | M | `30_DIAS` | GV-07, GV-08, GV-09 |

### Riscos aceitos

Nenhum risco `CRITICO` foi aceito. Há um risco `ALTO` aceito (GV-03, RIPD adiado por até 90 dias), detalhado em `nao_conformidades` e em `riscos_identificados`. O aceite não altera o score.

### Pontos fortes

Senhas com bcrypt (SE-01), HTTPS com HSTS (SE-02), controle de acesso por papel e isolamento por clínica (SE-03), consultas parametrizadas e saída escapada (SE-05), segredos do pipeline em secrets do CI (DS-01), segredos fora do repositório (IN-02), TLS com o banco (AP-04) e banner com botão "Rejeitar" tão visível quanto "Aceitar" (CK-01). Os dados em repouso ficam no Brasil (`sa-east-1`).

---

## 2. Score LGPD

### Resultado

| Indicador | Valor |
|---|---|
| **Score global** | **39/100** |
| **Classificação final** | **`CRITICO`** (faixa 0-49) |
| `score_tecnico` (informativo) | 47,2 |
| `score_documental` (informativo) | 15,8 |
| Natureza do agente | pequeno porte, com tratamento de alto risco (dados de saúde) |
| Modulação de severidade | nenhuma: a condição "sem tratamento de alto risco" de `core/severity-model.md` não é atendida |

### Regras aplicadas (`core/scoring-engine.md`)

- Valor do item: `CONFORME` = 1; `PARCIAL` = 0,5; `NAO_CONFORME` = 0.
- Peso do item pela `criticality`: `CRITICO` = 4; `ALTO` = 3; `MEDIO` = 2; `BAIXO` = 1 (sem modulação).
- `score_area = 100 × Σ(valor × peso) / Σ(peso)`, somando os itens da área. Cada item pontua em uma única área, definida pelo domínio, e cada falha é contada uma única vez.
- `score_global = Σ(score_area × peso_ajustado_area)`.
- O cálculo usa valores exatos. O score de cada área aparece com uma casa decimal, e só o score global é arredondado.

### Área não aplicável

| Área | Status | Justificativa |
|---|---|---|
| `ai_llm` | `NAO_APLICAVEL` | O módulo `ai-llm` não é acionado pelo cenário `saas_web`, e a exclusão está registrada no escopo excluído do roteador. Também não há objeto a avaliar: nenhuma dependência de SDK ou provedor de IA (`package.json:15-25`) e nenhum fluxo de IA declarado (`README.md:18-25`). Primeiro critério de `NAO_APLICAVEL` de `core/scoring-engine.md`. |

As seis áreas restantes somam 90%. Cada peso foi dividido por 0,90: `peso_ajustado_area = peso_area / 0,90`.

### Cálculo por área

| Área | Itens | Σ(valor × peso) | Σ(peso) | `score_area` | Peso original | Peso ajustado |
|---|---|---|---|---|---|---|
| `bases_legais` | 6 | 6,5 | 16 | 40,6 | 15% | 16,67% |
| `seguranca` | 10 | 18,5 | 30 | 61,7 | 25% | 27,78% |
| `direitos_titular` | 5 | 4,5 | 12 | 37,5 | 15% | 16,67% |
| `governanca` | 10 | 1,5 | 28 | 5,4 | 15% | 16,67% |
| `infraestrutura` | 4 | 5,5 | 12 | 45,8 | 10% | 11,11% |
| `apis_integracoes` | 4 | 3,0 | 11 | 27,3 | 10% | 11,11% |
| `ai_llm` | — | — | — | `NAO_APLICAVEL` | 10% | — |
| **Total** | **39** | **39,5** | **109** | | **100%** | **100%** |

**Score global = 39** (valor exato 39,166…, arredondado para o inteiro mais próximo).

**Memória de cálculo** (valor × peso de cada item, na ordem do checklist; frações exatas):

- `bases_legais`: BL-01 0,5×4 + CK-01 1×2 + CK-02 0×3 + CK-03 0,5×3 + CK-04 0,5×2 + CK-05 0×2 = 2 + 2 + 0 + 1,5 + 1 + 0 = **6,5 / 16**
- `seguranca`: SE-01 1×4 + SE-02 1×3 + SE-03 1×3 + SE-04 0,5×3 + SE-05 1×3 + SE-06 0×3 + SE-07 0×3 + DS-01 1×4 + DS-02 0×3 + DS-03 0×1 = 4 + 3 + 3 + 1,5 + 3 + 0 + 0 + 4 + 0 + 0 = **18,5 / 30**
- `direitos_titular`: DT-01 0×3 + DT-02 0,5×2 + DT-03 0,5×3 + DT-04 0,5×2 + DT-05 0,5×2 = 0 + 1 + 1,5 + 1 + 1 = **4,5 / 12**
- `governanca`: GV-01 0×3 + GV-02 0×3 + GV-03 0×3 + GV-04 0×3 + GV-05 0×2 + GV-06 0×2 + GV-07 0×3 + GV-08 0×3 + GV-09 0×3 + GV-10 0,5×3 = **1,5 / 28**
- `infraestrutura`: IN-01 0×3 + IN-02 1×4 + IN-03 0,5×3 + IN-04 0×2 = 0 + 4 + 1,5 + 0 = **5,5 / 12**
- `apis_integracoes`: AP-01 0×3 + AP-02 0×3 + AP-03 0×2 + AP-04 1×3 = **3 / 11**
- **Global:** [15 × (650/16) + 25 × (1850/30) + 15 × (450/12) + 15 × (150/28) + 10 × (550/12) + 10 × (300/11)] / 90 = 3.524,96 / 90 = 39,166… → **39 → `CRITICO`**

### Score técnico e score documental (informativos)

Mesma fórmula, aplicada a todos os itens de cada `control_type`. Não entram na classificação final.

| Subtotal | Itens | Σ(valor × peso) | Σ(peso) | Score |
|---|---|---|---|---|
| `score_tecnico` (`TECNICO`) | 26 | 33,5 | 71 | **47,2** |
| `score_documental` (`DOCUMENTAL`) | 13 | 6,0 | 38 | **15,8** |

Itens `DOCUMENTAL`: BL-01, DT-01, DT-03, DT-04, GV-01 a GV-05 e GV-07 a GV-10. Todos os demais são `TECNICO`. Leitura: o código tem falhas pontuais e corrigíveis, mas a lacuna maior é documental. Quase nada do que a LGPD pede por escrito existe hoje.

### Efeito do risco aceito

O item GV-03 (RIPD) tem aceite de risco registrado e continua `NAO_CONFORME`, com valor 0 e peso 3 em `governanca`. Com ou sem o aceite, `governanca` = 1,5 / 28 = 5,4 e o score global = 39. Aceitar um risco não torna o item conforme.

---

## 3. Checklist de conformidade

Na coluna **Item**: ID · `criticality` (define o peso) · `control_type` — requisito.

### `bases_legais`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **BL-01** · `CRITICO` · `DOCUMENTAL` — Base legal comprovável por finalidade, com o dado de saúde enquadrado no art. 11 | `bases_legais` | `PARCIAL` | `PARCIAL (DOCUMENTAL)`: `docs/lgpd/politica-de-privacidade.md:24-26` indica finalidades compatíveis com art. 7º, V e art. 11, II, "f", mas não nomeia nenhuma base legal. O campo `observacoes` recebe dado de saúde (`db/schema.sql:37`, `public/index.html:35`). A falta de registro das operações e de contrato com as clínicas é contada em GV-01 e GV-07 | Tratamento de dado sensível sem base demonstrável | Nomear a base de cada finalidade e o papel de cada parte |
| **CK-01** · `MEDIO` · `TECNICO` — "Rejeitar" na primeira camada, com o mesmo destaque de "Aceitar" | `bases_legais` | `CONFORME` | `ENCONTRADA (TECNICA)`: botões lado a lado, com o mesmo elemento e o mesmo estilo (`public/index.html:41-45` e `:22`); ambos gravam a escolha (`public/js/consent.js:24-25`) | — | Manter |
| **CK-02** · `ALTO` · `TECNICO` — Scripts de publicidade e analytics bloqueados até o aceite | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: `public/index.html:8-15` carrega `fbevents.js` e dispara `PageView` no `<head>`, antes de `consent.js` rodar (`public/index.html:53`); nenhuma outra base legal documentada | Envio de dados à Meta sem consentimento, em página de agendamento de saúde | Remover o pixel da página de agendamento ou carregá-lo só após o aceite |
| **CK-03** · `ALTO` · `TECNICO` — Revogação efetiva das preferências a qualquer momento | `bases_legais` | `PARCIAL` | `PARCIAL (TECNICA)`: o link "Preferências de cookies" reabre o banner (`public/index.html:50`, `public/js/consent.js:26-29`) e a recusa chama `fbq('consent', 'revoke')` (`consent.js:6-9`), o que interrompe os eventos seguintes, mas não remove o cookie `_fbp` nem o script já carregado. O `PageView` enviado antes da escolha é a falha de CK-02 e não é contado de novo aqui | Identificador da Meta continua no navegador depois da revogação | Na revogação, apagar `_fbp` e não recarregar o pixel |
| **CK-04** · `MEDIO` · `TECNICO` — Registro das escolhas como prova do consentimento | `bases_legais` | `PARCIAL` | `PARCIAL (TECNICA)`: a escolha fica só no `localStorage` do navegador, com data, mas sem versão do banner nem categorias (`public/js/consent.js:12`) | A AgendaFácil não consegue provar o consentimento | Registrar no servidor data, versão do banner e categorias, sem identificar o paciente além do necessário |
| **CK-05** · `MEDIO` · `TECNICO` — Consentimento granular por finalidade, com terceiros identificados | `bases_legais` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: o banner oferece apenas aceitar ou rejeitar tudo e o texto não cita publicidade nem a Meta (`public/index.html:42`) | Consentimento genérico, sem informação prévia adequada | Separar categorias (necessários, medição, publicidade) e nomear os terceiros |

### `seguranca`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **SE-01** · `CRITICO` · `TECNICO` — Senhas armazenadas com hash forte | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`: bcrypt com custo 12 (`src/auth.js:5-8`), comparação em `src/auth.js:19`; coluna `senha_hash` (`db/schema.sql:15`) | — | Manter |
| **SE-02** · `ALTO` · `TECNICO` — HTTPS obrigatório com HSTS | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`: redirecionamento para HTTPS (`api/index.js:14-19`) e HSTS de 1 ano (`api/index.js:32`); a Vercel serve as páginas apenas por HTTPS. A CSP enfraquecida pela hospedagem é contada em IN-01 | — | Manter; conferir o HSTS das páginas estáticas com `curl -I` |
| **SE-03** · `ALTO` · `TECNICO` — Autorização por papel e isolamento entre clínicas | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`: `/api/admin` exige token e papel `admin` (`api/index.js:41`, `src/auth.js:43-50`); as rotas da clínica filtram pelo `clinica_id` do token (`src/routes/clinica.js:13` e `:28`) | — | Manter e cobrir com testes automatizados |
| **SE-04** · `ALTO` · `TECNICO` — Autenticação robusta: segundo fator para quem acessa dados de saúde | `seguranca` | `PARCIAL` | `PARCIAL (TECNICA)`: login por senha bem implementado (`src/auth.js:11-28`), mas sem segundo fator. A falta de limitação de tentativas é contada em AP-03 | Conta de clínica protegida só por senha | MFA para usuários de clínica e de administração |
| **SE-05** · `ALTO` · `TECNICO` — Proteção contra injeção de SQL, XSS e CSRF | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`: todas as consultas usam parâmetros (`src/routes/agendamentos.js:31-45` e `:52-58`, `src/routes/clinica.js:9-30`); a confirmação usa `textContent` (`public/js/agendar.js:28`); o token vai no cabeçalho `Authorization`, não em cookie (`src/auth.js:32`) | — | Manter; acrescentar validação de formato (CPF, datas) |
| **SE-06** · `ALTO` · `TECNICO` — Logs da aplicação sem dados pessoais ou com mascaramento | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: `src/routes/agendamentos.js:29` grava nome, CPF e e-mail do paciente no console, que vira log da Vercel; `src/auth.js:20` grava o e-mail em logins que falham | Dados pessoais legíveis por quem acessa os logs | Registrar só IDs internos; expurgar os logs existentes |
| **SE-07** · `ALTO` · `TECNICO` — Trilha de auditoria de acessos a dados de pacientes | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: nenhum registro de quem consultou ou alterou dados de pacientes (`api/index.js:38-41`, `src/routes/clinica.js:8-33`) | Impossível investigar acesso indevido ou dimensionar um incidente | Registrar usuário, rota, paciente e horário, sem dados pessoais no log |
| **DS-01** · `CRITICO` · `TECNICO` — Segredos do pipeline protegidos e fora dos logs | `seguranca` | `CONFORME` | `ENCONTRADA (TECNICA)`: token e IDs da Vercel vêm de secrets do GitHub (`.github/workflows/ci.yml:27-30`), sem eco em log | — | Manter; restringir o deploy ao ambiente protegido da `main` |
| **DS-02** · `ALTO` · `TECNICO` — Varredura de dependências e SAST no CI | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: o pipeline roda só `install`, `lint` e `test` (`.github/workflows/ci.yml:16-18`); não há `npm audit`, Dependabot, CodeQL nem outra varredura | Biblioteca vulnerável chega à produção sem aviso | `npm audit` no CI, Dependabot e SAST |
| **DS-03** · `BAIXO` · `TECNICO` — SBOM gerado e armazenado | `seguranca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: nenhum SBOM gerado no pipeline (`.github/workflows/ci.yml:9-30`) | Resposta lenta a vulnerabilidades novas | Gerar SBOM CycloneDX a cada build |

### `direitos_titular`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **DT-01** · `ALTO` · `DOCUMENTAL` — Canal para exercício dos direitos do titular | `direitos_titular` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: a política não traz canal nem lista de direitos (`docs/lgpd/politica-de-privacidade.md:36`, TODO pendente); o rodapé só oferece um e-mail genérico (`public/index.html:48`) | O paciente não consegue exercer direitos do art. 18 | Publicar canal específico, com prazo e fluxo de resposta |
| **DT-02** · `MEDIO` · `TECNICO` — Fluxo de atendimento: acesso, correção, eliminação e portabilidade, no prazo do art. 19 | `direitos_titular` | `PARCIAL` | `PARCIAL (TECNICA)`: a clínica corrige nome, telefone e e-mail (`src/routes/clinica.js:21-33`); não há rota nem rotina de cópia, portabilidade ou eliminação, nem controle de prazo | Pedidos atendidos à mão, sem rastreio, ou não atendidos | Rotinas de exportação e eliminação, acionadas pela clínica controladora |
| **DT-03** · `ALTO` · `DOCUMENTAL` — Política de privacidade publicada e acessível | `direitos_titular` | `PARCIAL` | `PARCIAL (DOCUMENTAL)`: o texto existe em `docs/lgpd/politica-de-privacidade.md` e o rodapé aponta para `/privacidade` (`public/index.html:49`), mas não há página correspondente em `public/` nem rota no `vercel.json`; publicação não confirmada | O link pode levar a um erro 404 | Publicar a página e conferir o link em produção |
| **DT-04** · `MEDIO` · `DOCUMENTAL` — Conteúdo da política conforme o art. 9º | `direitos_titular` | `PARCIAL` | `PARCIAL (DOCUMENTAL)`: traz controlador, contato, dados e finalidades (`politica-de-privacidade.md:7-26`); faltam base legal, compartilhamento (clínicas, Vercel, banco, Meta), retenção, direitos, encarregado e detalhes de cookies (`:28-36`); finalidade genérica "Melhorar nossos serviços" (`:26`). A falta de informação sobre transferência internacional é contada em GV-09 | Transparência insuficiente; consentimento sem informação prévia é nulo (art. 9º, §1º) | Reescrever com o modelo `templates/privacy-policy-template.md` |
| **DT-05** · `MEDIO` · `TECNICO` — Aviso no formulário sobre a coleta do motivo da consulta | `direitos_titular` | `PARCIAL` | `PARCIAL (TECNICA)`: o campo é marcado como opcional (`public/index.html:35`), mas não avisa que se trata de informação de saúde compartilhada com a clínica nem traz link para a política junto ao formulário | Dado sensível coletado sem informação clara | Texto de apoio no campo e link para a política ao lado do botão "Agendar" |

### `governanca`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **GV-01** · `ALTO` · `DOCUMENTAL` — Registro das operações de tratamento (art. 37) | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: `docs/lgpd/` contém só a política; o `README.md:27-29` lista dados, sem finalidade, base, retenção nem compartilhamentos | Sem mapa do que é tratado, nada mais se sustenta; com dados sensíveis, `ALTO` | Elaborar o registro completo (a forma simplificada não vale com alto risco) |
| **GV-02** · `ALTO` · `DOCUMENTAL` — Encarregado indicado por ato formal, com contato divulgado | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: nenhum ato de indicação nem contato de encarregado (`politica-de-privacidade.md:36`; rodapé em `public/index.html:47-51`) | Encarregado exigível: a dispensa do pequeno porte não vale com alto risco (Res. CD/ANPD nº 2/2022, art. 3º) | Indicar encarregado (pode ser serviço externo) e divulgar o contato |
| **GV-03** · `ALTO` · `DOCUMENTAL` — RIPD para o tratamento de dados de saúde | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: nenhum RIPD em `docs/lgpd/` | Tratamento de alto risco sem análise formal de impacto | Elaborar o RIPD (risco aceito até 2026-12-31) |
| **GV-04** · `ALTO` · `DOCUMENTAL` — Plano de resposta a incidentes com comunicação em 3 dias úteis | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: nenhum plano ou runbook de incidentes no repositório | Comunicação à ANPD e aos titulares fora do prazo da Res. CD/ANPD nº 15/2024 | Adotar `templates/incident-response-template.md` |
| **GV-05** · `MEDIO` · `DOCUMENTAL` — Política de retenção com prazo por categoria e fundamento no art. 16 | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: nenhuma política de retenção; a política de privacidade não fala de prazos | Dados de saúde guardados indefinidamente | Definir prazos com as clínicas controladoras |
| **GV-06** · `MEDIO` · `TECNICO` — Eliminação automática ao fim do prazo | `governanca` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: o esquema não tem campo de expiração ou exclusão (`db/schema.sql:20-39`) e não há rotina de expurgo nem agendamento no `vercel.json` ou no CI | Base cresce sem limite, assim como o impacto de um vazamento | Job de expurgo ou anonimização, com registro |
| **GV-07** · `ALTO` · `DOCUMENTAL` — Contrato de operador com as clínicas, definindo papéis e instruções (art. 39) | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: não há termos de uso nem contrato de operador; a contratação é on-line (`README.md:16`) e a política apresenta a AgendaFácil como responsável sem distinguir papéis (`politica-de-privacidade.md:9`) | Operadora de dados sensíveis sem contrato (`ALTO`); responsabilidade solidária | Termos de uso com cláusulas de operador |
| **GV-08** · `ALTO` · `DOCUMENTAL` — Contrato de operador (DPA) com a hospedagem e o provedor do banco | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: nenhum DPA com a Vercel nem com o provedor do Postgres (`README.md:22-23`; nada em `docs/lgpd/`); termos padrão aceitos no cadastro não foram apresentados | Suboperadores que tratam dados de saúde sem obrigações contratuais (`ALTO`) | Reunir ou assinar os DPAs e arquivá-los |
| **GV-09** · `ALTO` · `DOCUMENTAL` — Transferência internacional com mecanismo do art. 33 e informação ao titular | `governanca` | `NAO_CONFORME` | `AUSENTE (DOCUMENTAL)`: mecanismo não evidenciado, porque os termos da Meta e da Vercel não foram localizados nem examinados; a política não informa a transferência. O fluxo existe: `public/index.html:13-15` (a mesma evidência de CK-02, reprovada aqui por obrigação distinta, o art. 33) e `public/js/agendar.js:23` enviam dados do navegador do paciente à Meta, nos EUA (sem adequação reconhecida); os logs das funções ficam com a Vercel Inc., nos EUA | Dados de pacientes saem do País sem base demonstrada | Remover o pixel da página de agendamento; examinar os termos e incorporar as CPC da Res. CD/ANPD nº 19/2024 onde faltarem |
| **GV-10** · `ALTO` · `DOCUMENTAL` — Deveres gerais de provedor de aplicações: sede e contato no País e canal de denúncia (Dec. nº 8.771/2016, art. 16-A) | `governanca` | `PARCIAL` | `PARCIAL (DOCUMENTAL)`: razão social, CNPJ, endereço e contato no rodapé (`public/index.html:48`); não há canal de denúncia permanente | Descumprimento de dever vigente desde 20/07/2026 | Página simples de denúncia, que pode ser a mesma do canal de privacidade |

### `infraestrutura`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **IN-01** · `ALTO` · `TECNICO` — A hospedagem não enfraquece os cabeçalhos de segurança do código | `infraestrutura` | `NAO_CONFORME` | `PARCIAL (TECNICA)`: o código define CSP restritiva (`api/index.js:22-34`), mas as páginas de `public/` são servidas direto pela CDN com a CSP do `vercel.json:12-15` (`default-src * 'unsafe-inline' 'unsafe-eval'`), que libera scripts de qualquer origem e não impede o enquadramento da página por outros sites; respostas de produção não verificadas | A página que coleta CPF e dados de saúde fica sem defesa contra XSS e clickjacking | Igualar a CSP do `vercel.json` à do código e conferir com `curl -I` |
| **IN-02** · `CRITICO` · `TECNICO` — Segredos em variáveis de ambiente, fora do repositório | `infraestrutura` | `CONFORME` | `ENCONTRADA (TECNICA)`: `.env` ignorado (`.gitignore:2-4`); `.env.example` só com marcadores (`.env.example:6` e `:9`); o código lê `process.env` (`src/db.js:4`, `src/auth.js:26` e `:36`) | — | Manter; separar segredos de produção e de preview no painel |
| **IN-03** · `ALTO` · `TECNICO` — Banco com criptografia em repouso, backups protegidos e acesso restrito | `infraestrutura` | `PARCIAL` | `PARCIAL (TECNICA)`: banco gerenciado em `sa-east-1` (`.env.example:5-6`) com TLS verificado (`src/db.js:5`); criptografia em repouso, backups e acesso ao painel não são visíveis no repositório | Proteção dos dados de saúde em repouso não comprovada | Anexar evidência do painel (criptografia, backups, membros com MFA) |
| **IN-04** · `MEDIO` · `TECNICO` — Registros de acesso guardados por 6 meses, sob sigilo (MCI, art. 15) | `infraestrutura` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: não há guarda própria dos registros de acesso (IP, porta lógica, data e hora) nem configuração de retenção ou exportação dos logs da Vercel (`vercel.json:1-20`) | Descumprimento do MCI e incapacidade de atender requisição judicial | Exportar os registros de acesso para armazenamento controlado, com expurgo após 6 meses |

### `apis_integracoes`

| Item | Área | Status | Evidência | Impacto | Recomendação |
|---|---|---|---|---|---|
| **AP-01** · `ALTO` · `TECNICO` — Tokens JWT com expiração, algoritmo fixo e audiência | `apis_integracoes` | `NAO_CONFORME` | `PARCIAL (TECNICA)`: a assinatura é verificada, mas `jwt.sign` não define `expiresIn`, `algorithm` nem `audience` (`src/auth.js:24-27`) e `jwt.verify` não restringe algoritmos (`src/auth.js:36`) | Token vazado dá acesso permanente à agenda da clínica | Expiração curta, algoritmo fixo, audiência e revogação |
| **AP-02** · `ALTO` · `TECNICO` — Respostas expõem só os campos necessários | `apis_integracoes` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: `GET /api/agendamentos/:codigo` é público e devolve `SELECT a.*, p.*` (`src/routes/agendamentos.js:51-61`), com CPF, telefone, e-mail, data de nascimento e motivo da consulta; a tela usa só `data_hora` e `nome` (`public/js/agendar.js:25-30`) | Quem tiver o código (link compartilhado, histórico do navegador) lê dados de saúde e CPF | Selecionar só data, horário e primeiro nome |
| **AP-03** · `MEDIO` · `TECNICO` — Limitação de taxa nas APIs | `apis_integracoes` | `NAO_CONFORME` | `AUSENTE (TECNICA)`: nenhuma limitação em `/api/login` nem em `POST /api/agendamentos` (`api/index.js:36-41`; nada em `package.json:15-22`) | Força bruta no login e agendamentos falsos em massa | `express-rate-limit` nas rotas públicas |
| **AP-04** · `ALTO` · `TECNICO` — Criptografia em trânsito com integrações | `apis_integracoes` | `CONFORME` | `ENCONTRADA (TECNICA)`: a conexão com o banco exige TLS com verificação de certificado (`src/db.js:5`; `sslmode=require` em `.env.example:6`); front-end e API usam HTTPS (`api/index.js:14-19`) | — | Manter |

---

## 4. Não conformidades

Todos os 31 itens `NAO_CONFORME` ou `PARCIAL` do checklist estão detalhados abaixo, em ordem de severidade. **Nenhum achado teve severidade modulada**, porque há tratamento de alto risco (ver "Natureza do agente de tratamento"). Os prazos seguem `IMEDIATO` (até 7 dias), `30_DIAS`, `90_DIAS` e `180_DIAS`.

### `ALTO`

#### NC-01 · GV-09 — Dados de pacientes enviados ao exterior sem mecanismo legal demonstrado

- **Problema:** a página de agendamento envia à Meta, nos EUA, identificadores do navegador (cookie `_fbp`, IP, user agent), a URL da clínica e o evento de agendamento. Os logs das funções, que hoje contêm CPF e e-mail (SE-06), ficam com a Vercel Inc., também nos EUA. Os termos desses provedores não foram localizados nem examinados, e a política não informa a transferência.
- **Severidade:** `ALTO`. Os EUA não têm adequação reconhecida pela ANPD. Pelo `legal/international-transfer.md`, o mecanismo **não evidenciado** (termos não examinados) é `ALTO`, com evidência `AUSENTE`, até a verificação. A falta de informação ao titular também é `ALTO`. Se o exame dos termos comprovar que não há CPC nem outro mecanismo, o item passa a `CRITICO` (`criticality` e peso 4).
- **Fundamento LGPD:** arts. 33 a 36; Res. CD/ANPD nº 19/2024 (prazo das CPC encerrado em 23/08/2025); art. 9º, V.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: nenhum contrato, termo ou CPC em `docs/lgpd/`; política sem menção à transferência. Fluxo comprovado em `public/index.html:13-15` e `public/js/agendar.js:23` (`TECNICA`). É a mesma evidência de CK-02, reprovada aqui por obrigação legal distinta.
- **Impacto técnico:** dados de navegação ligados a agendamentos de saúde ficam sob controle de terceiro no exterior, fora do alcance da AgendaFácil.
- **Impacto jurídico:** transferência internacional sem base demonstrada, tema prioritário de fiscalização da ANPD no biênio 2026-2027 (Res. CD/ANPD nº 30/2025); sujeita às sanções do art. 52.
- **Correção recomendada (esforço M):**
  1. Remover o Meta Pixel da página de agendamento, o que elimina o fluxo para a Meta (esforço P).
  2. Mapear as transferências que restarem (Vercel, provedor do banco, ferramentas futuras).
  3. Examinar os termos padrão aceitos; se incorporarem as CPC da Res. CD/ANPD nº 19/2024, arquivá-los como evidência; se não incorporarem, assiná-las.
  4. Informar a transferência na política.
- **Responsável e prazo:** sócia-fundadora (CEO), com assessoria jurídica externa · `IMEDIATO`.

#### NC-02 · BL-01 — Base legal do dado de saúde não demonstrada

- **Problema:** o motivo da consulta é dado sensível de saúde. A política indica finalidades ("preparar o atendimento"), mas nenhum documento diz qual base legal sustenta cada tratamento.
- **Severidade:** `ALTO`. O item é `PARCIAL`, com `criticality` `CRITICO`, porque tratar dado sensível sem base é crítico. A lacuna que resta é de comprovação: há base plausível (art. 11, II, "f", tutela da saúde em procedimento de serviço de saúde, a cargo da clínica), mas ela não está nomeada. A falta de registro (GV-01) e de contrato com as clínicas (GV-07) é contada naqueles itens.
- **Fundamento LGPD:** arts. 7º e 11; art. 6º, X (responsabilização e prestação de contas).
- **Evidência:** `PARCIAL (DOCUMENTAL)`: `docs/lgpd/politica-de-privacidade.md:24-26`; campo `observacoes` em `db/schema.sql:37` e `public/index.html:35`.
- **Impacto técnico:** sem regra clara de finalidade, o campo de texto livre tende a ser reaproveitado (relatórios, marketing).
- **Impacto jurídico:** se a base não for demonstrada numa fiscalização, o item passa a `NAO_CONFORME` e o achado a `CRITICO`.
- **Correção recomendada (esforço M):** registrar, por finalidade, a base legal e o papel de cada parte. Sugestão a validar com o jurídico:
  - identificação do paciente: art. 7º, V (procedimentos preliminares ao contrato com a clínica);
  - motivo da consulta: art. 11, II, "f", sob controle da clínica;
  - pixel e cookies de publicidade: consentimento (art. 7º, I).
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-03 · CK-02 — Meta Pixel disparado antes do consentimento

- **Problema:** o pixel é carregado e envia `PageView` no `<head>` da página de agendamento, antes de o banner aparecer. Quem clica em "Rejeitar" já foi rastreado.
- **Severidade:** `ALTO`. Mapeamento de `appsec/owasp-api.md`: pixels de publicidade de terceiros disparados antes do aceite, sem outra base legal documentada.
- **Fundamento LGPD:** art. 7º, I; art. 8º; art. 6º, III (necessidade).
- **Evidência:** `AUSENTE (TECNICA)`: `public/index.html:8-15`; `consent.js` só roda no fim da página (`public/index.html:53`).
- **Impacto técnico:** cookie `_fbp` gravado e dados enviados à Meta em toda visita, inclusive na página de uma clínica específica, o que revela contexto de saúde.
- **Impacto jurídico:** tratamento sem base legal; consentimento posterior não convalida a coleta anterior.
- **Correção recomendada (esforço P):** remover o pixel da página de agendamento. Se for necessário em páginas institucionais, carregá-lo dinamicamente só após "Aceitar" (ver `recomendacoes_tecnicas`).
- **Responsável e prazo:** desenvolvedor líder (CTO) · `IMEDIATO`.

#### NC-04 · SE-06 — CPF e e-mail gravados nos logs

- **Problema:** cada agendamento grava nome, CPF e e-mail do paciente no console, e cada login com falha grava o e-mail. Na Vercel, o console vira log da plataforma. Exemplo do que aparece hoje: `[agendamento] novo paciente nome=Paciente Exemplo cpf=123.456.789-09 email=paciente@exemplo.example clinica=fisio-exemplo`.
- **Severidade:** `ALTO`. Logs da aplicação com dados pessoais sem mascaramento (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 46; art. 6º, III e VII.
- **Evidência:** `AUSENTE (TECNICA)`: `src/routes/agendamentos.js:29`; `src/auth.js:20`.
- **Impacto técnico:** os dados se espalham para um sistema sem controle de acesso fino nem retenção definida.
- **Impacto jurídico:** medida de segurança inadequada; agrava qualquer incidente.
- **Correção recomendada (esforço P):** registrar só IDs internos (`paciente_id`, `clinica`); para login, registrar o ID do usuário ou um hash do e-mail; expurgar os logs existentes no painel.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-05 · AP-02 — API de confirmação devolve o cadastro completo do paciente

- **Problema:** a rota pública de confirmação devolve todas as colunas do agendamento e do paciente, incluindo CPF, telefone, e-mail, data de nascimento e motivo da consulta. A tela usa apenas data, horário e nome. Qualquer pessoa com o código (link repassado, histórico do navegador, ferramenta de suporte) obtém tudo.
- **Severidade:** `ALTO`. API com exposição excessiva de dados pessoais (`appsec/owasp-api.md`). Não há exploração confirmada; se houver, a falha se enquadra em "falha explorável com exfiltração" (`CRITICO`).
- **Fundamento LGPD:** art. 6º, III (necessidade); art. 46; art. 11.
- **Evidência:** `AUSENTE (TECNICA)`: `src/routes/agendamentos.js:51-61`; uso parcial em `public/js/agendar.js:25-30`.
- **Impacto técnico:** dado de saúde exposto por um endpoint sem autenticação.
- **Impacto jurídico:** potencial incidente com dado sensível, sujeito a comunicação à ANPD.
- **Correção recomendada (esforço P):** selecionar só `a.data_hora` e o primeiro nome; nunca devolver `observacoes`, CPF ou contato em rota pública.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-06 · AP-01 — Token de login sem expiração

- **Problema:** os tokens JWT são emitidos sem validade, algoritmo fixo nem audiência. Um token vazado dá acesso permanente à agenda da clínica, inclusive aos motivos de consulta.
- **Severidade:** `ALTO`. Falha de autenticação sem exploração confirmada (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 46; art. 6º, VII.
- **Evidência:** `PARCIAL (TECNICA)`: `src/auth.js:24-27` (emissão); `src/auth.js:36` (verificação sem `algorithms`).
- **Impacto técnico:** não há como encerrar sessões nem limitar o uso de um token roubado, a não ser trocando o segredo de todos.
- **Impacto jurídico:** medida de segurança inadequada para dados sensíveis.
- **Correção recomendada (esforço P):** `expiresIn: '8h'`, `algorithm: 'HS256'` e `audience` na emissão; `algorithms` e `audience` na verificação; em seguida, avaliar token de renovação com revogação.
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-07 · IN-01 — `vercel.json` anula a CSP definida no código

- **Problema:** o Express define uma CSP restritiva, mas as páginas estáticas, entre elas a que coleta CPF e dados de saúde, são servidas pela CDN da Vercel sem passar pelo Express. O único CSP que recebem é o do `vercel.json`, que permite scripts de qualquer origem, `unsafe-inline` e `unsafe-eval`, e não restringe o enquadramento da página. Para as respostas da API, qual cabeçalho prevalece depende da plataforma e precisa ser verificado em produção.
- **Severidade:** `ALTO`. Hospedagem que remove ou enfraquece cabeçalhos de segurança configurados no código (`cloud/cloud-audit.md`). Pela contagem única, a falha é reprovada só aqui; SE-02 a cita.
- **Fundamento LGPD:** art. 46; art. 6º, VII e VIII.
- **Evidência:** `PARCIAL (TECNICA)`: `vercel.json:12-15` contra `api/index.js:22-34`. Respostas de produção não coletadas.
- **Impacto técnico:** um XSS ou script de terceiro comprometido conseguiria ler o formulário de agendamento; a página pode ser embutida por outros sites (clickjacking).
- **Impacto jurídico:** medida técnica de segurança neutralizada pela configuração da hospedagem.
- **Correção recomendada (esforço P):** substituir o valor no `vercel.json` pela mesma política do código (`default-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'`), acrescentar `Strict-Transport-Security` e conferir com `curl -I` na página e na API. A política restritiva só funciona depois de retirar o pixel inline (CK-02).
- **Responsável e prazo:** CTO · `IMEDIATO`.

#### NC-08 · SE-07 — Sem trilha de auditoria de acessos a dados de pacientes

- **Problema:** não há registro de qual usuário consultou a agenda ou alterou dados de qual paciente.
- **Severidade:** `ALTO`. Ausência de trilha de auditoria (`cloud/cloud-audit.md`), agravada por envolver dados de saúde.
- **Fundamento LGPD:** art. 46; art. 6º, X; art. 37.
- **Evidência:** `AUSENTE (TECNICA)`: `api/index.js:38-41`; `src/routes/clinica.js:8-33`.
- **Impacto técnico:** acesso indevido por funcionário de clínica ou token vazado passa despercebido.
- **Impacto jurídico:** sem trilha, não se consegue avaliar a extensão de um incidente para comunicá-lo no prazo da Res. CD/ANPD nº 15/2024.
- **Correção recomendada (esforço M):** middleware que registre usuário, clínica, rota, ID do paciente e horário, sem dados pessoais, em armazenamento com retenção definida.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-09 · DS-02 — Nenhuma varredura de segurança no CI

- **Problema:** o pipeline não verifica vulnerabilidades em dependências nem faz análise estática de segurança.
- **Severidade:** `ALTO`. Ausência total de varredura de segurança (`devsecops/ci-cd-security.md`).
- **Fundamento LGPD:** art. 46; art. 49.
- **Evidência:** `AUSENTE (TECNICA)`: `.github/workflows/ci.yml:16-18`.
- **Impacto técnico:** vulnerabilidade conhecida em `express`, `jsonwebtoken` ou `pg` chega à produção sem alerta.
- **Impacto jurídico:** sistemas devem atender a requisitos de segurança desde a concepção (art. 49).
- **Correção recomendada (esforço P):** `npm audit --audit-level=high` no job `build`, Dependabot semanal e CodeQL (gratuito para repositórios públicos; para privados, avaliar alternativa).
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-10 · DT-01 — Sem canal para o paciente exercer seus direitos

- **Problema:** a política não lista os direitos do titular nem indica como exercê-los (há um TODO pendente). O único contato é um e-mail comercial genérico.
- **Severidade:** `ALTO`. Ausência de canal para exercício de direitos (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** arts. 18 e 19; art. 9º, VII.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: `docs/lgpd/politica-de-privacidade.md:36`; `public/index.html:48`.
- **Impacto técnico:** pedidos chegam por canais não monitorados e se perdem.
- **Impacto jurídico:** descumprimento direto dos arts. 18 e 19; como operadora, a AgendaFácil também precisa repassar os pedidos às clínicas.
- **Correção recomendada (esforço P):** endereço ou formulário específico de privacidade na política e no rodapé, com fluxo interno e prazo de resposta (imediato em formato simplificado ou até 15 dias, art. 19).
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-11 · GV-01 — Sem registro das operações de tratamento

- **Problema:** não existe inventário com finalidade, base legal, categorias de titulares, compartilhamentos, retenção e medidas de segurança.
- **Severidade:** `ALTO`. Ausência de registro com tratamento de dados sensíveis (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 37.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: `docs/lgpd/` contém só a política; `README.md:27-29` lista dados, sem os demais elementos.
- **Impacto técnico:** sem mapa de dados, não há como garantir eliminação, responder a pedidos nem dimensionar incidentes.
- **Impacto jurídico:** obrigação legal descumprida. Por haver alto risco, a forma simplificada da Res. CD/ANPD nº 2/2022 não está disponível (art. 3º).
- **Correção recomendada (esforço M):** registro em planilha ou documento versionado em `docs/lgpd/`, cobrindo pacientes, usuários das clínicas, visitantes do site e logs.
- **Responsável e prazo:** CEO, com o encarregado · `30_DIAS`.

#### NC-12 · GV-02 — Encarregado não indicado

- **Problema:** não há encarregado indicado nem contato divulgado.
- **Severidade:** `ALTO`. Pelo `governance/dpo-framework.md`, a falta de encarregado quando ele é exigível é `ALTO`. Aqui ele é exigível porque a dispensa do pequeno porte não vale para quem faz tratamento de alto risco (Res. CD/ANPD nº 2/2022, art. 3º).
- **Fundamento LGPD:** art. 41; Res. CD/ANPD nº 18/2024.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: `docs/lgpd/politica-de-privacidade.md:36`; `public/index.html:47-51`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** falta o canal formal com titulares e ANPD, obrigatório para esta empresa.
- **Correção recomendada (esforço P):** indicar encarregado por ato escrito, datado e assinado (pode ser pessoa jurídica, como um serviço de DPO externo) e divulgar o contato no site.
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-13 · GV-03 — Sem RIPD para o tratamento de dados de saúde (risco aceito)

- **Problema:** não há relatório de impacto para a operação que trata dados de saúde.
- **Severidade:** `ALTO`. Ausência de RIPD em tratamento de alto risco pelos critérios da Res. CD/ANPD nº 2/2022 (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 38; art. 5º, XVII.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: nenhum RIPD em `docs/lgpd/`.
- **Impacto técnico:** os riscos do fluxo de agendamento não foram analisados de forma sistemática.
- **Impacto jurídico:** se a ANPD solicitar o RIPD, a AgendaFácil não terá como apresentá-lo, e o tratamento de maior risco fica sem demonstração de salvaguardas.
- **Correção recomendada (esforço G):** elaborar o RIPD com `templates/ripd-template.md`, depois do registro das operações (GV-01), que é seu insumo.
- **Aceite de risco:**
  - `accepted_by`: Ana Exemplo, sócia-administradora e CEO (pessoa fictícia);
  - `accepted_at`: 2026-10-02;
  - `justification`: equipe de 3 pessoas. Os primeiros 30 dias ficam reservados às correções técnicas imediatas e aos documentos que alimentam o RIPD (registro das operações, contratos, encarregado). O RIPD formal fica adiado por até 90 dias, prazo em que o encarregado indicado (GV-02) conduzirá a elaboração;
  - `review_at`: 2026-12-31.
  - O aceite **não** altera status, severidade nem score: o item segue `NAO_CONFORME`, `ALTO`, com valor 0 e peso 3.
- **Responsável e prazo:** CEO, com o encarregado · prazo sugerido `30_DIAS`; execução adiada pelo aceite para `90_DIAS` (até 2026-12-31).

#### NC-14 · GV-04 — Sem plano de resposta a incidentes

- **Problema:** não há procedimento, responsáveis nem modelo de comunicação para incidentes de segurança.
- **Severidade:** `ALTO`. Ausência de processo de resposta a incidentes capaz de comunicar ANPD e titulares em 3 dias úteis (`governance/dpo-framework.md`). O dever não é modulado por porte.
- **Fundamento LGPD:** art. 48; Res. CD/ANPD nº 15/2024 (comunicação em 3 dias úteis, complementável em 20 dias úteis).
- **Evidência:** `AUSENTE (DOCUMENTAL)`: nenhum plano ou runbook no repositório.
- **Impacto técnico:** reação improvisada, perda de evidências e contenção lenta.
- **Impacto jurídico:** comunicação fora do prazo sujeita a processo sancionador; incidentes são tema prioritário de fiscalização (Res. CD/ANPD nº 30/2025).
- **Correção recomendada (esforço M):** adotar `templates/incident-response-template.md`, definir quem decide e quem comunica, e combinar com as clínicas como avisá-las, já que elas comunicam como controladoras.
- **Responsável e prazo:** CEO e CTO · `30_DIAS`.

#### NC-15 · GV-07 — Papéis de controlador e operador não definidos com as clínicas

- **Problema:** não há termos de uso nem contrato que estabeleça que a clínica é controladora dos dados dos pacientes e que a AgendaFácil trata esses dados por instrução dela. A política apresenta a AgendaFácil como responsável por tudo.
- **Severidade:** `ALTO`. Operador sem contrato com cláusulas de proteção de dados que trata dados sensíveis (`governance/dpo-framework.md`).
- **Fundamento LGPD:** art. 5º, VI e VII; art. 39; art. 42, §1º, I.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: `README.md:16`; `docs/lgpd/politica-de-privacidade.md:9`.
- **Impacto técnico:** não há instruções formais sobre retenção, eliminação e atendimento a pedidos.
- **Impacto jurídico:** sem instruções formais, a AgendaFácil pode ser vista como controladora dos dados de saúde e responde solidariamente por danos.
- **Correção recomendada (esforço M):** termos de uso com cláusulas de operador: objeto, instruções, confidencialidade, segurança, suboperadores, apoio a pedidos de titulares e a incidentes, devolução e eliminação ao fim do contrato. Pode partir de `templates/dpa-template.md`.
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-16 · GV-08 — Sem contrato de operador com a Vercel e o provedor do banco

- **Problema:** não foram localizados DPAs com os suboperadores que hospedam a aplicação, os logs e o banco.
- **Severidade:** `ALTO`. Operador sem DPA, inclusive o provedor de hospedagem, que trata dados sensíveis (`governance/dpo-framework.md`): a Vercel processa as requisições com o motivo da consulta, e o banco armazena esses dados.
- **Fundamento LGPD:** art. 39; art. 46.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: `README.md:22-23`; nada em `docs/lgpd/`.
- **Impacto técnico:** não há garantia contratual de segurança, notificação de incidentes nem eliminação ao fim do serviço.
- **Impacto jurídico:** a AgendaFácil não consegue demonstrar à clínica as garantias que deve oferecer como operadora. É uma obrigação distinta do mecanismo de transferência internacional (GV-09), embora os dois costumem ser resolvidos no mesmo instrumento.
- **Correção recomendada (esforço P):** baixar e arquivar os DPAs que os provedores oferecem, verificar a cobertura de suboperadores e de CPC (GV-09) e registrar no registro das operações.
- **Responsável e prazo:** CEO · `30_DIAS`.

#### NC-17 · GV-10 — Sem canal de denúncia de provedor de aplicações

- **Problema:** sede e contato estão no rodapé, mas não há canal permanente de denúncia, exigido de todo provedor de aplicações de internet desde 20/07/2026.
- **Severidade:** `ALTO`. O item é `PARCIAL`; a lacuna que resta é a ausência de canal de denúncia permanente, `ALTO` no mapeamento de `legal/plataformas-digitais.md`, aplicado por `governance` mesmo com aquele módulo inativo.
- **Fundamento:** Decreto nº 8.771/2016, art. 16-A, II (redação do Decreto nº 12.975/2026). Correlato LGPD: art. 6º, VI (transparência).
- **Evidência:** `PARCIAL (DOCUMENTAL)`: `public/index.html:48`.
- **Impacto técnico:** nenhum, além da criação de um canal.
- **Impacto jurídico:** descumprimento de dever geral fiscalizado pela ANPD (Decreto nº 8.771/2016, art. 19-A).
- **Correção recomendada (esforço P):** página "Fale conosco sobre privacidade e denúncias" com formulário ou e-mail monitorado, que preveja expressamente a notificação de conteúdo ilícito.
- **Responsável e prazo:** CEO · `30_DIAS`.

### `MEDIO`

#### NC-18 · CK-03 — Revogação que não apaga o identificador da Meta

- **Problema:** o usuário consegue rever a escolha, e a recusa chama `fbq('consent', 'revoke')`, o que interrompe os eventos seguintes. Mas o cookie `_fbp` e o script já carregado permanecem no navegador.
- **Severidade:** `MEDIO`. O item é `PARCIAL`, com `criticality` `ALTO`: o mecanismo de revogação existe, e a lacuna que resta é a limpeza do identificador. O envio do `PageView` antes da escolha, em cada visita, é a falha de CK-02 e não é contado de novo aqui (contagem única).
- **Fundamento LGPD:** art. 8º, §5º; art. 18, IX.
- **Evidência:** `PARCIAL (TECNICA)`: `public/js/consent.js:6-9` e `:26-29`; `public/index.html:50`.
- **Impacto técnico:** o identificador persistente da Meta segue disponível após a revogação.
- **Impacto jurídico:** revogação incompleta (art. 8º, §5º).
- **Correção recomendada (esforço P):** na revogação, apagar o cookie `_fbp` e não recarregar o pixel. Com o pixel carregado só após o aceite (CK-02), a revogação passa a ser completa.
- **Responsável e prazo:** CTO · `90_DIAS` (resolvido na prática junto com CK-02, `IMEDIATO`).

#### NC-19 · CK-04 — Escolha de cookies sem prova

- **Problema:** a escolha fica apenas no navegador, sem versão do banner nem categorias.
- **Severidade:** `MEDIO`. Ausência de registro das escolhas (`appsec/owasp-api.md`).
- **Fundamento LGPD:** art. 8º, §2º.
- **Evidência:** `PARCIAL (TECNICA)`: `public/js/consent.js:12`.
- **Impacto técnico:** limpar o navegador apaga a prova.
- **Impacto jurídico:** o ônus de provar o consentimento é do controlador.
- **Correção recomendada (esforço M):** registrar no servidor um identificador aleatório, data, versão do banner e categorias aceitas.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-20 · CK-05 — Consentimento de cookies genérico

- **Problema:** o banner oferece só "Aceitar" ou "Rejeitar" tudo e diz apenas "melhorar sua experiência", sem mencionar publicidade nem a Meta.
- **Severidade:** `MEDIO`. Consentimento pouco granular (`appsec/owasp-api.md`); o item é `NAO_CONFORME`, e a severidade é a `criticality`.
- **Fundamento LGPD:** art. 8º, §4º; art. 9º.
- **Evidência:** `AUSENTE (TECNICA)`: `public/index.html:42`.
- **Impacto técnico:** não há como aceitar medição e recusar publicidade.
- **Impacto jurídico:** autorização genérica é nula (art. 8º, §4º).
- **Correção recomendada (esforço M):** categorias separadas, sem pré-marcação, com nome dos terceiros e link para a política de cookies (`templates/cookie-policy-template.md`).
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-21 · SE-04 — Login sem segundo fator

- **Problema:** usuários de clínica acessam motivos de consulta apenas com senha.
- **Severidade:** `MEDIO`. O item é `PARCIAL`, com `criticality` `ALTO`: a senha é bem armazenada e verificada, e a lacuna que resta é o reforço do segundo fator (ausência parcial de hardening, `appsec/owasp-api.md`). A falta de limitação de tentativas é contada em AP-03.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `PARCIAL (TECNICA)`: `src/auth.js:11-28`.
- **Impacto técnico:** senhas fracas ou reutilizadas dão acesso à agenda.
- **Impacto jurídico:** medida de segurança aquém do adequado para dado sensível.
- **Correção recomendada (esforço M):** MFA por aplicativo autenticador para usuários de clínica e de administração.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-22 · DT-02 — Sem rotina para acesso, portabilidade e eliminação

- **Problema:** a clínica consegue corrigir dados, mas não há como gerar cópia, exportar ou eliminar o cadastro de um paciente.
- **Severidade:** `MEDIO`. Inexistência de fluxo de exclusão e portabilidade (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 18, II, V e VI; art. 19.
- **Evidência:** `PARCIAL (TECNICA)`: `src/routes/clinica.js:21-33`.
- **Impacto técnico:** pedidos exigem consultas manuais no banco.
- **Impacto jurídico:** risco de descumprir o prazo do art. 19.
- **Correção recomendada (esforço M):** rotas autenticadas para a clínica exportar (JSON ou CSV) e eliminar ou anonimizar um paciente, com registro da execução.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-23 · DT-03 — Política de privacidade não publicada

- **Problema:** o texto existe no repositório e o rodapé aponta para `/privacidade`, mas não há página correspondente.
- **Severidade:** `MEDIO`. O item é `PARCIAL`, com `criticality` `ALTO`: o texto existe e a publicação não pôde ser verificada. Se a página não existir em produção, o item passa a `NAO_CONFORME` e o achado a `ALTO` ("ausência de política de privacidade").
- **Fundamento LGPD:** art. 9º, caput (acesso facilitado e ostensivo).
- **Evidência:** `PARCIAL (DOCUMENTAL)`: `public/index.html:49`; ausência de `public/privacidade.html`.
- **Impacto técnico:** link quebrado no rodapé.
- **Impacto jurídico:** o titular não tem acesso às informações do tratamento.
- **Correção recomendada (esforço P):** publicar a política revisada (DT-04) em `public/privacidade.html` e testar o link em produção.
- **Responsável e prazo:** CTO · `30_DIAS`.

#### NC-24 · DT-04 — Política de privacidade incompleta

- **Problema:** faltam base legal, compartilhamentos (clínicas, Vercel, provedor do banco, Meta), retenção, direitos do art. 18, encarregado e detalhes de cookies. A finalidade "Melhorar nossos serviços" é genérica. A falta de informação sobre transferência internacional é contada em GV-09.
- **Severidade:** `MEDIO`. Política incompleta frente ao art. 9º (`legal/rights-of-data-subject.md`).
- **Fundamento LGPD:** art. 9º; art. 6º, I (finalidade específica).
- **Evidência:** `PARCIAL (DOCUMENTAL)`: `docs/lgpd/politica-de-privacidade.md:7-36`.
- **Impacto técnico:** nenhum direto.
- **Impacto jurídico:** consentimento obtido sem informação prévia transparente é nulo (art. 9º, §1º).
- **Correção recomendada (esforço M):** reescrever com `templates/privacy-policy-template.md`, explicando que, nos agendamentos, a clínica é a controladora.
- **Responsável e prazo:** CEO e assessoria jurídica · `30_DIAS`.

#### NC-25 · DT-05 — Formulário não avisa que o motivo da consulta é dado de saúde

- **Problema:** o campo é opcional, mas não explica que a informação é de saúde, que será vista pela clínica, nem onde ler mais.
- **Severidade:** `MEDIO`. Transparência incompleta na coleta de dado sensível.
- **Fundamento LGPD:** art. 9º; art. 6º, III e VI.
- **Evidência:** `PARCIAL (TECNICA)`: `public/index.html:35`.
- **Impacto técnico:** pacientes escrevem mais do que o necessário (diagnósticos, medicamentos).
- **Impacto jurídico:** coleta de dado sensível sem informação clara ao titular.
- **Correção recomendada (esforço P):** texto de apoio ("Opcional. Será visto apenas pela clínica para preparar seu atendimento. Não inclua exames ou diagnósticos.") e link para a política junto ao botão "Agendar".
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-26 · GV-05 — Sem política de retenção

- **Problema:** não há prazo definido para manter dados de pacientes, agendamentos e logs, nem fundamento do art. 16 para o que é conservado.
- **Severidade:** `MEDIO`. Retenção sem prazo definido (`governance/dpo-framework.md`).
- **Fundamento LGPD:** arts. 15 e 16.
- **Evidência:** `AUSENTE (DOCUMENTAL)`: nada em `docs/lgpd/`; a política não trata de prazos.
- **Impacto técnico:** acúmulo indefinido de dados de saúde.
- **Impacto jurídico:** conservação além da finalidade viola os arts. 15 e 16.
- **Correção recomendada (esforço M):** definir prazos por categoria com as clínicas controladoras. Exemplos:
  - agendamentos: até X meses após a consulta;
  - registros de acesso: 6 meses (MCI, art. 15; ver IN-04);
  - dados de clínica: até o fim do contrato, mais o prazo legal.

  Se as clínicas considerarem o motivo da consulta parte do prontuário, a guarda longa é delas, não da AgendaFácil.
- **Responsável e prazo:** CEO, com as clínicas · `90_DIAS`.

#### NC-27 · GV-06 — Sem eliminação automática

- **Problema:** o esquema não prevê expiração ou exclusão, e não existe rotina de expurgo.
- **Severidade:** `MEDIO`. Complemento técnico da retenção (`governance/dpo-framework.md`); a evidência é distinta da de GV-05 (código, e não documento).
- **Fundamento LGPD:** arts. 15 e 16; art. 6º, III.
- **Evidência:** `AUSENTE (TECNICA)`: `db/schema.sql:20-39`; nenhum cron no `vercel.json` ou no CI.
- **Impacto técnico:** a base só cresce, e com ela o impacto de um vazamento.
- **Impacto jurídico:** mesmo com política escrita, sem execução não há conformidade.
- **Correção recomendada (esforço M):** job agendado (cron da Vercel ou do banco) que elimine ou anonimize registros vencidos e grave o que foi feito, alcançando também backups conforme a política do provedor.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-28 · IN-03 — Criptografia em repouso do banco não comprovada

- **Problema:** o banco fica no Brasil e a conexão usa TLS, mas não há evidência de criptografia em repouso, proteção dos backups e controle de acesso ao painel.
- **Severidade:** `MEDIO`. O item é `PARCIAL`, com `criticality` `ALTO`: a lacuna é de comprovação. Se ficar confirmado que não há criptografia em repouso, o item passa a `NAO_CONFORME` e o achado a `ALTO` (`cloud/cloud-audit.md`).
- **Fundamento LGPD:** art. 46.
- **Evidência:** `PARCIAL (TECNICA)`: `.env.example:5-6`; `src/db.js:5`.
- **Impacto técnico:** desconhecido até a verificação.
- **Impacto jurídico:** a AgendaFácil não consegue demonstrar a medida de segurança.
- **Correção recomendada (esforço P):** capturar as configurações do painel (criptografia, backups, membros com MFA) e arquivá-las como evidência.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-29 · IN-04 — Registros de acesso sem guarda de 6 meses

- **Problema:** como provedora de aplicações constituída como pessoa jurídica com fins econômicos, a AgendaFácil deve guardar os registros de acesso (IP, porta lógica, data e hora) por 6 meses, sob sigilo. Não há configuração para isso.
- **Severidade:** `MEDIO`. Registros de acesso sem guarda de 6 meses (`cloud/cloud-audit.md`). O requisito é avaliado uma única vez, como item de `cloud`.
- **Fundamento:** MCI, art. 15; Decreto nº 8.771/2016, art. 15-A. Correlato LGPD: art. 7º, II e art. 16, I.
- **Evidência:** `AUSENTE (TECNICA)`: `vercel.json:1-20` sem exportação de logs; nenhum armazenamento próprio.
- **Impacto técnico:** os logs da plataforma podem ser descartados antes do prazo.
- **Impacto jurídico:** descumprimento do MCI, cumulativo com a LGPD.
- **Correção recomendada (esforço M):** exportar os registros de acesso para armazenamento controlado no Brasil, sem dados pessoais além do exigido, com expurgo automático após 6 meses salvo requisição cautelar.
- **Responsável e prazo:** CTO · `90_DIAS`.

#### NC-30 · AP-03 — APIs sem limitação de taxa

- **Problema:** login e agendamento público aceitam requisições ilimitadas, o que também deixa o login sem proteção contra força bruta.
- **Severidade:** `MEDIO`. Ausência parcial de hardening (`appsec/owasp-api.md`). Item mais específico para essa falha; SE-04 o cita.
- **Fundamento LGPD:** art. 46.
- **Evidência:** `AUSENTE (TECNICA)`: `api/index.js:36-41`; `package.json:15-22`.
- **Impacto técnico:** força bruta de senhas e criação massiva de agendamentos falsos.
- **Impacto jurídico:** medida de segurança insuficiente.
- **Correção recomendada (esforço P):** `express-rate-limit` em `/api/login` e `POST /api/agendamentos`, ou o firewall da plataforma.
- **Responsável e prazo:** CTO · `90_DIAS`.

### `BAIXO`

#### NC-31 · DS-03 — Sem SBOM

- **Problema:** não há inventário das dependências gerado a cada build.
- **Severidade:** `BAIXO`. Melhoria com baixo risco imediato.
- **Fundamento LGPD:** art. 46; art. 6º, X.
- **Evidência:** `AUSENTE (TECNICA)`: `.github/workflows/ci.yml:9-30`.
- **Impacto técnico:** diante de uma vulnerabilidade nova, leva mais tempo saber se o projeto é afetado.
- **Impacto jurídico:** baixo; reforça a prestação de contas.
- **Correção recomendada (esforço P):** gerar SBOM CycloneDX no CI e guardá-lo como artefato.
- **Responsável e prazo:** CTO · `180_DIAS`.

---

## 5. Itens obrigatórios ausentes

Requisitos sem nenhuma evidência (`AUSENTE`) que a LGPD, a ANPD ou o MCI exigem de forma direta:

| Requisito | Norma | Item |
|---|---|---|
| Registro das operações de tratamento (forma completa) | LGPD, art. 37; Res. CD/ANPD nº 2/2022, art. 3º | GV-01 |
| Encarregado indicado e contato divulgado | LGPD, art. 41; Res. CD/ANPD nº 18/2024; Res. CD/ANPD nº 2/2022, art. 3º | GV-02 |
| RIPD do tratamento de alto risco (risco aceito até 2026-12-31) | LGPD, arts. 5º, XVII e 38 | GV-03 |
| Plano de resposta e comunicação de incidentes | LGPD, art. 48; Res. CD/ANPD nº 15/2024 | GV-04 |
| Política de retenção e eliminação | LGPD, arts. 15 e 16 | GV-05, GV-06 |
| Contrato de operador com as clínicas | LGPD, art. 39 | GV-07 |
| Contrato de operador com hospedagem e banco | LGPD, art. 39 | GV-08 |
| Mecanismo de transferência internacional (não evidenciado) e informação ao titular | LGPD, arts. 33 e 9º; Res. CD/ANPD nº 19/2024 | GV-09 |
| Canal de exercício de direitos | LGPD, arts. 18 e 19 | DT-01 |
| Canal de denúncia de provedor de aplicações | Decreto nº 8.771/2016, art. 16-A, II | GV-10 |
| Guarda de registros de acesso por 6 meses | MCI, art. 15 | IN-04 |
| Bloqueio de rastreamento antes do consentimento | LGPD, arts. 7º, I e 8º | CK-02 |
| Mascaramento de dados pessoais em logs | LGPD, art. 46 | SE-06 |

---

## 6. Riscos identificados

### Técnicos

- Exposição de CPF, contato e motivo da consulta pela API pública de confirmação (AP-02).
- Tokens de login sem validade: um vazamento dá acesso permanente (AP-01).
- Dados pessoais espalhados nos logs da plataforma (SE-06).
- Página de coleta sem CSP efetiva, vulnerável a XSS e clickjacking (IN-01).
- Dependências vulneráveis sem detecção (DS-02, DS-03).
- Acesso indevido sem rastro (SE-07); contas protegidas só por senha e sem limite de tentativas (SE-04, AP-03).

### Jurídicos

- Transferência internacional sem mecanismo do art. 33 demonstrado, tema prioritário de fiscalização. Pode subir a `CRITICO` se o exame dos termos comprovar ausência de CPC (GV-09).
- Tratamento de dado de saúde sem base legal demonstrada e sem papéis definidos com as clínicas, com responsabilidade solidária do operador, art. 42, §1º, I (BL-01, GV-07).
- Rastreamento sem consentimento válido (CK-02, CK-03, CK-05).
- Obrigações documentais básicas ausentes, agravadas pela perda das dispensas do pequeno porte: registro completo, encarregado, RIPD, incidentes, retenção, contratos, canal de direitos e canal de denúncia (seção 5).
- Exposição às sanções do art. 52 da LGPD (advertência; multa de até 2% do faturamento, limitada a R$ 50 milhões por infração; publicização; bloqueio e eliminação dos dados), com dosimetria pela Res. CD/ANPD nº 4/2023. Some-se a isso o MCI (art. 12) para os deveres de provedor de aplicações.

### Operacionais

- Equipe de 3 pessoas sem plano de incidentes: um vazamento pararia o produto e estouraria o prazo de 3 dias úteis (GV-04).
- Pedidos de titulares e de clínicas atendidos à mão, sem rotina de exportação ou eliminação (DT-02).
- Base de dados crescendo sem limite (GV-05, GV-06).
- Clínicas mais estruturadas devem exigir DPA e evidências de segurança na contratação; sem eles, vendas travam (GV-07, GV-08).

### Reputacionais

- Pixel de publicidade em página de agendamento de saúde é o tipo de caso que costuma virar notícia e afastar clínicas e pacientes (CK-02, GV-09).
- Um vazamento de motivos de consulta atinge a confiança das clínicas, que respondem perante seus pacientes e conselhos profissionais (AP-02, SE-06).

### Riscos aceitos

| Item | Severidade | Aceito por | Data do aceite | Justificativa | Revisão |
|---|---|---|---|---|---|
| GV-03 — RIPD do tratamento de dados de saúde | `ALTO` | Ana Exemplo, sócia-administradora e CEO (fictícia) | 2026-10-02 | Os primeiros 30 dias da equipe de 3 pessoas ficam com as correções técnicas imediatas e com os documentos que alimentam o RIPD (registro, contratos, encarregado); adiamento de até 90 dias, com o RIPD conduzido pelo encarregado indicado | 2026-12-31 |

O aceite fica registrado para prestação de contas. O item continua pontuando como `NAO_CONFORME` e deve ser reavaliado na data de revisão.

---

## 7. Plano de adequação

Esforço: `P` até 1 dia; `M` até 1 semana; `G` mais de 1 semana. `IMEDIATO` significa até 7 dias. `IMEDIATO` e `30_DIAS` ficam no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo.

### Curto prazo (0-30 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 1 | Remover o Meta Pixel da página de agendamento; se mantido no site institucional, carregar só após o aceite e apagar `_fbp` na revogação | CK-02, CK-03, GV-09 | CTO | P | `IMEDIATO` |
| 2 | Retirar CPF, nome e e-mail dos logs e expurgar os logs existentes | SE-06 | CTO | P | `IMEDIATO` |
| 3 | Reduzir a resposta da confirmação a data, horário e primeiro nome | AP-02 | CTO | P | `IMEDIATO` |
| 4 | Expiração, algoritmo e audiência no JWT | AP-01 | CTO | P | `IMEDIATO` |
| 5 | Corrigir a CSP e acrescentar HSTS no `vercel.json`; conferir com `curl -I` | IN-01 | CTO | P | `IMEDIATO` |
| 6 | Mapear as transferências internacionais, examinar os termos dos provedores e incorporar CPC onde faltarem | GV-09 | CEO + jurídico | M | `IMEDIATO` |
| 7 | Reunir e arquivar os DPAs da Vercel e do provedor do banco | GV-08 | CEO | P | `30_DIAS` |
| 8 | Termos de uso com cláusulas de operador para as clínicas | GV-07, BL-01 | CEO + jurídico | M | `30_DIAS` |
| 9 | Indicar encarregado (interno ou serviço externo) | GV-02 | CEO | P | `30_DIAS` |
| 10 | Reescrever e publicar a política de privacidade, com canal de direitos e canal de denúncia | DT-01, DT-03, DT-04, GV-10 | CEO + jurídico; publicação pelo CTO | M | `30_DIAS` |
| 11 | Registro das operações de tratamento, na forma completa | GV-01 | CEO + encarregado | M | `30_DIAS` |
| 12 | Plano de resposta a incidentes, combinado com as clínicas | GV-04 | CEO + CTO | M | `30_DIAS` |
| 13 | `npm audit`, Dependabot e SAST no CI | DS-02 | CTO | P | `30_DIAS` |
| 14 | Trilha de auditoria de acessos a dados de pacientes | SE-07 | CTO | M | `30_DIAS` |

### Médio prazo (30-90 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 15 | RIPD do tratamento de dados de saúde (prazo sugerido `30_DIAS`, adiado pelo aceite de risco até 2026-12-31) | GV-03 | CEO + encarregado | G | `90_DIAS` |
| 16 | Política de retenção definida com as clínicas | GV-05 | CEO + clínicas | M | `90_DIAS` |
| 17 | Job de eliminação ou anonimização automática | GV-06 | CTO | M | `90_DIAS` |
| 18 | Rotinas de exportação e eliminação para a clínica | DT-02 | CTO | M | `90_DIAS` |
| 19 | Aviso sobre dado de saúde no campo "Motivo da consulta" | DT-05 | CTO | P | `90_DIAS` |
| 20 | Banner com categorias e registro das escolhas no servidor | CK-04, CK-05 | CTO | M | `90_DIAS` |
| 21 | MFA e limitação de tentativas no login e nas rotas públicas | SE-04, AP-03 | CTO | M | `90_DIAS` |
| 22 | Guarda dos registros de acesso por 6 meses, com expurgo | IN-04 | CTO | M | `90_DIAS` |
| 23 | Evidências do painel do banco (criptografia, backups, MFA) | IN-03 | CTO | P | `90_DIAS` |

### Longo prazo (90-180 dias)

| # | Ação | Itens | Responsável sugerido | Esforço | Prazo |
|---|---|---|---|---|---|
| 24 | Gerar SBOM a cada build | DS-03 | CTO | P | `180_DIAS` |
| 25 | Revisar o aceite de risco do RIPD e repetir esta auditoria (`/lgpd-saas`) para medir a evolução | GV-03 e todos | CEO + encarregado | P | `180_DIAS` |
| 26 | Revisão semestral da política, dos contratos e do registro; treinamento básico de privacidade para a equipe e as clínicas | DT-04, GV-01, GV-07 | Encarregado | M | `180_DIAS` |

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

**Pixel só após o aceite, e nunca na página de agendamento.** Remover o bloco `public/index.html:7-16`. Em páginas institucionais, carregar o script a partir de `aplicar('aceito')` em `consent.js`, por um arquivo próprio (não inline), para manter a CSP restritiva. Na revogação, apagar o cookie `_fbp` (`document.cookie = '_fbp=; Max-Age=0; path=/'`, com o domínio usado pelo pixel).

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

**Trilha de auditoria:** middleware nas rotas `/api/clinica` e `/api/admin` que registre `usuario`, `clinica`, `metodo`, `rota`, `paciente_id` e horário em tabela própria, com retenção definida na política (GV-05).

**Eliminação automática:** job agendado que execute, conforme os prazos da política, `DELETE` ou anonimização (`nome = 'removido'`, `cpf = NULL`, `observacoes = NULL`) dos registros vencidos e grave quantos foram afetados.

**Em monitoramento (norma não vigente, não gera não conformidade):** a revisão da Res. CD/ANPD nº 1/2021 (fiscalização e processo sancionador) está em consulta pública até 26/10/2026. Até a publicação da norma final, a Res. CD/ANPD nº 1/2021 segue vigente e é a referência de risco sancionatório deste relatório.

---

## Glossário

- **ANPD:** Agência Nacional de Proteção de Dados, que regula e fiscaliza a LGPD.
- **Agente de pequeno porte:** microempresa, empresa de pequeno porte, startup e equivalentes, com regras simplificadas pela Res. CD/ANPD nº 2/2022, salvo nas exclusões da própria resolução, como o tratamento de alto risco.
- **Tratamento de alto risco:** tratamento em larga escala ou com impacto significativo para os titulares, combinado com fatores como dados sensíveis; impede as simplificações do pequeno porte.
- **Controlador:** quem decide por que e como os dados são tratados (aqui, a clínica, para os dados dos pacientes).
- **Operador:** quem trata dados em nome do controlador (aqui, a AgendaFácil, para os dados dos pacientes).
- **Dado pessoal sensível:** dado sobre saúde, origem racial, religião, vida sexual, biometria e outros do art. 5º, II, com regras mais rígidas.
- **Base legal:** hipótese da lei que autoriza um tratamento (arts. 7º e 11).
- **Encarregado (DPO):** pessoa ou empresa que faz a ponte entre a organização, os titulares e a ANPD.
- **Registro das operações de tratamento:** inventário do que é tratado, para quê, com qual base, por quanto tempo e com quem é compartilhado (art. 37).
- **RIPD:** relatório de impacto à proteção de dados, que analisa riscos e salvaguardas de um tratamento.
- **DPA (contrato de operador):** contrato que fixa as obrigações de proteção de dados de quem trata dados em nome de outro.
- **CPC (cláusulas-padrão contratuais):** cláusulas aprovadas pela ANPD que autorizam enviar dados a países sem adequação reconhecida.
- **Transferência internacional:** envio ou acesso a dados pessoais a partir de outro país.
- **Mecanismo não evidenciado:** contrato ou termos não localizados ou não examinados; diferente de mecanismo comprovadamente ausente, que é mais grave.
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
- **`NAO_APLICAVEL`:** área de score cujo objeto não existe no projeto (aqui, IA); seu peso é redistribuído.

---

> Este relatório foi gerado com apoio de IA pelo LGPD Enterprise Auditor, a partir das evidências disponíveis no momento da análise. Ele apoia, mas não substitui, a avaliação do encarregado (DPO) e a assessoria jurídica especializada. As conclusões dependem da completude e da atualidade das evidências fornecidas.
