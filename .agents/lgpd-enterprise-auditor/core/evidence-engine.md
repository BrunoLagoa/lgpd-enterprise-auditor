# Núcleo — motor de evidências

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

### Mais de uma evidência por item
Um item ou achado pode reunir várias evidências, de origens diferentes (ex.: prova técnica de que os dados saem do País **e** ausência documental de mecanismo de transferência). O grau (`evidence_type`) continua único e resume a comprovação do controle; a origem pode ser `TECNICA`, `DOCUMENTAL` ou `TECNICA + DOCUMENTAL`; cada evidência é descrita com seu rastro (arquivo e linha, configuração, documento e data).

## Regras de validação
- Cada `check_item` `APLICAVEL` e cada `finding` deve possuir `evidence`, `evidence_type`, `evidence_source` e `evidence_confidence`.
- Item `NAO_APLICAVEL` exige evidência `ENCONTRADA` da inexistência do objeto (ex.: nenhum Dockerfile nem manifesto de orquestração no repositório). Item `NAO_VERIFICADO` não tem grau: registra o que impediu a verificação e o acesso necessário.
- Todo `NAO_CONFORME` deve trazer `evidence_type` `AUSENTE` ou `PARCIAL`.
- O grau mede a comprovação do **controle exigido**, não a prova do problema: quando a análise encontra a violação (ex.: CPF em log), o controle está `AUSENTE` e a descrição cita o que foi encontrado.
- Todo `CONFORME` deve trazer `evidence_type` `ENCONTRADA`.
- Todo `PARCIAL` (status) deve trazer `evidence_type` `PARCIAL`.
- Para achados `CRITICO` e `ALTO`, exigir pelo menos uma evidência `TECNICA` ou `DOCUMENTAL` explícita e rastreável.
- Nunca usar valores de eixos diferentes como se fossem alternativos (ex.: `TECNICA` não substitui `ENCONTRADA`).

## Escala de confiança da evidência (`evidence_confidence`)
- `ALTA`: evidência direta e rastreável do que o item exige — técnica e documental coerentes quando o item pede as duas; ou, em item puramente técnico ou puramente documental, a prova direta (arquivo e linha, configuração de produção, documento vigente).
- `MEDIA`: evidência direta, mas de um lado só quando o item pede os dois (só o código sem confirmação em produção; só o documento sem prova de aplicação).
- `BAIXA`: evidência indireta, incompleta, sem rastro completo ou baseada apenas em declaração do auditado.

Para documento ausente: `ALTA` quando o auditado confirma que não existe ou um arquivo evidencia a lacuna; `MEDIA` quando só não foi localizado no material fornecido; `BAIXA` quando a fonte (ex.: termos do provedor) não chegou a ser examinada.

A confiança não altera status, severidade nem score. Achado `CRITICO` ou `ALTO` com confiança `BAIXA` deve indicar a verificação que elevaria a confiança; ela entra nas verificações pendentes do relatório.

## Critério de bloqueio
Sem evidência rastreável, o item não pode ser classificado como `CONFORME`.
