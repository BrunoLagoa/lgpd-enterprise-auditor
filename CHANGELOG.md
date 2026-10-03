# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/). A versão do projeto é a `metadata.version` do `SKILL.md`, repetida em todos os `commands/*.md`; cada versão publicada tem uma tag `vX.Y.Z` correspondente.

## [Não lançado]

## [1.3.1] - 2026-10-02

### Alterado
- Comandos (`commands/*.md`) com acentuação completa, inclusive nas descrições exibidas no menu dos assistentes, e citações legais padronizadas (`nº`, `§`).
- Títulos dos arquivos do framework em português (`Núcleo — …`, `Módulo X — …`, `Manifesto — …`, `Modelo — …`).

## [1.3.0] - 2026-10-02

Mudanças motivadas pelo primeiro uso em projeto real e pela preparação para o lançamento público.

### Adicionado
- Cálculo do score fechado e reproduzível: `CONFORME` = 1, `PARCIAL` = 0,5, `NAO_CONFORME` = 0, com peso do item pela criticidade (4/3/2/1) (#4).
- Mapa de áreas por domínio: cada item do checklist pontua em uma única área; novos campos `score_area`, `criticality` e `control_type` no `check_item` (#5).
- Modulação de severidade por porte e exposição (Res. CD/ANPD nº 2/2022), limitada a um nível e vedada nos casos graves (#6).
- Score técnico e score documental, informativos, ao lado do score global (#7).
- Natureza do agente de tratamento como entrada inicial obrigatória do router, dos comandos e da skill (#8).
- Dados de acesso público e manifestamente públicos (art. 7º, §§ 3º, 4º e 7º), incluindo dado sensível divulgado por órgão oficial (#9).
- Registro de risco aceito no achado (quem, quando, justificativa e revisão), sem efeito no score (#11).
- Relatório: "o que fazer agora" com esforço `P | M | G`, coluna `Área` no checklist, glossário, aviso legal fixo e marcação de confidencialidade (#12, #13, #15).
- Exemplo público em `examples/saas-demo/`: SaaS fictício com falhas propositais e relatório completo (#16).
- Arquivos de comunidade: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, modelos de issue (bug, atualização normativa, melhoria) e de PR (#16).

### Alterado
- Antes de perguntar, a auditoria lê o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, README, `docs/`) e pergunta só o que falta (#14).
- Módulo de cloud generalizado para PaaS e hospedagem compartilhada, com validação das respostas de produção; `cloud/aws-audit.md` passa a ser `cloud/cloud-audit.md` (#10).
- Regras de consistência apontadas ao gerar o exemplo: itens `PARCIAL` também geram achado (severidade da lacuna, limitada à criticidade); contagem única de uma mesma falha; precedência da regra de severidade mais específica; transferência internacional distingue mecanismo comprovadamente ausente (`CRITICO`) de não evidenciado (`ALTO`); dispensa de encarregado e registro simplificado não valem para pequeno porte com tratamento de alto risco; severidade explícita para encarregado/RIPD, resposta a incidentes e DPA com operadores; `IMEDIATO` definido como até 7 dias.
- `README.md` passa a ser em português (canônico) e a versão em inglês vai para `README.en.md`, com resumo do produto, badges, link para o exemplo e aviso legal (#15, #16).

## [1.2.0] - 2026-10-02

### Adicionado
- `CHANGELOG.md` e verificação de versão única (`scripts/tests/test-versions.sh` e workflow `versions.yml`): `SKILL.md`, `commands/*.md`, changelog e tag precisam ter a mesma versão.
- Framework modular com as verificações da skill que faltavam:
  - `appsec`: HTTPS/HSTS/CSP, segregação e trilha de auditoria no backend, JWT/OAuth com escopos mínimos, exposição excessiva de dados, inventário de APIs públicas, API keys fora do código e criptografia em trânsito;
  - `cloud`: criptografia em repouso, backups e réplicas, WAF, IDS/IPS e SIEM;
  - `mobile`: detecção de jailbreak/root e validação de deep links;
  - `devsecops`: varredura de infraestrutura como código (IaC);
  - `governance`: retenção e eliminação (arts. 15 e 16), com eliminação automática, descarte seguro e retenções legais.
- Orientação para incluir `.lgpd-auditor-backup/` no `.gitignore`, nos instaladores e nos READMEs.

### Alterado
- Checklist de paridade entre a skill e o framework verificado item a item (39 de 39), com data da verificação.
- Definição de dado sensível completa, igual ao art. 5º, II ("quando vinculado a uma pessoa natural"), na skill e no framework.
- Adequação da União Europeia (Res. CD/ANPD nº 32/2026) com a ressalva de que dispensa apenas o mecanismo do art. 33, também na skill, no template de DPA e em `anpd-guidelines.md`.
- Skill: base correta da vedação à autodeclaração de idade, os três cortes etários sem unificação, art. 7º, §1º do Decreto nº 12.976/2026, arts. 16-I e 16-P, e exemplos com evidência e fundamento.
- Relatórios por público (`reports/`) passam a remeter ao relatório canônico; normas em monitoramento ficam só em `recomendacoes_tecnicas`.
- `ai-llm`: rotulagem de conteúdo sintético movida para "Em monitoramento"; orientações preliminares da ANPD no `eca-digital` marcadas como não vinculantes.
- README do framework lista os cenários `web_site` e `full_audit`; evidências de teste esperadas incluem `digital_platform`.
- Instaladores: a pergunta do assistente passa a ser "Instalar também a skill?", com o mesmo texto na ajuda de `--with-skill` / `-WithSkill`.
- Terminologia unificada: o projeto deixa de usar designações de versão, "legado" e "monolítica" para suas partes e passa a falar em skill (`SKILL.md`) e framework modular (`.agents/lgpd-enterprise-auditor/`), inclusive na descrição do comando `lgpd-full-audit`, nos títulos dos arquivos e nos READMEs.

### Removido
- Pasta `legacy/` do framework: a cobertura do `full_audit` passa a ficar em `orchestrator/full-audit.md`; a matriz de rastreabilidade foi renomeada para `validation/traceability-matrix.md`.

### Corrigido
- `commands/lgpd-plataformas-digitais.md` estava na versão `1.0.0`; alinhado em `1.1.0`.

## [1.1.0] - 2026-10-02

### Adicionado
- Instalador interativo por projeto: `scripts/install.sh` (macOS, Linux, WSL, Git Bash) e `scripts/install.ps1` (Windows PowerShell 5.1 e PowerShell 7), com as ações `install`, `update`, `uninstall` e `check`, modo `--non-interactive` e manifesto por ferramenta em `.agents/lgpd-enterprise-auditor/.install/`.
- Ferramentas suportadas pelo instalador: `claude`, `cursor`, `vscode`, `opencode` e `agents` (Codex, Gemini CLI e similares); a skill é opcional, exceto em `agents`.
- Testes de regressão dos dois instaladores (`scripts/tests/`) e CI no Ubuntu, no macOS (`/bin/bash` 3.2) e no Windows (PowerShell 7 e 5.1).
- Frontmatter YAML no `SKILL.md` (`name`, `description`, `license`, `metadata`), permitindo instalá-lo como skill.
- Módulo `plataformas-digitais` (Decretos nº 12.975/2026 e nº 12.976/2026): `legal/plataformas-digitais.md`, manifesto, cenário `digital_platform`, gatilho normativo no router, domínio 17 da skill e comando `lgpd-plataformas-digitais`.
- Módulo `eca-digital` (Lei nº 15.211/2025) com templates de relatório semestral de transparência e checklist de aferição de idade.
- Comando `lgpd-web` e cenário `web_site` para sites e landing pages.
- Regra de área `NAO_APLICAVEL` com redistribuição proporcional dos pesos do score (skill e framework).
- Checklists de consentimento (art. 8º), transparência (art. 9º), prazos de atendimento ao titular (art. 19), registro das operações (art. 37, com forma simplificada para pequeno porte), cookies e tracking, e dados pessoais em logs.

### Alterado
- Evidência classificada em dois eixos independentes: `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`), na skill e no framework.
- Base normativa atualizada com as resoluções da ANPD e a Lei nº 15.352/2026 (ANPD como Agência); itens com prazo revisados.
- READMEs com seção de instalação; a documentação do `full_audit` aponta para os locais de instalação da skill.

## [1.0.0] - 2026-05-15

### Adicionado
- Versão inicial: skill autocontida (`SKILL.md`) e framework modular em `.agents/lgpd-enterprise-auditor/` (contratos do core, módulos especialistas, orquestrador por cenário, relatórios, templates e validação de paridade).
- Comandos `lgpd-full-audit`, `lgpd-saas`, `lgpd-mobile`, `lgpd-ai-llm` e `lgpd-devsecops`.
- READMEs em inglês e português e licença MIT.

[Não lançado]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.3.1...HEAD
[1.3.1]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/tag/v1.1.0
[1.0.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/commit/8e4f21b
