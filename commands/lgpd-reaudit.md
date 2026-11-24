---
name: lgpd-reaudit
description: Executa uma nova auditoria LGPD e a compara com o relatório anterior do mesmo projeto. Use depois de correções, para ver o que foi corrigido, o que piorou, o que segue pendente, os prazos vencidos e a variação do score.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.13.1"
---

# LGPD Reauditoria

Siga `.agents/lgpd-enterprise-auditor/reports/reaudit-report.md`: ele define como achar o relatório anterior, como parear os itens e o arquivo do comparativo.

Antes de perguntar, localize o relatório anterior e leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura). Apresente o que o relatório anterior registra (data da análise, comando, cenário, versão do framework, score e classificação) e o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- o caminho do relatório anterior, se ele não for encontrado ou houver mais de um;
- o que mudou desde a auditoria anterior na natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- o que mudou no papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- novas integrações, novos dados pessoais ou sensíveis, uso de IA/LLM e público menor de 18 anos;
- se o cenário continua o mesmo.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador). O comparativo é sempre gravado em `.md`.

Use o cenário do relatório anterior (linha "Cenário" do `.md` ou `meta.scenario` do `.html`), com os módulos de `.agents/lgpd-enterprise-auditor/orchestrator/activation-matrix.md`, e refaça os gatilhos técnicos e normativos de `.agents/lgpd-enterprise-auditor/orchestrator/router.md`: o projeto pode ter ganhado ou perdido o objeto de um módulo desde então.

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- avaliar cada item com evidência colhida nesta auditoria antes de abrir a comparação; o relatório anterior nunca é evidência;
- produzir o relatório novo completo conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`, sem sobrescrever o anterior;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`, e o comparativo conforme `.agents/lgpd-enterprise-auditor/reports/reaudit-report.md`.
