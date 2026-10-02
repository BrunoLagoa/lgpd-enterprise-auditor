# Auditor Core

## Objetivo
Estabelecer os contratos canônicos da auditoria LGPD Enterprise, garantindo consistência entre módulos especialistas, scoring e relatórios.

## Princípios obrigatórios
- Não assumir conformidade sem evidência.
- Exigir base legal válida para cada operação de tratamento.
- Priorizar minimização, segurança, rastreabilidade e privacy by design/default.
- Avaliar impacto técnico, jurídico, operacional e reputacional.

## Contratos canônicos

### `finding`
Estrutura mínima para cada não conformidade:
- `id`: identificador único.
- `module`: módulo origem (ex.: `cloud`, `ai-llm`).
- `title`: título objetivo.
- `problem`: descrição objetiva do problema.
- `severity`: `CRITICO | ALTO | MEDIO | BAIXO`.
- `lgpd_article`: artigo(s) aplicáveis da LGPD.
- `evidence_type`: grau de comprovação - `ENCONTRADA | PARCIAL | AUSENTE`.
- `evidence_source`: origem da evidência - `TECNICA | DOCUMENTAL`.
- `evidence`: evidência observada.
- `technical_impact`: impacto técnico.
- `legal_impact`: impacto jurídico/regulatório.
- `recommendation`: ação recomendada.
- `owner`: responsável sugerido.
- `deadline_suggestion`: `IMEDIATO | 30_DIAS | 90_DIAS | 180_DIAS`.

### `check_item`
Estrutura mínima de checklist:
- `id`: identificador único.
- `domain`: domínio (ex.: `consentimento`, `apis`).
- `item`: requisito validado.
- `status`: `CONFORME | PARCIAL | NAO_CONFORME`.
- `evidence`: evidência associada.
- `evidence_type`: `ENCONTRADA | PARCIAL | AUSENTE`.
- `evidence_source`: `TECNICA | DOCUMENTAL`.
- `impact`: impacto caso falha.
- `recommendation`: correção sugerida.

### `module_output`
Resultado padrão por módulo:
- `module`: nome do módulo.
- `coverage`: percentual de cobertura de itens aplicáveis.
- `check_items`: lista de `check_item`.
- `findings`: lista de `finding`.
- `score_partial`: score parcial do módulo (0-100).
- `gaps`: itens obrigatórios ausentes.
- `recommendations`: recomendações priorizadas.

## Fluxo mínimo de execução
1. Identificar stack, arquitetura e integrações.
2. Ativar módulos por contexto via orquestrador.
3. Executar checklist com evidência obrigatória.
4. Classificar achados por severidade.
5. Calcular score por área e score global.
6. Gerar relatório com formato obrigatório.

## Cobertura completa
O modo `full_audit` ativa todos os módulos e cobre os 17 domínios de auditoria definidos em `orchestrator/full-audit.md`, os mesmos da skill (`SKILL.md`).
