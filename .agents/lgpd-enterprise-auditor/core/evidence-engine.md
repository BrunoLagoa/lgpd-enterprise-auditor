# Evidence Engine (V2)

## Objetivo
Padronizar a classificação de evidências para impedir conclusões sem comprovação e suportar auditoria rastreável.

## Tipos de evidência
- `ENCONTRADA`: implementação comprovada de forma clara.
- `PARCIAL`: implementação incompleta ou sem cobertura total.
- `AUSENTE`: não foi possível comprovar implementação.
- `TECNICA`: evidência oriunda de código, logs, arquitetura, configuração.
- `DOCUMENTAL`: evidência oriunda de política, contrato, processo e registro.

## Regras de validação
- Cada `check_item` deve possuir pelo menos uma evidência.
- Todo `NAO_CONFORME` deve trazer evidência `AUSENTE` ou `PARCIAL`.
- Todo `CONFORME` deve trazer evidência `ENCONTRADA`.
- Para achados críticos e altos, exigir pelo menos uma evidência técnica ou documental explícita.

## Escala de confiança da evidência
- `ALTA`: evidência técnica + documental coerentes.
- `MEDIA`: apenas técnica ou apenas documental.
- `BAIXA`: evidência indireta, incompleta ou sem rastreio completo.

## Critério de bloqueio
Sem evidência rastreável, o item não pode ser classificado como `CONFORME`.
