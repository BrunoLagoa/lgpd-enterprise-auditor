# ECA Digital — Estatuto Digital da Criança e do Adolescente (Lei nº 15.211/2025)

## Objetivo
Auditar a conformidade de produtos e serviços de tecnologia da informação direcionados a — ou acessíveis por — crianças e adolescentes no território nacional, conforme a Lei nº 15.211/2025, regulamentada pelo Decreto nº 12.880/2026 e fiscalizada pela ANPD.

Este módulo **complementa**, e não substitui, o art. 14 da LGPD — ver [[children-adolescents]].

## Base normativa
- **Lei nº 15.211/2025** (17/09/2025), em vigor desde **17/03/2026**.
- **Decreto nº 12.622/2025** — atribuiu à ANPD a competência de regulamentar, zelar e fiscalizar a Lei nº 15.211/2025.
- **Decreto nº 12.880/2026** (18/03/2026) — regulamenta a lei e institui a Política Nacional de Promoção e Proteção dos Direitos da Criança e do Adolescente no Ambiente Digital.
- **Lei nº 15.352/2026** — transformou a ANPD em agência reguladora, em grande medida por causa das novas atribuições do ECA Digital — ver [[anpd-guidelines]].
- Orientações preliminares da ANPD sobre mecanismos confiáveis de aferição de idade (março/2026) e Radar Tecnológico nº 5 (aferição de idade).

## Quando se aplica
Ativar o módulo quando **qualquer** condição for verdadeira:
- o produto/serviço é direcionado a crianças (até 12 anos incompletos) ou adolescentes;
- o produto/serviço é **provavelmente acessado** por menores, ainda que não direcionado (rede social, plataforma de vídeo, jogo, marketplace, app de mensagens, fórum);
- há criação de conta por usuários menores de 18 anos;
- há jogos eletrônicos, itens virtuais pagos ou monetização por engajamento;
- há publicidade, recomendação algorítmica ou perfilamento sobre base de usuários que inclua menores.

Provedor estrangeiro alcançado pela lei deve manter **representante legal no Brasil** com poderes para receber citações, intimações e notificações judiciais e administrativas.

## Obrigações auditáveis

### 1. Aferição de idade
- Mecanismo **confiável** de verificação de idade; **autodeclaração simples é insuficiente**.
- Dados coletados para aferição de idade têm **finalidade exclusiva** de verificação — reutilizá-los para marketing, perfilamento ou treinamento de modelo viola a finalidade (art. 6º, I, LGPD).
- O mecanismo deve ser proporcional e minimizador: preferir prova de faixa etária a coleta de documento completo; evitar retenção do artefato de verificação.
- Ver [[age-assurance-checklist]] para o roteiro detalhado de evidências.

### 2. Vinculação a responsável e supervisão parental
- Menores de 16 anos só podem acessar redes sociais com conta **vinculada à de um responsável legal**.
- Devem existir ferramentas de supervisão parental para tempo de uso, contatos e conteúdos acessados.
- A vinculação deve ser verificável — vínculo autodeclarado sem confirmação não constitui evidência.

### 3. Privacidade e configuração por padrão
- Perfis de menores devem nascer com a configuração **mais protetiva por padrão** (privacidade por padrão, art. 6º, VIII e art. 46 da LGPD).
- Geolocalização, descoberta por estranhos e exposição pública de conteúdo devem estar desativadas por padrão.

### 4. Publicidade e perfilamento
- Vedado usar dados ou **perfis emocionais/comportamentais** de menores para fins publicitários.
- Vedado impulsionamento de conteúdo que retrate menores de forma erotizada.
- Publicidade dirigida a criança segue também o CDC e a Resolução Conanda nº 163/2014.

### 5. Jogos eletrônicos e monetização
- Vedadas **caixas-surpresa (loot boxes) pagas** sem revelação prévia do conteúdo.
- Mecânicas de engajamento compulsório dirigidas a menores devem ser avaliadas como risco de design.

### 6. Moderação, notificação e remoção
- Dever de remover conteúdo de abuso e exploração sexual, cyberbullying, indução à automutilação e ao suicídio.
- **Retenção mínima de 6 meses** dos dados relacionados para fins de investigação.
- Deve existir canal de denúncia acessível e rastreável, com prazo e trilha de tratamento.

### 7. Relatório semestral de transparência
- Obrigatório para provedores com **mais de 1 milhão de usuários menores de 18 anos registrados**.
- Publicação **no próprio site** do provedor, em periodicidade **semestral**, com dados de moderação, denúncias, riscos identificados e medidas adotadas.
- **Primeiro relatório: até 17/09/2026**, cobrindo 01/01 a 30/06/2026 (ou 17/03 a 30/06/2026 para provedores sem dados de janeiro e fevereiro).
- Ver [[eca-transparency-report-template]].

## Regime sancionatório (art. 35 da Lei nº 15.211/2025)
- advertência, com prazo de até **30 dias** para adoção de medidas corretivas;
- multa simples de até **10% do faturamento do grupo no Brasil** no último exercício ou, na ausência de faturamento, de **R$ 10,00 a R$ 1.000,00 por usuário registrado**, limitada a **R$ 50.000.000,00 por infração**;
- proibição do exercício das atividades.
- Suspensão de serviço exige decisão judicial. Filiais no Brasil de empresas estrangeiras respondem solidariamente pelo pagamento das multas.
- A dosimetria considera gravidade, reincidência, boa-fé e adoção de medidas corretivas após notificação.

Esse regime é **cumulativo e independente** das sanções do art. 52 da LGPD — a mesma falha pode gerar dupla exposição.

## Cronograma regulatório da ANPD (referência de exigibilidade)
| Etapa | Período | O que ocorre |
|---|---|---|
| I | mar/2026 → | orientações preliminares, monitoramento de lojas de apps e SO (Apple, Google, Microsoft), tomadas de subsídios |
| II | ago/2026 → nov/2026 | parâmetros normativos de aferição de idade, prioridades de monitoramento, período de adaptação |
| III | jan/2027 → | fiscalização efetiva conforme Mapa de Temas Prioritários (Res. CD/ANPD nº 30/2025) |

A lei **já é exigível desde 17/03/2026**; o cronograma acima descreve a postura de fiscalização, não uma suspensão de vigência. Nunca classificar um requisito como dispensado por estar em etapa de adaptação.

## Checklist atômico
- Há usuários menores de 18 anos (registrados ou prováveis) na base?
- Existe mecanismo confiável de aferição de idade, além da autodeclaração?
- Os dados de aferição de idade são usados exclusivamente para essa finalidade e descartados depois?
- Contas de menores de 16 anos estão vinculadas a responsável legal verificado?
- Existem ferramentas de supervisão parental efetivas (tempo, contatos, conteúdo)?
- As configurações de privacidade de perfis de menores são protetivas por padrão?
- Há vedação técnica ao uso de dados/perfis de menores para publicidade e perfilamento?
- Jogos e itens virtuais respeitam a vedação a caixas-surpresa pagas sem revelação prévia?
- Existe fluxo de denúncia, moderação e remoção de conteúdo, com retenção mínima de 6 meses?
- O provedor atinge o limiar de 1 milhão de menores registrados? Se sim, o relatório semestral foi publicado no prazo?
- Provedor estrangeiro possui representante legal no Brasil formalmente constituído?

## Mapeamento para severidade e score
- Ausência de mecanismo de aferição de idade em serviço acessível a menores: `CRITICO`.
- Uso de dados ou perfis de menores para publicidade/perfilamento: `CRITICO`.
- Conta de menor de 16 anos em rede social sem vinculação a responsável: `CRITICO`.
- Ausência de fluxo de remoção de conteúdo de abuso sexual/automutilação: `CRITICO`.
- Reuso dos dados de aferição de idade para outra finalidade: `ALTO`.
- Ausência de supervisão parental ou de privacidade por padrão: `ALTO`.
- Relatório semestral de transparência não publicado por provedor acima do limiar: `ALTO`.
- Loot box paga sem revelação prévia de conteúdo: `ALTO`.
- Provedor estrangeiro sem representante legal no Brasil: `MEDIO`.
- Áreas de scoring primárias: `bases_legais` (15%), `direitos_titular` (15%) e `governanca` (15%); riscos de exposição de dados de menores contribuem para `seguranca` (25%).

## Regra de fundamentação
Todo `finding` originado neste módulo deve citar **o dispositivo do ECA Digital** e o **correlato na LGPD** (art. 14 e/ou princípios do art. 6º, e art. 46 quando for falha de segurança). Achado sem correlato LGPD explícito quebra o contrato de `finding` em [[auditor-core]].

## Em monitoramento (não vigente — não gera não conformidade)
- Guia orientativo da ANPD sobre aferição de idade atualizado em maio/2026 (Processo nº 00261.003182/2026-47), submetido a tomada de subsídios até 09/07/2026 — parâmetros podem mudar.
- Guia sobre "Fornecedores de produtos ou serviços de tecnologia da informação" (Processo nº 00261.002701/2026-50), tomada de subsídios encerrada em 15/06/2026, aguardando versão final.
- Parâmetros normativos definitivos de aferição de idade previstos para a Etapa II (a partir de agosto/2026).

## Relação com outros módulos
- Art. 14 da LGPD e consentimento parental: ver [[children-adolescents]].
- Base legal e finalidade do tratamento: ver [[legal-bases-engine]].
- Aferição de idade em lojas de aplicativos e SO: ver [[mobile-storage]].
- Recomendação algorítmica e perfilamento por IA: ver [[llm-audit]].
- Governança, DPO e trilha de evidência: ver [[dpo-framework]].
