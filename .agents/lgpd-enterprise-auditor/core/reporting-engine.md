# Reporting Engine

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
- síntese de riscos por severidade.

### `score_lgpd`
- score 0-100;
- classificação final canônica;
- score por área;
- áreas `NAO_APLICAVEL`, com justificativa, e pesos ajustados (regra de `core/scoring-engine.md`).

### `checklist_conformidade`
Tabela obrigatória:
`Item | Status | Evidência | Impacto | Recomendação`

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
- correção recomendada.

### `riscos_identificados`
Separar por:
- técnicos;
- jurídicos;
- operacionais;
- reputacionais.

### `plano_adequacao`
- curto prazo: 0-30 dias;
- médio prazo: 30-90 dias;
- longo prazo: 90-180 dias.

## Regra de consistência
Toda não conformidade listada no checklist deve aparecer detalhada em `nao_conformidades`.
