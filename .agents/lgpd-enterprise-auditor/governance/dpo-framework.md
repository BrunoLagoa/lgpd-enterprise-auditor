# Governance Module - DPO Framework

## Escopo
Avaliar governança de privacidade, accountability e controles organizacionais.

## Regulamento do Encarregado (Res. CD/ANPD nº 18/2024)
- A indicação do encarregado deve ser formalizada por **ato escrito, datado e assinado** pelo agente de tratamento.
- O encarregado pode ser **pessoa natural ou pessoa jurídica** (permitindo DPO as a service).
- Devem estar assegurados autonomia técnica, acesso à alta direção e ausência de conflito de interesses.
- **Agentes de tratamento de pequeno porte** (Res. CD/ANPD nº 2/2022) estão dispensados da **indicação formal**, mas não das obrigações de canal de comunicação com titulares e ANPD.
- A identidade e o contato devem ser divulgados de forma clara, objetiva e de fácil acesso, preferencialmente no site.

## Checklist atômico
- Existe DPO/encarregado formalmente designado por ato escrito, datado e assinado (Res. CD/ANPD nº 18/2024)?
- A identidade e o contato do encarregado são divulgados publicamente, de forma clara e objetiva, preferencialmente no site (art. 41, §1º)?
- O encarregado possui autonomia, acesso à alta direção e ausência de conflito de interesses?
- Se o agente é de pequeno porte e não indicou encarregado, existe canal de comunicação alternativo divulgado?
- Existe RIPD para operações de maior risco?
- Existe política de retenção aprovada e aplicada?
- Existe processo de resposta a incidentes com responsáveis definidos e prazo de comunicação à ANPD/titulares de 3 dias úteis (Res. CD/ANPD nº 15/2024)?
- Existe gestão de terceiros com cláusulas de proteção de dados?
- Existe trilha de auditoria e evidência documental contínua?

## Critérios de evidência
- nomeação formal do DPO;
- RIPD(s) atualizados;
- políticas versionadas;
- runbook de incidentes;
- contratos/DPA com operadores e subprocessadores.

## Mapeamento para severidade e score
- Falha de DPO/RIPD em cenário crítico: `ALTO` ou `CRITICO`.
- Encarregado exercendo a função sem ato formal de indicação: `MEDIO`.
- Falhas documentais de baixa materialidade: `BAIXO` ou `MEDIO`.
- Área de scoring primária: `governanca` (15%).

## Relação com outros módulos
- Regulamentos da ANPD aplicáveis: ver [[anpd-guidelines]].
- Obrigações de transparência para público infantojuvenil: ver [[eca-digital]].
