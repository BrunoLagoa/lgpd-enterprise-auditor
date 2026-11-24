# Relatório de Reauditoria

> Comparação entre duas auditorias do mesmo projeto, usada pelo comando `/lgpd-reaudit`. A nova auditoria é completa e segue `core/reporting-engine.md`; este arquivo define só a comparação, gravada em arquivo próprio. Não muda evidência, severidade, score nem o formato do relatório. As seções abaixo são copiadas para a skill (`SKILL.md`, "REAUDITORIA") por `scripts/update-generated.py`: não citar arquivos do framework nelas.

## Quando usar
Depois de correções, para medir a evolução da adequação: o que foi corrigido, o que piorou, o que segue pendente e quais prazos venceram. Exige um relatório anterior gerado por este auditor (`.md` ou `.html`); sem ele, não há o que comparar e a auditoria é feita da forma comum.

## Relatório anterior
- Procurar o relatório anterior pelos nomes `auditoria-lgpd-*` e `relatorio-auditoria-lgpd*` (ex.: em `docs/lgpd/auditorias/`); com mais de um, propor o de data da análise mais recente e confirmar com o usuário; sem nenhum, pedir o caminho. Como o relatório costuma ficar fora do repositório, perguntar antes de concluir que ele não existe.
- Do `.html`, ler só o JSON do bloco `<script type="application/json" id="lgpd-dados">`. Com `.md` e `.html` da mesma auditoria, vale o `.md`.
- Extrair: data da análise, comando, cenário, versão do framework, módulos ativos, score, classificação com as marcas, cobertura e score por área; de cada item do checklist, o ID, a aplicabilidade, o status e a criticidade; de cada não conformidade, o item, a severidade, o prazo sugerido e o aceite de risco, se houver.
- O relatório anterior é só ponto de comparação: nunca serve de evidência para a nova auditoria.

## Nova auditoria
- Usar o mesmo cenário do relatório anterior, salvo pedido do usuário. O roteamento é refeito, porque o projeto pode ter mudado: entra o módulo cujo gatilho passou a valer, sai o módulo cujo objeto deixou de existir, com a evidência disso.
- O contexto registrado no relatório anterior vale como contexto inferido, a confirmar. Perguntar só o que pode ter mudado desde então (natureza e porte do agente de tratamento, tratamento de alto risco, papel em cada fluxo, novas integrações, novos dados, público menor de 18 anos) e, na mesma rodada, o formato de saída.
- Avaliar todos os itens de novo, com evidência colhida agora, **antes** de abrir a comparação, para que o resultado anterior não influencie a avaliação. Nunca copiar status nem evidência do relatório anterior: um item só fica `CONFORME` com evidência `ENCONTRADA` desta auditoria.
- O relatório novo é completo: as 8 seções e os anexos, no formato escolhido, com a data no nome e sem sobrescrever o anterior. O bloco "Contexto e escopo" registra o relatório anterior usado (arquivo, data da análise e versão do framework).
- Aceite de risco do relatório anterior: listado no comparativo; só passa para o `finding` novo se o usuário confirmar que continua válido e a data de revisão (`review_at`) não tiver passado.

## Comparação item a item
Os itens são pareados pelo ID do catálogo. Achados (`NC-nn`) são renumerados a cada relatório: parear pelo item. Itens extras (`EX-nn`) não têm ID estável: parear pela descrição do controle ou, sem correspondência clara, tratar como novo e como fora desta auditoria.

| Situação | Critério |
|---|---|
| Corrigido | `APLICAVEL` nas duas; antes `NAO_CONFORME` ou `PARCIAL`, agora `CONFORME` |
| Melhorou | `APLICAVEL` nas duas; antes `NAO_CONFORME`, agora `PARCIAL` |
| Piorou | `APLICAVEL` nas duas; antes `CONFORME`, agora `PARCIAL` ou `NAO_CONFORME`, ou antes `PARCIAL`, agora `NAO_CONFORME` |
| Pendente | `APLICAVEL` nas duas, com o mesmo status `NAO_CONFORME` ou `PARCIAL` |
| Mantido conforme | `APLICAVEL` e `CONFORME` nas duas |
| Mudou de aplicabilidade | aplicabilidade diferente nas duas (ex.: `NAO_VERIFICADO` antes, `APLICAVEL` agora), com o status novo e o motivo |
| Novo | sem par no relatório anterior: item novo no catálogo ou de módulo ativado agora |
| Fora desta auditoria | sem par na auditoria nova: módulo não ativado agora ou item retirado do catálogo |

Itens com a mesma aplicabilidade diferente de `APLICAVEL` nas duas auditorias entram só na contagem. Quando o item pareado tem achado nas duas auditorias com severidade diferente (agravante que passou a valer, modulação por porte), registrar a severidade antes e agora.

**Prazos vencidos:** para cada achado do relatório anterior cujo item segue `NAO_CONFORME` ou `PARCIAL`, o vencimento é a data da análise anterior somada ao prazo sugerido (`IMEDIATO` vence na própria data; `30_DIAS`, `90_DIAS` e `180_DIAS` somam os dias) ou, havendo aceite de risco com novo prazo, o `accepted_deadline`. Vencimento anterior à data da nova análise entra na lista de prazos vencidos, com os dias de atraso.

## Score e classificação na comparação
- Score global antes, agora e a variação em pontos; classificação antes e agora, com as marcas (teto por achado crítico, score parcial, escopo direcionado); cobertura antes e agora; não conformidades por severidade antes e agora.
- Score por área antes, agora e a variação, para cada área presente em qualquer das duas auditorias.
- A variação é só a diferença entre os números de cada relatório: nada é recalculado no relatório anterior.

## Comparabilidade
Antes dos números, registrar o que limita a comparação:
- **versões do framework diferentes**: o catálogo, os pesos ou as regras podem ter mudado; listar os itens novos e os fora desta auditoria e avisar que parte da variação pode vir da mudança de versão, não de correções;
- **cenário ou módulos ativos diferentes**: o score global compara escopos diferentes; a comparação por item continua válida nos itens pareados;
- **cobertura diferente**: itens `NAO_VERIFICADO` em uma auditoria e verificados na outra mudam o score sem que nada tenha sido corrigido.

## Arquivo do comparativo
- Gravado em Markdown, qualquer que seja o formato escolhido para o relatório, na mesma pasta e com o mesmo nome base do relatório novo, terminado em `-comparativo.md`.
- Começa com `CONFIDENCIAL — uso interno` e segue as regras de armazenamento do relatório.
- Ordem: identificação das duas auditorias (arquivo, data da análise, comando, cenário, versão do framework); comparabilidade; evolução (score, classificação, cobertura, não conformidades por severidade e contagem de itens por situação); score por área; regressões (itens que pioraram); prazos vencidos; corrigidos; melhoraram; pendentes, da maior para a menor severidade; mudanças de aplicabilidade, novos e fora desta auditoria; aceites de risco do relatório anterior e o que foi feito com cada um.
- Tabelas de itens com as colunas `Item | Antes | Agora | Achado`: `Item` no formato `ID · criticality — texto`, `Antes` e `Agora` com o status (ou a aplicabilidade) e a severidade do achado, quando houver, e `Achado` com o `NC-nn` do relatório novo. A evidência fica só no relatório novo; o comparativo não a repete. Itens mantidos conformes aparecem só na contagem.

## Resposta da reauditoria
Com os arquivos gravados, a resposta em tela traz só: score antes e agora, com a variação; classificação antes e agora; quantos itens foram corrigidos, melhoraram, pioraram e seguem pendentes; os IDs das regressões; os prazos vencidos; o aviso de comparabilidade, se houver; e os caminhos do relatório novo e do comparativo.
