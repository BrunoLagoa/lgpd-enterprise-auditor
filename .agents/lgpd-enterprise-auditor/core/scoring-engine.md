# Scoring Engine (V2)

## Objetivo
Padronizar cálculo e classificação do score LGPD em escala 0-100.

## Pesos por área
- `bases_legais`: 15%
- `seguranca`: 25%
- `direitos_titular`: 15%
- `governanca`: 15%
- `infraestrutura`: 10%
- `apis_integracoes`: 10%
- `ai_llm`: 10%

Somatório obrigatório: 100%.

## Cálculo recomendado
1. Calcular score parcial de cada área (0-100) com base no percentual de itens conformes ponderados por criticidade.
2. Aplicar peso da área.
3. Somar resultados para score global (0-100).

Fórmula:
`score_global = SUM(score_area * peso_area)`

## Classificação final canônica
- `0-49`: `CRITICO`
- `50-69`: `BAIXO_NIVEL`
- `70-84`: `PARCIALMENTE_CONFORME`
- `85-94`: `ALTA_CONFORMIDADE`
- `95-100`: `EXCELENTE`

## Normalização de rótulos
Para evitar ambiguidades da V1, os relatórios devem usar exatamente os rótulos canônicos acima.

## Convenção de identificadores
- IDs de módulo usam kebab-case (ex.: `ai-llm`).
- IDs de área de score usam snake_case (ex.: `ai_llm`).
- Mapeamento obrigatório:
  - `ai-llm` (módulo) -> `ai_llm` (área de score).
