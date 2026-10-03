# Núcleo — formato do relatório

## Objetivo
Definir formato obrigatório e ordem de construção do relatório final.

## Estrutura obrigatória
1. `resumo_executivo`
2. `score_lgpd`
3. `checklist_conformidade`
4. `nao_conformidades`
5. `itens_obrigatorios_ausentes`
6. `riscos_identificados`
7. `plano_adequacao`
8. `recomendacoes_tecnicas`

## Campos mínimos por seção

### `resumo_executivo`
- nível geral de conformidade;
- síntese de riscos por severidade;
- **o que fazer agora**: as 3 a 5 ações de maior impacto, em linguagem simples, cada uma com esforço (`P | M | G`) e prazo;
- riscos aceitos de severidade `CRITICO`, quando houver, em destaque.

### `score_lgpd`
- score 0-100;
- classificação final canônica;
- score por área;
- áreas `NAO_APLICAVEL`, com justificativa, e pesos ajustados (regra de `core/scoring-engine.md`);
- `score_tecnico` e `score_documental` (informativos);
- natureza do agente de tratamento e eventuais modulações de severidade por porte.

### `checklist_conformidade`
Tabela obrigatória:
`Item | Área | Status | Evidência | Impacto | Recomendação`

A coluna `Área` traz a `score_area` do item (mapa de `core/scoring-engine.md`).

Status permitidos:
- `CONFORME`
- `PARCIAL`
- `NAO_CONFORME`

A célula `Evidência` deve registrar os dois eixos de `core/evidence-engine.md` no formato `GRAU (ORIGEM): descrição`, ex.: `ENCONTRADA (TECNICA): política de retenção aplicada em job de expurgo`.

### `nao_conformidades`
Para cada achado:
- problema;
- severidade;
- fundamento LGPD;
- impacto técnico;
- impacto jurídico;
- evidência (com `evidence_type` e `evidence_source`);
- correção recomendada, com esforço (`P | M | G`);
- modulação de severidade, quando houver;
- aceite de risco, quando houver (quem aceitou, quando, justificativa e data de revisão).

### `riscos_identificados`
Separar por:
- técnicos;
- jurídicos;
- operacionais;
- reputacionais.

Listar à parte os **riscos aceitos**, com o registro de aceite de cada um.

### `plano_adequacao`
- curto prazo: 0-30 dias;
- médio prazo: 30-90 dias;
- longo prazo: 90-180 dias.

`IMEDIATO` e `30_DIAS` entram no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo. Cada ação traz responsável sugerido e esforço estimado (`P`: até 1 dia; `M`: até 1 semana; `G`: mais de 1 semana).

## Após as 8 seções
- **Glossário**: termos técnicos e jurídicos usados no relatório (ex.: registro das operações de tratamento, encarregado, RIPD, varredura de dependências), em uma linha cada, para leitores de fora da área.
- **Aviso legal** (texto fixo, ao final de todo relatório):
  > Este relatório foi gerado com apoio de IA pelo LGPD Enterprise Auditor, a partir das evidências disponíveis no momento da análise. Ele apoia, mas não substitui, a avaliação do encarregado (DPO) e a assessoria jurídica especializada. As conclusões dependem da completude e da atualidade das evidências fornecidas.

Glossário e aviso legal não contam como seções e não alteram a ordem obrigatória.

## Classificação e armazenamento
O relatório descreve falhas que podem estar abertas e é **confidencial**:
- iniciar o documento com a marcação `CONFIDENCIAL — uso interno`;
- não versionar em repositório público; preferir local fora do repositório auditado ou pasta ignorada pelo git (ex.: `docs/lgpd/auditorias/`, listada no `.gitignore`);
- compartilhar só com quem precisa agir sobre os achados;
- nomear com data e escopo (ex.: `auditoria-lgpd-AAAA-MM-<cenario>.md`) para permitir comparação entre auditorias.

## Regra de consistência
Todo item `NAO_CONFORME` ou `PARCIAL` do checklist deve aparecer detalhado em `nao_conformidades`.
