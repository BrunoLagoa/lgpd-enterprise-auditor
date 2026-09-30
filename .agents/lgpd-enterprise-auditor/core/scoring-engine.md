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
2. Aplicar peso da área (peso ajustado quando houver área `NAO_APLICAVEL`).
3. Somar resultados para score global (0-100).

Fórmula:
`score_global = SUM(score_area * peso_area)`

## Áreas não aplicáveis
`NAO_APLICAVEL` é status de **área de score**, não de `check_item` (cujo status continua restrito a `CONFORME | PARCIAL | NAO_CONFORME`).

Uma área só pode ser `NAO_APLICAVEL` quando o objeto que ela avalia não existe no escopo auditado — nunca por falta de evidência. Falta de evidência é `AUSENTE` e reduz o score.

Critérios (basta um):
- nenhum módulo ativo pontua a área, e a exclusão está registrada no "escopo excluído explicitamente" da saída de `orchestrator/router.md`; ou
- o módulo foi ativado (ex.: `full_audit`), mas comprovou a inexistência do objeto com evidência `ENCONTRADA` (ex.: nenhum SDK ou chamada a provedor de LLM no código e nenhum fluxo de IA declarado).

Áreas sempre aplicáveis, nunca `NAO_APLICAVEL`: `bases_legais`, `seguranca`, `direitos_titular` e `governanca`.

Redistribuição proporcional entre as áreas aplicáveis:
`peso_ajustado_area = peso_area / SUM(peso das áreas aplicáveis)`
`score_global = SUM(score_area * peso_ajustado_area)`

Exemplo: `saas_web` sem uso de IA → `ai_llm` é `NAO_APLICAVEL`; as seis áreas restantes somam 90% e cada peso é dividido por 0,90 (`seguranca` passa de 25% para 27,8%).

O relatório deve declarar em `score_lgpd` as áreas `NAO_APLICAVEL`, a justificativa e os pesos ajustados.

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
