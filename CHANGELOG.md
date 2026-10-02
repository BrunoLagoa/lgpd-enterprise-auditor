# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/). A versão do projeto é a `metadata.version` do `SKILL.md`, repetida em todos os `commands/*.md`; cada versão publicada tem uma tag `vX.Y.Z` correspondente.

## [Não lançado]

### Adicionado
- `CHANGELOG.md` e verificação de versão única (`scripts/tests/test-versions.sh` e workflow `versions.yml`): `SKILL.md`, `commands/*.md`, changelog e tag precisam ter a mesma versão.
- V2 com as verificações da V1 que faltavam:
  - `appsec`: HTTPS/HSTS/CSP, segregação e trilha de auditoria no backend, JWT/OAuth com escopos mínimos, exposição excessiva de dados, inventário de APIs públicas, API keys fora do código e criptografia em trânsito;
  - `cloud`: criptografia em repouso, backups e réplicas, WAF, IDS/IPS e SIEM;
  - `mobile`: detecção de jailbreak/root e validação de deep links;
  - `devsecops`: varredura de infraestrutura como código (IaC);
  - `governance`: retenção e eliminação (arts. 15 e 16), com eliminação automática, descarte seguro e retenções legais.
- Orientação para incluir `.lgpd-auditor-backup/` no `.gitignore`, nos instaladores e nos READMEs.

### Alterado
- Checklist de paridade V1/V2 verificado item a item (39 de 39), com data da verificação.
- Definição de dado sensível completa, igual ao art. 5º, II ("quando vinculado a uma pessoa natural"), em V1 e V2.
- Adequação da União Europeia (Res. CD/ANPD nº 32/2026) com a ressalva de que dispensa apenas o mecanismo do art. 33, também na V1, no template de DPA e em `anpd-guidelines.md`.
- V1: base correta da vedação à autodeclaração de idade, os três cortes etários sem unificação, art. 7º, §1º do Decreto nº 12.976/2026, arts. 16-I e 16-P, e exemplos com evidência e fundamento.
- Relatórios por público (`reports/`) passam a remeter ao relatório canônico; normas em monitoramento ficam só em `recomendacoes_tecnicas`.
- `ai-llm`: rotulagem de conteúdo sintético movida para "Em monitoramento"; orientações preliminares da ANPD no `eca-digital` marcadas como não vinculantes.
- README da V2 lista os cenários `web_site` e `full_audit`; evidências de teste esperadas incluem `digital_platform`.
- Instaladores: a pergunta do assistente passa a ser "Instalar também a skill?", sem o rótulo "(V1 monolítica)", também na ajuda de `--with-skill` / `-WithSkill`.

### Corrigido
- `commands/lgpd-plataformas-digitais.md` estava na versão `1.0.0`; alinhado em `1.1.0`.

## [1.1.0] - 2026-10-02

### Adicionado
- Instalador interativo por projeto: `scripts/install.sh` (macOS, Linux, WSL, Git Bash) e `scripts/install.ps1` (Windows PowerShell 5.1 e PowerShell 7), com as ações `install`, `update`, `uninstall` e `check`, modo `--non-interactive` e manifesto por ferramenta em `.agents/lgpd-enterprise-auditor/.install/`.
- Ferramentas suportadas pelo instalador: `claude`, `cursor`, `vscode`, `opencode` e `agents` (Codex, Gemini CLI e similares); a skill é opcional, exceto em `agents`.
- Testes de regressão dos dois instaladores (`scripts/tests/`) e CI no Ubuntu, no macOS (`/bin/bash` 3.2) e no Windows (PowerShell 7 e 5.1).
- Frontmatter YAML no `SKILL.md` (`name`, `description`, `license`, `metadata`), permitindo instalá-lo como skill.
- Módulo `plataformas-digitais` (Decretos nº 12.975/2026 e nº 12.976/2026): `legal/plataformas-digitais.md`, manifesto, cenário `digital_platform`, gatilho normativo no router, domínio 17 da V1 e comando `lgpd-plataformas-digitais`.
- Módulo `eca-digital` (Lei nº 15.211/2025) com templates de relatório semestral de transparência e checklist de aferição de idade.
- Comando `lgpd-web` e cenário `web_site` para sites e landing pages.
- Regra de área `NAO_APLICAVEL` com redistribuição proporcional dos pesos do score (V1 e V2).
- Checklists de consentimento (art. 8º), transparência (art. 9º), prazos de atendimento ao titular (art. 19), registro das operações (art. 37, com forma simplificada para pequeno porte), cookies e tracking, e dados pessoais em logs.

### Alterado
- Evidência classificada em dois eixos independentes: `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`), em V1 e V2.
- Base normativa atualizada com as resoluções da ANPD e a Lei nº 15.352/2026 (ANPD como Agência); itens com prazo revisados.
- READMEs com seção de instalação; ponte `legacy/v1-monolith.md` aponta para os locais de instalação da skill.

## [1.0.0] - 2026-05-15

### Adicionado
- Versão inicial: V1 monolítica (`SKILL.md`) e V2 modular em `.agents/lgpd-enterprise-auditor/` (contratos do core, módulos especialistas, orquestrador por cenário, relatórios, templates e validação de paridade).
- Comandos `lgpd-full-audit`, `lgpd-saas`, `lgpd-mobile`, `lgpd-ai-llm` e `lgpd-devsecops`.
- READMEs em inglês e português e licença MIT.

[Não lançado]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/tag/v1.1.0
[1.0.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/commit/8e4f21b
