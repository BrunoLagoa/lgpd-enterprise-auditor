# Dados de Crianças e Adolescentes (art. 14, LGPD)

## Objetivo
Padronizar a avaliação do tratamento de dados pessoais de crianças (até 12 anos incompletos) e adolescentes, que recebem proteção reforçada.

## Regras legais (art. 14)
- O tratamento deve ser realizado sempre no **melhor interesse** da criança e do adolescente.
- Dados de **crianças** exigem **consentimento específico e em destaque de pelo menos um dos pais ou responsável legal** (art. 14, §1º).
- O controlador deve **manter pública** a informação sobre os tipos de dados coletados, a forma de utilização e os procedimentos para exercício de direitos (art. 14, §2º).
- Não condicionar a participação em jogo/aplicação/atividade ao fornecimento de dados além do necessário (art. 14, §4º).
- Esforços razoáveis para verificar que o consentimento foi dado pelo responsável, consideradas as tecnologias disponíveis (art. 14, §5º).

## Relação com o ECA Digital (Lei nº 15.211/2025)
Desde **17/03/2026** o art. 14 da LGPD convive com o **Estatuto Digital da Criança e do Adolescente**, que impõe obrigações próprias e regime sancionatório autônomo a provedores de produtos e serviços de TI acessíveis a menores.

- Sempre que este módulo identificar público infantojuvenil, **ativar também** [[eca-digital]].
- A LGPD trata da **licitude do tratamento** (base legal, finalidade, consentimento parental); o ECA Digital trata do **desenho e da operação do serviço** (aferição de idade, supervisão parental, moderação, publicidade, transparência).
- Um achado pode violar as duas normas ao mesmo tempo — nesse caso, citar ambos os fundamentos no `finding`.
- Autodeclaração de idade deixou de ser aceitável como mecanismo de verificação: é insuficiente perante o ECA Digital e fragiliza os "esforços razoáveis" do art. 14, §5º.

## Checklist atômico
- Há público infantojuvenil entre os titulares (ou o serviço é direcionado/atrativo a menores)?
- Existe mecanismo de verificação de idade confiável (não apenas autodeclaração)?
- O consentimento parental é coletado, específico e em destaque?
- A coleta respeita a minimização (não exige dados além do necessário)?
- As informações sobre tratamento estão públicas e acessíveis?

## Mapeamento para severidade e score
- Tratamento de dado de criança sem consentimento parental: `CRITICO`.
- Ausência de verificação de idade em serviço com público infantil: `ALTO` pela LGPD e `CRITICO` quando o serviço estiver no escopo do ECA Digital.
- Área de scoring primária: `bases_legais` e `direitos_titular`.

## Relação com outros módulos
- Obrigações do ECA Digital (aferição de idade, supervisão parental, transparência): ver [[eca-digital]].
- Consentimento granular: ver [[legal-bases-engine]].
- Direitos do titular exercidos por responsável: ver [[rights-of-data-subject]].
