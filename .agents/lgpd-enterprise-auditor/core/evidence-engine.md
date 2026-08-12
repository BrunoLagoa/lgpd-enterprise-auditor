# Evidence Engine (V2)

## Objetivo
Padronizar a classificação de evidências para impedir conclusões sem comprovação e suportar auditoria rastreável.

## Eixos de classificação
A evidência é classificada em dois eixos independentes e obrigatórios.

### Eixo 1 - grau de comprovação (`evidence_type`)
- `ENCONTRADA`: implementação comprovada de forma clara.
- `PARCIAL`: implementação incompleta ou sem cobertura total.
- `AUSENTE`: não foi possível comprovar implementação.

### Eixo 2 - origem da evidência (`evidence_source`)
- `TECNICA`: evidência oriunda de código, logs, arquitetura, configuração.
- `DOCUMENTAL`: evidência oriunda de política, contrato, processo e registro.

Quando `evidence_type` for `AUSENTE`, registrar em `evidence_source` a origem onde a evidência era esperada e não foi encontrada.

## Regras de validação
- Cada `check_item` e cada `finding` deve possuir `evidence`, `evidence_type` e `evidence_source`.
- Todo `NAO_CONFORME` deve trazer `evidence_type` `AUSENTE` ou `PARCIAL`.
- Todo `CONFORME` deve trazer `evidence_type` `ENCONTRADA`.
- Todo `PARCIAL` (status) deve trazer `evidence_type` `PARCIAL`.
- Para achados `CRITICO` e `ALTO`, exigir pelo menos uma evidência `TECNICA` ou `DOCUMENTAL` explícita e rastreável.
- Nunca usar valores de eixos diferentes como se fossem alternativos (ex.: `TECNICA` não substitui `ENCONTRADA`).

## Escala de confiança da evidência
- `ALTA`: evidência técnica + documental coerentes.
- `MEDIA`: apenas técnica ou apenas documental.
- `BAIXA`: evidência indireta, incompleta ou sem rastreio completo.

## Critério de bloqueio
Sem evidência rastreável, o item não pode ser classificado como `CONFORME`.
