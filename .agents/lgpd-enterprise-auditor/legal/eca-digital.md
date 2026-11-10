# ECA Digital — Estatuto Digital da Criança e do Adolescente (Lei nº 15.211/2025)

## Objetivo
Auditar a conformidade de produtos e serviços de tecnologia da informação direcionados a — ou de acesso provável por — crianças e adolescentes no País, conforme a Lei nº 15.211/2025, regulamentada pelo Decreto nº 12.880/2026 e fiscalizada pela ANPD.

Este módulo **complementa**, e não substitui, o art. 14 da LGPD — ver [[children-adolescents]].

Referências de artigo verificadas no texto oficial (Planalto): a lei em 2026-08 e o Decreto nº 12.880/2026 em 2026-11.

## Base normativa
- **Lei nº 15.211/2025** (17/09/2025). Vigência: **17/03/2026** (art. 41-A, com a redação da Lei nº 15.352/2026).
- **Decreto nº 12.622/2025** — atribuiu à ANPD a competência de regulamentar, zelar e fiscalizar a Lei nº 15.211/2025.
- **Decreto nº 12.880/2026** (18/03/2026) — regulamenta a lei e institui a Política Nacional de Promoção e Proteção dos Direitos da Criança e do Adolescente no Ambiente Digital.
- **Despacho Decisório CD/ANPD nº 122/2026** (DOU 11/08/2026) — fixa o prazo, o período de referência, o conteúdo mínimo e as dispensas do relatório semestral de transparência do art. 31 até regulamentação específica.
- Normas conexas citadas pela própria lei: ECA (Lei nº 8.069/1990), LGPD (Lei nº 13.709/2018), CDC (Lei nº 8.078/1990), Marco Civil da Internet (Lei nº 12.965/2014), Marco Legal dos Jogos Eletrônicos (Lei nº 14.852/2024) e Estatuto da Pessoa com Deficiência (Lei nº 13.146/2015).
- **Guia Orientativo da ANPD "Fornecedores de produtos ou serviços de tecnologia da informação: escopo e obrigações gerais do ECA Digital"** (versão 1.0, 28/10/2026) — orientativo: fixa a interpretação da ANPD sobre quem está no escopo da lei e é a referência das perguntas de enquadramento deste módulo. Nunca fundamenta `finding` ou `NAO_CONFORME`: o achado cita a lei ou o decreto.
- Orientações preliminares da ANPD sobre aferição de idade (março/2026) e Radar Tecnológico nº 5 — **não vinculantes**: servem de referência técnica, mas nunca fundamentam `finding` ou `NAO_CONFORME`.
- Nota Técnica da Sedigi/MJSP sobre companheiros de IA acessíveis a crianças e adolescentes (22/09/2026), encaminhada à ANPD e à Senacon — preliminar e **não vinculante**: referência para sistemas conversacionais que simulam vínculo afetivo (aferição de idade só por autodeclaração, perfilamento emocional para publicidade e coleta de dados íntimos foram os indícios apontados) — ver [[llm-audit]].

## Escopo de aplicação (art. 1º)
A lei alcança **todo produto ou serviço de TI direcionado a crianças e adolescentes no País ou de acesso provável por eles**, independentemente de onde seja desenvolvido, fabricado, ofertado ou operado.

**Produto ou serviço de TI** (art. 2º, I) é o fornecido à distância, por meio eletrônico e por requisição individual do usuário — os três elementos juntos. Exemplos da lei: aplicações de internet, softwares, **sistemas operacionais de terminais**, **lojas de aplicativos** e jogos eletrônicos conectados. O critério é funcional: marketplaces, mensageria e dispositivos conectados entram quando atendem aos três elementos, e a gratuidade para o usuário não afasta a lei. Ficam fora o serviço prestado com presença física das partes, a radiodifusão, o telemarketing e as funcionalidades essenciais ao funcionamento da internet (art. 2º, §2º).

**Serviço direcionado** é o que o próprio fornecedor declara voltado a crianças e adolescentes (termos de uso, descrição, comunicação).

**Acesso provável** (art. 1º, parágrafo único) exige os três requisitos **ao mesmo tempo**:
1. suficiente probabilidade de uso e atratividade para crianças e adolescentes;
2. considerável facilidade de acesso e utilização por eles;
3. significativo grau de risco à privacidade, à segurança ou ao desenvolvimento biopsicossocial — presumido em serviços de interação social e compartilhamento em larga escala.

### Regras de enquadramento
Entendimento fixado no Guia Orientativo da ANPD (versão 1.0, 28/10/2026), com base na lei e no Decreto nº 12.880/2026:

- **Categorias com presunção de acesso provável ou direcionamento** — nelas o teste dos três requisitos é dispensado e o módulo se aplica: redes sociais; lojas de aplicativos; sistemas operacionais; serviços com controle editorial; jogos eletrônicos; provedores de conteúdo adulto; **sistemas de IA generativa** (geração de conteúdo e interação em linguagem natural, como modelos de linguagem e agentes conversacionais — Decreto, art. 11); comércio eletrônico que venda ou intermedeie produtos e serviços proibidos a menores (Decreto, art. 18).
- A presunção só é afastada com fundamentação nas características concretas do serviço que mostre a ausência de um dos três requisitos (ex.: agente conversacional restrito a funcionários de uma empresa). Registrar a fundamentação no escopo excluído.
- **Nenhuma medida de cumprimento afasta o enquadramento**: aferição de idade, por mais robusta, e medidas de mitigação de risco são cumprimento da lei, avaliado nos itens, e não motivo para deixar de aplicar o módulo.
- Declaração de público adulto, termos de uso que proíbem menores e a autoavaliação do fornecedor **não decidem** o enquadramento: vale o funcionamento concreto do serviço, e a ANPD pode determinar enquadramento diverso (Decreto, arts. 16, §3º e 19, §2º).
- Fora das categorias presumidas, estes indícios ajudam a avaliar os três requisitos, sem substituí-los: conteúdo ou produto de interesse de crianças e adolescentes; design atrativo a esse público (personagens, gamificação, recompensas, rankings, influenciadores); publicidade voltada a eles; semelhança com serviço das categorias presumidas; uso efetivo por menores, segundo dados da plataforma ou pesquisas. Recursos de acessibilidade e boa usabilidade, sozinhos, não são indício.
- Na dúvida, prevalece o melhor interesse da criança e do adolescente (art. 5º, §2º): aplicar o módulo e registrar a incerteza.

**Proporcionalidade e dispensa (art. 39)**: as obrigações dos arts. 6º, 17, 18, 19, 20, 27, 28, 29, 31, 32 e 40 são moduladas pelo grau de interferência do fornecedor sobre o conteúdo, número de usuários e porte. Serviços **com controle editorial** e provedores de conteúdo licenciado ficam dispensados desses artigos se cumprirem classificação indicativa, transparência etária, mediação parental e canal de denúncias (art. 39, §1º). Esses provedores, e os de conteúdo musical ou literário, também ficam dispensados de aferir idade se oferecerem contas ou perfis infantis com conteúdo adequado à faixa etária e supervisão parental com bloqueio ou restrição de acesso; conteúdo jornalístico e esportivo sob controle editorial, não sujeito à classificação indicativa, é dispensado sem condição (Decreto, art. 22). A dispensa não alcança a configuração mais protetiva por padrão (art. 7º) nem as demais obrigações. Verificar essas hipóteses antes de emitir achado — evita falso positivo.

## Obrigações auditáveis

### 1. Prevenção e mitigação de riscos de conteúdo (art. 6º)
Medidas razoáveis, desde a concepção e ao longo da operação, contra acesso, exposição, recomendação ou facilitação de contato com:
- exploração e abuso sexual (I);
- violência física, intimidação sistemática virtual e assédio (II);
- indução a danos à saúde física ou mental — substâncias, autodiagnóstico/automedicação, automutilação e suicídio (III);
- jogos de azar, apostas de quota fixa, loterias, tabaco, álcool, narcóticos e produtos de venda proibida a menores (IV);
- práticas publicitárias predatórias, injustas ou enganosas e outras que causem dano financeiro (V);
- conteúdo pornográfico (VI).

Inclui política antibullying com apoio às vítimas e programas educativos (art. 6º, §2º).

### 2. Privacidade por padrão (art. 7º)
- Configuração **no modelo mais protetivo disponível** por padrão, desde a concepção.
- Informação clara e acessível para que criança/adolescente e responsáveis façam escolhas informadas ao adotar configurações menos protetivas (§1º).
- Vedado tratamento que cause, facilite ou contribua para violação da privacidade ou de outros direitos, observados os princípios do art. 6º da LGPD (§2º).

### 3. Gestão de risco e classificação indicativa (art. 8º)
- gerenciamento de riscos de recursos, funcionalidades e sistemas (I);
- avaliação do conteúdo por faixa etária compatível com a classificação indicativa (II);
- sistemas que impeçam o encontro com conteúdo ilegal, pornográfico ou inadequado (III);
- **configurações por padrão que evitem o uso compulsivo** (IV) — o Decreto nº 12.880/2026, art. 9º, parágrafo único, nomeia os mecanismos de incentivo ao uso excessivo: ocultação de pontos naturais de parada, acionamento de novos conteúdos sem solicitação, recompensa por tempo de uso e notificações excessivas;
- informação extensiva da faixa etária indicada no momento do acesso (V), com a classificação indicativa informada nos termos de uso, em português e de forma acessível (Decreto, art. 12, §4º).

**Avaliação de impacto à segurança e à saúde** (Decreto, art. 47): todo fornecedor no escopo deve realizá-la, com identificação e análise dos riscos, probabilidade e gravidade do impacto, tratamento e mitigação e acompanhamento contínuo da efetividade das medidas, e **dar publicidade à versão resumida** em linguagem clara e acessível (§1º). Conteúdo mínimo e periodicidade dependem de ato da ANPD (§2º), ainda não editado; a obrigação de fazer e publicar o resumo já vale.

**IA generativa e agentes conversacionais** (Decreto, art. 11): o fornecedor de sistema capaz de gerar conteúdo e interagir em linguagem natural deve ser transparente com crianças e adolescentes quanto ao caráter sintético e automatizado da interação (I), prevenir a manipulação comportamental (II), avaliar o risco algorítmico à segurança e à saúde (III) e implementar salvaguardas ao desenvolvimento físico, mental e psicossocial (IV). A interação automatizada de teor sexualmente explícito equipara-se a conteúdo pornográfico (art. 16, §4º).

### 4. Bloqueio de conteúdo impróprio e verificação de idade (art. 9º)
- Quem oferta conteúdo/produto/serviço impróprio, inadequado ou proibido a menores de 18 anos deve adotar **medidas eficazes** para impedir o acesso.
- **Mecanismos confiáveis de verificação de idade a cada acesso, vedada a autodeclaração** (§1º).
- Provedores com conteúdo pornográfico devem impedir a criação de contas/perfis por crianças e adolescentes (§3º).
- O Decreto nº 12.880/2026 detalha: conteúdo impróprio ou inadequado depende, cumulativamente, de classificação indicativa, segurança por padrão e supervisão parental com bloqueio configurável (art. 14); conteúdo, produto ou serviço **proibido** — a lista do art. 15, §1º: armas, bebidas alcoólicas, fumígenos e cigarros eletrônicos, produtos que causem dependência, fogos, jogos de azar e apostas, caixas de recompensa, pornografia, serviços de acompanhantes e aplicações de encontros de cunho sexual — exige verificação de idade eficaz e impedimento efetivo do acesso (art. 15); nos casos de apostas, caixas de recompensa, pornografia, acompanhantes e encontros, também vedar a criação de contas por menores e remover as que eles operem (art. 15, §2º).
- Conteúdo pornográfico: verificação de idade própria, inclusive para prévias, imagens, títulos e legendas (Decreto, art. 16, §1º); para usuário não cadastrado, sem idade verificada ou menor, ocultar ou desfocar por padrão, ou exigir verificação de idade sem autodeclaração (art. 17). Obras de contexto educativo, artístico, informativo ou jornalístico, livros sem imagens e áudio não se enquadram (art. 16, §2º).
- **Venda ou intermediação de produtos e serviços proibidos** (Decreto, art. 18; lista do art. 15, §1º, I a VII): verificação de idade efetiva no cadastro, com bloqueio da compra por padrão e sem desbloqueio por autodeclaração, ou na aquisição, impedindo a conclusão por menor; usuário não cadastrado ou não autenticado fica bloqueado.
- Rede social com conteúdo proibido: versão sem esse conteúdo e sem a publicidade correspondente — única opção para usuário não cadastrado — ou verificação de idade efetiva, vedada a autodeclaração (Decreto, art. 19).

### 5. Aferição de idade na cadeia (arts. 10 a 15)
- Fornecedores devem adotar mecanismos que proporcionem **experiências adequadas à idade**, respeitadas autonomia progressiva e diversidade socioeconômica (art. 10).
- **Lojas de aplicativos e sistemas operacionais** (art. 12) devem: aferir idade/faixa etária com medidas proporcionais, **auditáveis** e tecnicamente seguras (I); permitir supervisão parental (II); e oferecer **API segura de "sinal de idade"** aos provedores de aplicações, com minimização de dados e vedado compartilhamento contínuo, automatizado e irrestrito (III e §1º).
- Download por menores depende de **consentimento livre e informado do responsável**, vedada presunção por silêncio (art. 12, §2º).
- **Dados coletados para verificação de idade só podem ser usados para essa finalidade** (art. 13) — regra absoluta, sem exceção no texto legal.
- Fornecedores devem adotar medidas técnicas e organizacionais para **receber o sinal de idade** (art. 14) e, independentemente das lojas/SO, manter **mecanismos próprios** de bloqueio (parágrafo único).
- Responsabilidade **solidária** de todos os agentes da cadeia digital (art. 15).
- Decreto nº 12.880/2026: os mecanismos de aferição observam proporcionalidade ao risco, acurácia, minimização, não rastreabilidade, inclusão e auditabilidade (art. 24); **documento coletado para aferir idade não pode ser armazenado** — fica só o dado de idade ou faixa etária, e a imagem ou cópia é eliminada de modo imediato e irreversível (art. 24, §3º); o sinal de idade é gratuito e não leva data de nascimento exata, identidade civil nem dados de perfilamento (art. 25, §1º); lojas e sistemas operacionais permitem contestar a classificação etária, coíbem contas múltiplas e pedem a autorização do responsável informando a classificação indicativa do aplicativo (art. 25, §§2º e 3º), e não disponibilizam aplicativos de loterias ou apostas não autorizadas ou sem verificação de idade (art. 21); se a aferição do fornecedor divergir do sinal recebido, vale a alternativa mais protetiva (art. 25, §4º); serviço acessado pelo navegador afere a idade por conta própria, podendo usar sinais (art. 26, §2º), e receber o sinal não isenta da efetividade da proteção (art. 26, §3º); quem afere idade oferece meio de contestar o resultado (art. 27).

Ver [[age-assurance-checklist]] para o roteiro de evidências.

### 6. Informação, RIPD e supervisão parental (arts. 16 a 18)
- Informações sobre riscos e medidas de segurança acessíveis independentemente da aquisição do produto (art. 16), em conformidade com o art. 14 da LGPD.
- Em tratamento além do estritamente necessário à operação, o controlador deve **mapear riscos** e **elaborar relatório de impacto**, compartilhável mediante requisição da autoridade (art. 16, parágrafo único, I e II) — usar [[ripd-template]].
- Ferramentas de supervisão parental acessíveis, com informação em local de fácil acesso, aviso visível quando ativas e controle de tempo de uso (art. 17, I a IV).
- **Configurações-padrão no mais alto nível de proteção** (art. 17, §4º), assegurando no mínimo: restrição de comunicação por usuários não autorizados; limitação de recursos que estendam artificialmente o uso (autoplay, recompensas por tempo, notificações); ferramentas de acompanhamento; visualização e limitação de tempo; **controle sobre recomendação personalizada, com opção de desativação**; restrição de compartilhamento de geolocalização com aviso prévio; educação midiática; revisão regular de ferramentas de IA com possibilidade de desabilitar funcionalidades não essenciais; conexão a serviços de suporte emocional quando viável.
- As ferramentas devem permitir aos responsáveis (art. 18): gerenciar conta e privacidade; **restringir compras e transações financeiras**; identificar perfis de adultos que se comunicam com o menor; acessar métricas de tempo de uso; ativar/desativar salvaguardas; e ter tudo **em língua portuguesa**.
- **Vedado design manipulativo** (dark patterns) que comprometa a autonomia do usuário ou enfraqueça as salvaguardas (art. 18, §2º). O Decreto nº 12.880/2026, art. 10, parágrafo único, nomeia as práticas: obstrução (caminho complexo ou desproporcional para interromper o uso, cancelar ou mudar preferências), exploração de vulnerabilidades cognitivas (pressão emocional, urgência fabricada, escolha enviesada, estímulo inadequado à idade) e prejuízo ao exercício de direitos (ocultar ou dificultar controles de privacidade, supervisão parental, consentimento ou revogação).

### 7. Monitoramento infantil (art. 19)
Produtos de monitoramento (câmeras, rastreadores, apps de acompanhamento) devem garantir inviolabilidade de imagens, sons e informações captadas e transmitidas, e **informar a criança/adolescente, em linguagem apropriada**, sobre o monitoramento.

### 8. Jogos eletrônicos (arts. 20 e 21)
- **Vedadas as caixas de recompensa (loot boxes)** em jogos direcionados a crianças e adolescentes ou de acesso provável por eles, nos termos da classificação indicativa (art. 20). A definição legal (art. 2º, IV) é: aquisição mediante pagamento de itens ou vantagens aleatórias, sem conhecimento prévio do conteúdo.
- Como cumprir (Decreto nº 12.880/2026, art. 23): o jogo com caixas de recompensa verifica a idade para impedir o acesso de crianças e adolescentes a essa funcionalidade; a verificação é dispensada na versão sem caixas de recompensa ou com a funcionalidade totalmente restrita por padrão.
- Jogos com interação entre usuários devem observar integralmente as salvaguardas do art. 16 da Lei nº 14.852/2024 e, **por padrão, limitar a interação** de modo a assegurar o consentimento dos responsáveis (art. 21).

### 9. Publicidade e perfilamento (arts. 22, 23 e 26)
- **Vedado o perfilamento para direcionamento de publicidade comercial** a crianças e adolescentes, bem como o uso de **análise emocional, realidade aumentada, estendida e virtual** para esse fim (art. 22).
- Vedadas monetização e impulsionamento de conteúdo que retrate menores de forma erotizada, sexualmente sugestiva ou em contexto adulto (art. 23).
- **Vedada a criação de perfis comportamentais** de crianças e adolescentes para publicidade, inclusive a partir de **dados obtidos na verificação de idade** e de dados grupais e coletivos (art. 26).
- Decreto nº 12.880/2026: é abusiva a publicidade que se aproveite da deficiência de julgamento e experiência da criança (art. 31); quem oferta ou distribui publicidade a menores deve impedir o perfilamento e as demais técnicas do art. 22 da lei (art. 33); é vedado veicular, monetizar ou impulsionar conteúdo que exponha crianças ou adolescentes a situações violadoras, vexatórias ou degradantes (art. 35).
- **Conteúdo monetizado ou impulsionado que explore, de forma habitual, a imagem ou a rotina de criança ou adolescente** (Decreto, art. 34): o fornecedor deve exigir do usuário a autorização judicial do art. 149 do ECA e retirar o conteúdo de imediato se ela faltar. Vale para conteúdo cuja monetização ou impulsionamento tenha começado a partir de 16/06/2026 (noventa dias após a publicação do decreto).

### 10. Vinculação de conta e redes sociais (arts. 24 e 25)
- Contas de crianças e adolescentes **de até 16 anos** devem estar **vinculadas à conta de um responsável legal** (art. 24, caput).
- Serviços impróprios a menores devem informar de forma destacada, restringir conteúdo que atraia menores e **aprimorar continuamente a verificação de idade** (art. 24, §1º), com efetividade avaliada pela autoridade (§2º).
- Diante de **fundados indícios** de conta operada por menor, o provedor pode exigir confirmação de identidade — com dados usados exclusivamente para verificação (§3º) — e deve **suspender o acesso**, garantindo procedimento célere de apelação ao responsável (§4º).
- Sem conta de responsável, é vedado reduzir o nível de proteção das configurações de supervisão parental (§5º).
- Regras específicas, concretas e documentadas para tratamento de dados de menores (art. 25).

### 11. Violações graves, notificação e remoção (arts. 27 a 30)
- **Remover e comunicar** conteúdos de aparente exploração, abuso sexual, sequestro e aliciamento às autoridades nacionais e internacionais competentes (art. 27). A comunicação vai ao Centro Nacional de Triagem de Notificações, na Polícia Federal, com remoção imediata e preservação do material, dos dados da conta e dos metadados; confirmado o recebimento, o conteúdo de exploração e abuso sexual é excluído dos servidores e os demais dados são mantidos (Decreto nº 12.880/2026, arts. 36 e 39). Requisitos e prazos dependem de ato do MJSP.
- **Retenção de dados** associados ao relatório — conteúdo, metadados e dados do usuário responsável — pelo prazo do **art. 15 do Marco Civil da Internet (6 meses)**, podendo ser maior mediante requerimento (art. 27, §§2º e 3º).
- Mecanismo de notificação de violações disponível aos usuários e comunicação às autoridades (art. 28), acessível, gratuito, efetivo e amplamente divulgado (Decreto nº 12.880/2026, art. 41).
- **Retirada de conteúdo violador independentemente de ordem judicial**, de imediato e com tratamento prioritário, quando comunicado pela vítima, representantes, Ministério Público, autoridades policiais ou entidades de defesa habilitadas pela ANPD (art. 29; Decreto, arts. 43 e 44). A notificação exige identificação técnica específica do conteúdo e do notificante, **vedada denúncia anônima** (§2º); o mecanismo deve ser público e de fácil acesso (§3º); conteúdo jornalístico e sob controle editorial está fora do procedimento (§4º).
- **Direito de contestação** ao usuário que publicou: notificação da retirada, motivo e fundamentação com indicação de análise humana ou automatizada, recurso, acesso fácil ao mecanismo e prazos definidos (art. 30).

### 12. Transparência e prestação de contas (art. 31)
Obrigatório para provedores de aplicações com **mais de 1.000.000 de usuários nessa faixa etária registrados, com conexão no território nacional**. Relatórios **semestrais, em língua portuguesa, publicados no sítio eletrônico do provedor**, contendo:
1. canais de denúncia e sistemas/processos de apuração;
2. quantidade de denúncias recebidas;
3. quantidade de moderação de conteúdo ou de contas, por tipo;
4. medidas de identificação de contas infantis (art. 24, §3º) e de atos ilícitos (art. 27);
5. aprimoramentos técnicos de proteção de dados e privacidade;
6. aprimoramentos técnicos para aferir consentimento parental (art. 14, §1º, LGPD);
7. métodos e resultados das avaliações de impacto e gestão de riscos.

Parágrafo único: acesso **gratuito** a dados para pesquisa acadêmica, científica, tecnológica, de inovação ou jornalística, vedado uso comercial.

**Primeiro ciclo:** publicação até **17/09/2026**, cobrindo 01/01 a 30/06/2026 — ou 17/03 a 30/06/2026 para provedores sem dados de janeiro e fevereiro. **Prazo encerrado:** desde 18/09/2026, provedor acima do limiar sem relatório publicado está em não conformidade atual. **Ciclos seguintes** (Despacho Decisório CD/ANPD nº 122/2026): semestres civis, com publicação até **1º/02** (julho a dezembro do ano anterior) e **1º/08** (janeiro a junho); o relatório do 2º semestre de 2026 vence em 01/02/2027. Até regulamentação específica, o conteúdo mínimo é um documento único com os sete incisos do art. 31, detalhando as notificações recebidas por categoria e os dados proporcionais sobre o seu prosseguimento (Decreto nº 12.880/2026, art. 45, I e II); ficam dispensados os provedores abaixo do limiar e os serviços com controle editorial ou conteúdo licenciado que atendam ao art. 39, §1º, I a IV. O despacho recomenda enviar cópia do relatório à ANPD no ato da publicação, sem substituir a publicação no site. Ver [[eca-transparency-report-template]].

### 13. Uso abusivo dos instrumentos de denúncia (arts. 32 e 33)
Mecanismos para identificar uso abusivo das denúncias (censura, perseguição), com informação clara aos usuários, sanções internas graduadas, notificação, direito a recurso, prazos e **registros detalhados** dos casos e sanções.

### 14. Representante legal no País (art. 40)
Manter representante legal no Brasil com poderes para receber citações, intimações e notificações e responder perante Judiciário, Ministério Público e administração pública.

### 15. Embalagens de equipamentos (art. 38)
Equipamentos eletrônicos de uso pessoal com acesso à internet comercializados no País devem trazer adesivo em português alertando responsáveis sobre conteúdo impróprio.

Regra transitória (Decreto nº 12.880/2026, art. 50): até a regulamentação da ANPD, a exigência alcança os fabricantes e importadores de equipamentos cuja apresentação, embalagem ou comunicação mercadológica seja **exclusivamente direcionada a crianças e adolescentes**, fabricados ou importados depois de 18/03/2026, com a mensagem: "Este produto permite acesso à internet. Conteúdos da internet podem apresentar riscos a crianças e adolescentes. O uso do produto requer supervisão parental." Fora dessa hipótese, `ECA-22` fica `NAO_APLICAVEL` até a regulamentação.

## Regime sancionatório (art. 35)
| Sanção | Detalhe | Quem aplica |
|---|---|---|
| I — advertência | prazo de até 30 dias para medidas corretivas | ANPD |
| II — multa simples | até **10% do faturamento do grupo econômico no Brasil** no último exercício ou, sem faturamento, **R$ 10,00 a R$ 1.000,00 por usuário cadastrado**, limitada a **R$ 50.000.000,00 por infração** | ANPD |
| III — suspensão temporária das atividades | — | **Poder Judiciário** |
| IV — proibição de exercício das atividades | — | **Poder Judiciário** |

- Dosimetria (§1º): gravidade e extensão do dano individual e coletivo, reincidência, capacidade econômica, finalidade social e impacto no fluxo de informações.
- Empresa estrangeira: filial, sucursal, escritório ou estabelecimento no País **responde solidariamente** pela multa (§2º).
- O rito segue a apuração de infrações administrativas do ECA (§3º); os valores são corrigidos anualmente pelo IPCA (§4º).
- Suspensão e proibição podem ser efetivadas por **ordem de bloqueio** a provedores de conexão, PTTs e serviços de DNS (§6º).

Regime **cumulativo e independente** das sanções do art. 52 da LGPD — a mesma falha pode gerar dupla exposição.

## Cronograma regulatório da ANPD (postura de fiscalização)
| Etapa | Período | O que ocorre |
|---|---|---|
| I | mar/2026 → | orientações preliminares, monitoramento de lojas de apps e SO (Apple, Google, Microsoft), tomadas de subsídios |
| II | ago/2026 → nov/2026 | parâmetros normativos de aferição de idade, prioridades de monitoramento, período de adaptação |
| III | jan/2027 → | fiscalização efetiva conforme Mapa de Temas Prioritários (Res. CD/ANPD nº 30/2025) |

A lei **é exigível desde 17/03/2026**; o cronograma descreve a postura fiscalizatória, não suspensão de vigência. Nunca classificar requisito como dispensado por estar em etapa de adaptação.

## Checklist atômico
Perguntas de enquadramento (não pontuam):
- O produto ou serviço é fornecido à distância, por meio eletrônico e por requisição individual (art. 2º, I)?
- O fornecedor o declara direcionado a crianças e adolescentes?
- Ele está em uma das categorias com presunção de acesso provável ("Regras de enquadramento")? Se sim, o módulo se aplica, salvo fundamentação concreta em contrário.
- Fora delas, os três requisitos do art. 1º, parágrafo único, estão presentes ao mesmo tempo? Aferição de idade e outras medidas de cumprimento não entram nessa conta.
- O fornecedor se enquadra na dispensa do art. 39, §1º (controle editorial ou conteúdo licenciado)? Se sim, cumpre as quatro condições?

Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`. Itens que dependem do tipo de serviço (conteúdo adulto, loja de aplicativos ou sistema operacional, jogos, monitoramento infantil, equipamentos, limiar de 1 milhão de usuários, provedor estrangeiro, IA generativa, venda de produtos proibidos, monetização ou impulsionamento de conteúdo de usuários) ficam `NAO_APLICAVEL` quando o objeto não existe. O consentimento parental e o tratamento de dados de crianças pela LGPD são os itens `CA` de [[children-adolescents]].

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `ECA-01` | Há medidas de prevenção, desde a concepção, contra as seis categorias de conteúdo do art. 6º? | 16 | `CRITICO` | `ALTO` se a lacuna estiver só nas categorias dos incisos IV a VI | `TECNICO` | Lei nº 15.211/2025, art. 6º; LGPD arts. 6º, VIII e 14 |
| `ECA-02` | As configurações padrão são as mais protetivas disponíveis? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, art. 7º; LGPD arts. 14 e 46 |
| `ECA-03` | Há gestão de risco, classificação indicativa, bloqueio de conteúdo inadequado, padrões contra uso compulsivo e informação da faixa etária no acesso? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, art. 8º; LGPD arts. 6º, VIII e 14 |
| `ECA-04` | Serviço com conteúdo impróprio a menores de 18 anos: há verificação de idade confiável **a cada acesso**, sem autodeclaração, e bloqueio de criação de conta em serviço pornográfico? | 16 | `CRITICO` | — | `TECNICO` | Lei nº 15.211/2025, art. 9º, §§1º e 3º; LGPD art. 14 |
| `ECA-05` | Loja de aplicativos ou sistema operacional: há aferição de idade auditável, supervisão parental, API de sinal de idade com minimização e consentimento do responsável para download? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, art. 12; LGPD arts. 6º, III e 14 |
| `ECA-06` | Os dados de verificação de idade são usados **exclusivamente** para essa finalidade, e a imagem ou cópia de documento coletada é eliminada logo após a captura da idade? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 13 e 24, §3º; Decreto nº 12.880/2026, art. 24, §3º; LGPD art. 6º, I e III |
| `ECA-07` | O fornecedor recebe o sinal de idade da loja ou do sistema e mantém mecanismo próprio de bloqueio, sem depender só de autodeclaração? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 10 e 14; LGPD art. 14, §5º |
| `ECA-08` | Em tratamento além do estritamente necessário: há mapeamento de riscos e relatório de impacto? | 16 | `MEDIO` | — | `DOCUMENTAL` | Lei nº 15.211/2025, art. 16, parágrafo único; LGPD art. 38 |
| `ECA-09` | As ferramentas de supervisão parental cumprem os nove padrões do art. 17, §4º e as seis capacidades do art. 18, em língua portuguesa? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 17 e 18; LGPD art. 14 |
| `ECA-10` | O produto está livre de design manipulativo (dark patterns) que enfraqueça as salvaguardas? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, art. 18, §2º; LGPD arts. 6º, VI e 14 |
| `ECA-11` | Jogos: o produto está livre de caixas de recompensa (loot boxes), ou o acesso de menores a elas é impedido por verificação de idade ou por restrição total por padrão? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, art. 20; Decreto nº 12.880/2026, art. 23; LGPD art. 14 |
| `ECA-12` | Jogos: a interação entre usuários é limitada por padrão, dependendo do consentimento dos responsáveis? | 16 | `MEDIO` | — | `TECNICO` | Lei nº 15.211/2025, art. 21; LGPD art. 14 |
| `ECA-13` | O serviço está livre de perfilamento, análise emocional e realidade aumentada, estendida ou virtual para publicidade a menores, inclusive com dados da verificação de idade? | 16 | `CRITICO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 22 e 26; LGPD arts. 6º, I e 14 |
| `ECA-14` | O serviço impede a monetização e o impulsionamento de conteúdo que retrate menores de forma erotizada ou em contexto adulto? | 16 | `CRITICO` | — | `TECNICO` | Lei nº 15.211/2025, art. 23; LGPD art. 14 |
| `ECA-15` | As contas de usuários de até 16 anos estão vinculadas à conta de um responsável legal? | 16 | `CRITICO` | — | `TECNICO` | Lei nº 15.211/2025, art. 24; LGPD art. 14, §1º |
| `ECA-16` | Há procedimento para indícios de conta operada por menor, com suspensão e apelação célere do responsável? | 16 | `MEDIO` | — | `TECNICO` | Lei nº 15.211/2025, art. 24, §§3º e 4º; LGPD art. 14 |
| `ECA-17` | Há fluxo de remoção e comunicação às autoridades de conteúdo de exploração, abuso sexual, sequestro e aliciamento, com retenção dos dados pelo prazo do art. 15 do MCI (6 meses)? | 16 | `CRITICO` | — | `TECNICO` | Lei nº 15.211/2025, art. 27; LGPD arts. 7º, II e 16, I |
| `ECA-18` | Há canal de notificação público e de fácil acesso, com identificação do notificante, retirada sem ordem judicial e direito de contestação? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 28 a 30; LGPD arts. 6º, VI e 20 |
| `ECA-19` | Acima de 1.000.000 de usuários menores registrados no País: o relatório semestral com os sete incisos do art. 31 foi publicado no prazo, no site e em português? | 16 | `ALTO` | — | `DOCUMENTAL` | Lei nº 15.211/2025, art. 31; LGPD art. 6º, X |
| `ECA-20` | Há mecanismo contra o uso abusivo dos instrumentos de denúncia, com sanções graduadas e registros? | 16 | `MEDIO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 32 e 33; LGPD art. 6º, X |
| `ECA-21` | Provedor estrangeiro: há representante legal no País com poderes para receber citações e notificações? | 16 | `MEDIO` | — | `DOCUMENTAL` | Lei nº 15.211/2025, art. 40; LGPD art. 6º, X |
| `ECA-22` | Equipamentos eletrônicos com acesso à internet: a embalagem traz o adesivo de alerta aos responsáveis? | 16 | `BAIXO` | — | `DOCUMENTAL` | Lei nº 15.211/2025, art. 38; Decreto nº 12.880/2026, art. 50; LGPD art. 6º, VI |
| `ECA-23` | Produtos de monitoramento infantil: as informações captadas são invioláveis e o menor é avisado do monitoramento em linguagem apropriada? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, art. 19; LGPD arts. 14 e 46 |
| `ECA-24` | IA generativa ou agente conversacional: a interação informa o caráter sintético e automatizado, e há prevenção de manipulação comportamental, avaliação do risco algorítmico e salvaguardas ao desenvolvimento de crianças e adolescentes? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 6º e 8º, I; Decreto nº 12.880/2026, art. 11; LGPD arts. 6º, VI e 14 |
| `ECA-25` | Venda ou intermediação de produtos ou serviços proibidos a menores: há verificação de idade efetiva no cadastro ou na compra, sem desbloqueio por autodeclaração e com bloqueio para usuário não autenticado? | 16 | `ALTO` | — | `TECNICO` | Lei nº 15.211/2025, arts. 6º, IV e 9º; Decreto nº 12.880/2026, arts. 15 e 18; LGPD art. 14 |
| `ECA-26` | Há avaliação de impacto à segurança e à saúde de crianças e adolescentes, com acompanhamento da efetividade das medidas, e a versão resumida está publicada em linguagem clara? | 16 | `MEDIO` | — | `DOCUMENTAL` | Lei nº 15.211/2025, arts. 8º, I e 16, parágrafo único, II; Decreto nº 12.880/2026, art. 47; LGPD art. 6º, X |
| `ECA-27` | Conteúdo monetizado ou impulsionado que explore de forma habitual a imagem ou a rotina de criança ou adolescente: o fornecedor exige a autorização judicial e retira o conteúdo quando ela falta? | 16 | `ALTO` | — | `TECNICO` | Decreto nº 12.880/2026, art. 34; Lei nº 15.211/2025, art. 5º; Lei nº 8.069/1990, art. 149; LGPD art. 14 |

Fronteiras entre itens:
- `ECA-04` trata de conteúdo impróprio ou proibido **exibido ou consumido** no serviço; `ECA-25`, da **compra e venda** de produtos e serviços proibidos. A caixa de recompensa em jogo é só `ECA-11`.
- `ECA-03` avalia a gestão de risco em funcionamento no produto; `ECA-08`, o relatório de impacto do tratamento de dados além do estritamente necessário; `ECA-26`, o documento de avaliação de impacto à segurança e à saúde e a publicação do seu resumo. A falta de um não reprova os outros.
- `ECA-14` trata de conteúdo erotizado ou em contexto adulto; `ECA-27`, da exploração habitual da imagem do menor sem autorização judicial.
- `ECA-24` avalia os quatro deveres do art. 11 do decreto; governança, transparência e segurança de IA em geral são os itens `IA` de [[llm-audit]].

## Mapeamento para severidade e score
- Conteúdo adulto sem verificação de idade a cada acesso, ou com autodeclaração (art. 9º, §1º): `CRITICO`.
- Ausência de medidas contra os conteúdos do art. 6º, I a III: `CRITICO`.
- Perfilamento ou análise emocional para publicidade a menores (arts. 22 e 26): `CRITICO`.
- Conta de menor de até 16 anos sem vinculação a responsável (art. 24): `CRITICO`.
- Ausência de fluxo de remoção/comunicação de abuso sexual e aliciamento (art. 27): `CRITICO`.
- Reuso dos dados de aferição de idade para outra finalidade (art. 13): `ALTO`.
- Ausência de privacidade por padrão (art. 7º) ou dos defaults de supervisão parental (art. 17, §4º): `ALTO`.
- Relatório semestral do art. 31 não publicado por provedor acima do limiar: `ALTO`.
- Loot box acessível a menores em jogo de acesso provável (art. 20; Decreto, art. 23): `ALTO`.
- IA generativa sem os deveres do art. 11 do Decreto: `ALTO`.
- Venda de produto proibido a menores sem verificação de idade efetiva (Decreto, art. 18): `ALTO`.
- Monetização ou impulsionamento de conteúdo com exploração habitual da imagem de menor, sem autorização judicial (Decreto, art. 34): `ALTO`.
- Ausência da avaliação de impacto à segurança e à saúde ou da publicação do resumo (Decreto, art. 47): `MEDIO`.
- Dark pattern que enfraquece salvaguardas (art. 18, §2º): `ALTO`.
- Ausência de relatório de impacto no caso do art. 16, parágrafo único: `MEDIO`.
- Ausência de mecanismo contra uso abusivo de denúncias (art. 32): `MEDIO`.
- Provedor estrangeiro sem representante legal no País (art. 40): `MEDIO`.
- Ausência do adesivo do art. 38 em embalagens: `BAIXO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `eca_digital` (domínio 16) para todos os itens deste módulo; o consentimento parental e o tratamento de dados de crianças pela LGPD (art. 14) são os itens `CA`, que pontuam em `bases_legais`. A criticidade de cada item está na tabela do checklist; os artigos sem regra acima (8º, 12, 14, 19, 21, 23, 24, §§3º e 4º, e 28 a 30) seguem a criticidade da tabela.
- O Decreto nº 12.880/2026 detalha como cumprir a lei e não tem regime de severidade próprio: achado fundamentado nele segue a criticidade do item.

## Regra de fundamentação
Todo `finding` deste módulo deve citar **o artigo do ECA Digital** (e o do Decreto nº 12.880/2026, quando o detalhamento vier dele) e o **correlato na LGPD** (art. 14 e/ou princípios do art. 6º; art. 46 quando for falha de segurança). Achado sem correlato LGPD explícito quebra o contrato de `finding` em [[auditor-core]].

## Em monitoramento (não vigente — não gera não conformidade)
A situação das normas em monitoramento, com a data da última conferência, está só em [[anpd-guidelines]]: guia de aferição de idade, parâmetros definitivos de aferição de idade e cronograma de fiscalização. O cronograma não suspende a vigência da lei: os requisitos deste módulo são exigíveis desde 17/03/2026.

Regulamentos ainda pendentes previstos na própria lei: requisitos mínimos de aferição de idade e supervisão parental em lojas/SO (art. 12, §3º), diretrizes de supervisão parental (art. 17, §1º), prazos de notificação às autoridades (art. 27, §1º), critérios de acesso a dados para pesquisa (art. 31, parágrafo único) e critérios de modulação de obrigações (art. 39, §3º).

Pendentes de ato da ANPD ou do MJSP previsto no Decreto nº 12.880/2026: requisitos mínimos de segurança por padrão (art. 10), regulamentação dos deveres de IA generativa (art. 11, parágrafo único), termos da verificação de idade na venda de produtos proibidos e em redes sociais (arts. 18 e 19), requisitos contra a exposição a produtos proibidos (art. 32), prazos da comunicação ao Centro Nacional de Triagem de Notificações (art. 39, §1º), conteúdo mínimo e periodicidade da avaliação de impacto (art. 47, §2º) e aviso em embalagens (art. 50, §3º). O dever em si já vale; a falta do ato só impede exigir o detalhe que ele trará.

## Relação com outros módulos
- Art. 14 da LGPD e consentimento parental: ver [[children-adolescents]].
- Base legal e finalidade do tratamento: ver [[legal-bases-engine]].
- Relatório de impacto: ver [[ripd-template]].
- Aferição de idade em lojas de aplicativos e SO: ver [[mobile-storage]].
- Recomendação algorítmica, análise emocional e IA: ver [[llm-audit]].
- Governança, DPO e trilha de evidência: ver [[dpo-framework]].
