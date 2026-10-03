# Núcleo — contratos do auditor

## Objetivo
Estabelecer os contratos canônicos da auditoria LGPD Enterprise, garantindo consistência entre módulos especialistas, scoring e relatórios.

## Princípios obrigatórios
- Não assumir conformidade sem evidência.
- Exigir base legal válida para cada operação de tratamento.
- Priorizar minimização, segurança, rastreabilidade e privacy by design/default.
- Avaliar impacto técnico, jurídico, operacional e reputacional.

## Contratos canônicos

### `finding`
Estrutura mínima para cada não conformidade. Todo `check_item` com status `NAO_CONFORME` **ou** `PARCIAL` gera um `finding`: no `NAO_CONFORME`, a severidade é a `criticality` do item; no `PARCIAL`, reflete a lacuna que resta e nunca excede a `criticality`.
- `id`: identificador único.
- `module`: módulo origem (ex.: `cloud`, `ai-llm`).
- `title`: título objetivo.
- `problem`: descrição objetiva do problema.
- `severity`: `CRITICO | ALTO | MEDIO | BAIXO`.
- `lgpd_article`: artigo(s) aplicáveis da LGPD.
- `evidence_type`: grau de comprovação do controle - `ENCONTRADA | PARCIAL | AUSENTE` (um único grau por achado).
- `evidence_source`: origem da evidência - `TECNICA | DOCUMENTAL`; um achado pode ter as duas origens (`TECNICA + DOCUMENTAL`).
- `evidence`: uma ou mais evidências observadas, cada uma com sua origem e descrição rastreável.
- `evidence_confidence`: confiança da evidência - `ALTA | MEDIA | BAIXA` (`core/evidence-engine.md`).
- `technical_impact`: impacto técnico.
- `legal_impact`: impacto jurídico/regulatório.
- `recommendation`: ação recomendada.
- `owner`: responsável sugerido.
- `deadline_suggestion`: `IMEDIATO | 30_DIAS | 90_DIAS | 180_DIAS` (`IMEDIATO` = até 7 dias).
- `effort`: esforço estimado da correção - `P | M | G` (P: até 1 dia; M: até 1 semana; G: mais de 1 semana).
- `severity_modulation` (opcional): quando a severidade foi modulada por porte e exposição (`core/severity-model.md`) - severidade original, severidade aplicada e justificativa.
- `risk_acceptance` (opcional): quando o controlador decidiu aceitar o risco - `accepted_by` (nome e papel de quem aceitou), `accepted_at` (data), `justification`, `review_at` (data de revisão, no máximo 12 meses depois) e, se o aceite adiar a correção, `accepted_deadline` (novo prazo, mantido também o `deadline_suggestion` original). O aceite **não** altera status, severidade nem score.

### `check_item`
Estrutura mínima de checklist:
- `id`: identificador único.
- `domain`: domínio de auditoria (um dos 17 de `orchestrator/full-audit.md`, ex.: `consentimento`, `apis_integracoes`).
- `score_area`: área de score em que o item pontua - exatamente uma, definida pelo domínio (mapa em `core/scoring-engine.md`).
- `criticality`: severidade que o item teria se não conforme - `CRITICO | ALTO | MEDIO | BAIXO`; define o peso do item no score.
- `control_type`: natureza do controle - `TECNICO` (código, configuração, infraestrutura) ou `DOCUMENTAL` (política, contrato, registro, processo). Item que exige os dois é classificado por onde o controle é executado: em sistema, `TECNICO`; por ato formal, `DOCUMENTAL`.
- `item`: requisito validado.
- `applicability`: `APLICAVEL | NAO_APLICAVEL | NAO_VERIFICADO` (regras em `core/scoring-engine.md`). Só item `APLICAVEL` tem `status` e entra no score.
- `status`: `CONFORME | PARCIAL | NAO_CONFORME` (apenas para item `APLICAVEL`).
- `evidence`: uma ou mais evidências, cada uma com sua origem e descrição rastreável.
- `evidence_type`: `ENCONTRADA | PARCIAL | AUSENTE` (um único grau por item).
- `evidence_source`: `TECNICA | DOCUMENTAL`; um item pode ter as duas origens (`TECNICA + DOCUMENTAL`).
- `evidence_confidence`: `ALTA | MEDIA | BAIXA` (`core/evidence-engine.md`).
- `impact`: impacto caso falha.
- `recommendation`: correção sugerida.

### `module_output`
Resultado padrão por módulo:
- `module`: nome do módulo.
- `coverage`: cobertura do módulo - itens com `status` ÷ (itens com `status` + itens `NAO_VERIFICADO`), em percentual.
- `check_items`: lista de `check_item`.
- `findings`: lista de `finding`.
- `score_partial`: score parcial do módulo (0-100).
- `gaps`: itens obrigatórios ausentes.
- `recommendations`: recomendações priorizadas.

## Fluxo mínimo de execução
1. Levantar o contexto: primeiro ler o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependência e de infraestrutura); apresentar o contexto inferido e perguntar só o que faltar, incluindo a natureza do agente de tratamento (entradas de `orchestrator/router.md`) e o formato de saída do relatório (`core/reporting-engine.md`).
2. Ativar módulos por contexto via orquestrador.
3. Executar checklist com evidência obrigatória.
4. Classificar achados por severidade.
5. Calcular score por área e score global.
6. Gerar relatório com formato obrigatório.

## Cobertura completa
O modo `full_audit` ativa todos os módulos e cobre os 17 domínios de auditoria definidos em `orchestrator/full-audit.md`, os mesmos da skill (`SKILL.md`).
