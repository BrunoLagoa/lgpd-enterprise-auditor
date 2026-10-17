# Relatório Técnico

> Visão por público do relatório canônico definido em `core/reporting-engine.md`. Não substitui as 8 seções obrigatórias, que continuam sendo entregues na ordem canônica.
> Como o relatório canônico, é **confidencial**: começa com `CONFIDENCIAL — uso interno` e termina com o aviso legal de `core/reporting-engine.md`.

## 1. Contexto técnico
- arquitetura:
- stack:
- integrações:
- módulos ativados:
- papel do auditado por fluxo de dados (controlador, operador ou ambos):

## 2. Checklist de conformidade
Uma tabela por área de score (mapa por domínio de `core/scoring-engine.md`), com a área no título:

| Item | Status | Evidência | Achado |
|---|---|---|---|
|  |  |  |  |

Preencher `Item` como `ID · criticality · control_type — texto do item` (ex.: `SE-03 · ALTO · TECNICO — …`), `Evidência` como `GRAU (ORIGEM), confiança NIVEL: descrição`, conforme `core/evidence-engine.md`, e `Achado` com o ID da não conformidade (`NC-nn`) ou `—`. As tabelas listam só itens `APLICAVEL`; impacto e correção ficam na seção 3.

### Itens fora do cálculo
| Item | Área | Aplicabilidade | Justificativa ou acesso necessário |
|---|---|---|---|
|  |  |  |  |

`NAO_APLICAVEL` (inexistência comprovada ou obrigação de outro agente) e `NAO_VERIFICADO` (fora do alcance do auditor), conforme `core/scoring-engine.md`.

## 3. Não conformidades detalhadas
Para cada achado:
- problema;
- severidade;
- fundamento LGPD;
- impacto técnico;
- impacto jurídico;
- evidência (com `evidence_type`, `evidence_source` e `evidence_confidence`);
- correção recomendada, com esforço (`P | M | G`);
- modulação de severidade e aceite de risco, quando houver.

## 4. Riscos técnicos e operacionais
- riscos técnicos:
- riscos operacionais:
