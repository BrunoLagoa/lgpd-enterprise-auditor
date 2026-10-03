# Scoring Engine

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

## Cálculo do score (obrigatório)
O cálculo é fechado para que duas execuções sobre as mesmas evidências cheguem ao mesmo número.

1. **Valor do item** pelo status: `CONFORME` = 1; `PARCIAL` = 0,5; `NAO_CONFORME` = 0.
2. **Peso do item** pela `criticality` (severidade que teria se não conforme, já considerada a modulação por porte de `core/severity-model.md`): `CRITICO` = 4; `ALTO` = 3; `MEDIO` = 2; `BAIXO` = 1.
3. **Score da área** (0-100): `score_area = 100 * SUM(valor * peso) / SUM(peso)`, somando os itens cuja `score_area` é aquela área.
4. **Score global**: aplicar o peso de cada área (ajustado quando houver área `NAO_APLICAVEL`) e somar.

Fórmula:
`score_global = SUM(score_area * peso_area)`

Calcular com valores exatos; exibir o score de cada área com uma casa decimal e arredondar só o score global, para o inteiro mais próximo.

**Contagem única:** uma mesma falha (mesma causa e mesma evidência) reprova um único item, o mais específico. Outros itens afetados a citam na evidência e só são reprovados se representarem obrigação legal distinta (ex.: o mesmo pixel viola o consentimento de cookies e também configura transferência internacional sem mecanismo). Uma área aplicável sem nenhum item avaliado indica cobertura insuficiente: avaliar ao menos um item dela; se não for possível, declarar "cobertura insuficiente" em `score_lgpd` e redistribuir seu peso como na regra de `NAO_APLICAVEL`, sem chamá-la assim.

## Mapa de áreas por domínio
Cada `check_item` pontua em **exatamente uma** área, definida pelo seu domínio. Módulos não escolhem a área caso a caso.

| Domínio de auditoria | Área de score |
|---|---|
| Bases legais (arts. 7º e 11), dados de acesso público e dados de crianças (art. 14) | `bases_legais` |
| 1. Mapeamento de dados | `governanca` |
| 2. Consentimento | `bases_legais` |
| 3. Direitos do titular | `direitos_titular` |
| 4. Política de privacidade (inclui transparência, art. 9º) | `direitos_titular` |
| 5. Cookies e tracking | `bases_legais` |
| 6. Segurança da informação | `seguranca` |
| 7. Cloud security (inclui PaaS e hospedagem) | `infraestrutura` |
| 8. Mobile security | `seguranca` |
| 9. APIs e integrações | `apis_integracoes` |
| 10. DevSecOps | `seguranca` |
| 11. Logs e observabilidade | `seguranca` |
| 12. IA/LLM | `ai_llm` |
| 13. Governança (encarregado, RIPD, incidentes, políticas) | `governanca` |
| 14. Compartilhamento de dados (inclui transferência internacional) | `governanca` |
| 15. Retenção e exclusão | `governanca` |
| 16. Proteção de crianças e adolescentes no ambiente digital — ECA Digital (deveres de produto) | `governanca` |
| 17. Plataformas digitais e conteúdo de terceiros | `governanca` |

## Score técnico e score documental (informativos)
Além do score global, o relatório mostra dois subtotais com a mesma fórmula dos passos 1 a 3, aplicada a todos os itens de cada natureza (`control_type`):
- `score_tecnico`: itens `TECNICO`;
- `score_documental`: itens `DOCUMENTAL`.

Os subtotais **não** entram na classificação final; servem para mostrar, por exemplo, um núcleo técnico forte com documentação ausente.

## Riscos aceitos
Item com `risk_acceptance` registrado continua pontuando pelo seu status. Aceitar um risco não torna o item conforme.

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
Para evitar ambiguidades, os relatórios devem usar exatamente os rótulos canônicos acima.

## Convenção de identificadores
- IDs de módulo usam kebab-case (ex.: `ai-llm`).
- IDs de área de score usam snake_case (ex.: `ai_llm`).
- Mapeamento obrigatório:
  - `ai-llm` (módulo) -> `ai_llm` (área de score).
