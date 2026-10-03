# Governance Module - DPO Framework

## Escopo
Avaliar governança de privacidade, accountability e controles organizacionais.

## Regulamento do Encarregado (Res. CD/ANPD nº 18/2024)
- A indicação do encarregado deve ser formalizada por **ato escrito, datado e assinado** pelo agente de tratamento.
- O encarregado pode ser **pessoa natural ou pessoa jurídica** (permitindo DPO as a service).
- Devem estar assegurados autonomia técnica, acesso à alta direção e ausência de conflito de interesses.
- **Agentes de tratamento de pequeno porte** (Res. CD/ANPD nº 2/2022) estão dispensados da **indicação formal**, mas não das obrigações de canal de comunicação com titulares e ANPD. A dispensa não vale para quem se enquadra nas exclusões da resolução, como o tratamento de alto risco (art. 3º).
- A identidade e o contato devem ser divulgados de forma clara, objetiva e de fácil acesso, preferencialmente no site.

## Registro das operações de tratamento (art. 37)
- Controlador e operador devem manter registro das operações de tratamento que realizarem (art. 37). É a base do mapeamento de dados.
- Conteúdo mínimo esperado: inventário e classificação dos dados (comum, sensível, de criança/adolescente), finalidade, base legal (art. 7º ou 11), categorias de titulares, compartilhamentos e transferências internacionais, retenção/descarte e medidas de segurança.
- Agentes de tratamento de pequeno porte podem cumprir a obrigação de forma **simplificada** (Res. CD/ANPD nº 2/2022), mas não estão dispensados dela; a forma simplificada também não vale nas exclusões da resolução, como o tratamento de alto risco (art. 3º).

## Retenção e eliminação (arts. 15 e 16)
- O tratamento termina quando a finalidade é alcançada ou os dados deixam de ser necessários, ao fim do período de tratamento, por comunicação do titular (inclusive revogação) ou por determinação da ANPD (art. 15).
- Terminado o tratamento, os dados devem ser eliminados; a conservação só é autorizada para cumprimento de obrigação legal ou regulatória, estudo por órgão de pesquisa (anonimizados sempre que possível), transferência a terceiro respeitados os requisitos de tratamento, ou uso exclusivo do controlador com dados anonimizados e vedado o acesso por terceiro (art. 16).

## Checklist atômico
- Existe registro das operações de tratamento (art. 37) atualizado, com inventário e classificação de dados, ciclo de vida, compartilhamentos e retenção, sem dados órfãos (sem finalidade ou responsável)?
- Existe DPO/encarregado formalmente designado por ato escrito, datado e assinado (Res. CD/ANPD nº 18/2024)?
- A identidade e o contato do encarregado são divulgados publicamente, de forma clara e objetiva, preferencialmente no site (art. 41, §1º)?
- O encarregado possui autonomia, acesso à alta direção e ausência de conflito de interesses?
- Se o agente é de pequeno porte e não indicou encarregado, existe canal de comunicação alternativo divulgado?
- Existe RIPD para operações de maior risco?
- Existe política de retenção aprovada e aplicada, com prazo por categoria de dado e a hipótese do art. 16 que justifica cada conservação?
- A eliminação ou anonimização ao fim do prazo é automática e alcança réplicas, backups e operadores?
- O descarte de dados e mídias é seguro e registrado?
- Retenções legais (ex.: fiscais, trabalhistas, registros de acesso do MCI art. 15) estão identificadas e limitadas ao prazo legal?
- Existe processo de resposta a incidentes com responsáveis definidos e prazo de comunicação à ANPD/titulares de 3 dias úteis (Res. CD/ANPD nº 15/2024)?
- Existe gestão de terceiros com cláusulas de proteção de dados?
- Se o auditado é provedor de aplicações de internet: há sede e representante legal pessoa jurídica no País, com contato acessível no site, e canal de denúncia permanente de fácil acesso (Decreto nº 8.771/2016, art. 16-A, com a redação do Decreto nº 12.975/2026)? Ver [[plataformas-digitais]].
- Existe trilha de auditoria e evidência documental contínua?

## Critérios de evidência
- registro das operações de tratamento versionado;
- política de retenção e evidência de execução da eliminação (jobs de expurgo, logs de descarte);
- nomeação formal do DPO;
- RIPD(s) atualizados;
- políticas versionadas;
- runbook de incidentes;
- contratos/DPA com operadores e subprocessadores.

## Mapeamento para severidade e score
- Ausência de encarregado (quando exigível) ou de RIPD em tratamento de alto risco (critérios da Res. CD/ANPD nº 2/2022): `ALTO`; demais falhas de encarregado ou RIPD: `MEDIO`.
- Posição do framework sobre o RIPD: embora o art. 38 o torne exigível quando a ANPD o solicita, a ausência em tratamento de alto risco é `ALTO`, porque o relatório precisa estar pronto para ser apresentado e é a principal evidência de gestão de risco.
- Ausência de processo de resposta a incidentes que permita comunicar ANPD e titulares em 3 dias úteis: `ALTO`.
- Operador sem contrato com cláusulas de proteção de dados (DPA), inclusive o provedor de hospedagem: `MEDIO`; `ALTO` se o operador tratar dados sensíveis ou de crianças e adolescentes.
- Provedor de aplicações sem os deveres gerais do art. 16-A (representante legal, canal de denúncia): aplicar o mapeamento de severidade de `legal/plataformas-digitais.md`, mesmo com aquele módulo inativo.
- Ausência de registro das operações de tratamento (art. 37): `MEDIO`; `ALTO` quando houver tratamento de dados sensíveis ou de crianças e adolescentes.
- Encarregado exercendo a função sem ato formal de indicação: `MEDIO`.
- Retenção sem prazo definido ou sem fundamento no art. 16 (retenção obscura): `MEDIO`.
- Falhas documentais de baixa materialidade: `BAIXO` ou `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `governanca` (domínios 1, 13, 14 e 15) para todos os itens deste módulo.

## Relação com outros módulos
- Regulamentos da ANPD aplicáveis: ver [[anpd-guidelines]].
- Obrigações de transparência para público infantojuvenil: ver [[eca-digital]].
- Deveres de provedores de aplicações de internet (representante legal, canal de denúncia, relatório anual de transparência): ver [[plataformas-digitais]].
