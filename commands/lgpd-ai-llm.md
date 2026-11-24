---
name: lgpd-ai-llm
description: Executa auditoria LGPD direcionada para sistemas com IA/LLM (cenário ai_llm_system). Use quando o produto chama provedores ou SDKs de IA generativa, usa embeddings, RAG ou fine-tuning, ou envia dados pessoais a modelos.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.13.1"
---

# LGPD IA/LLM

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- provedores de IA/LLM utilizados;
- uso de prompts, embeddings, RAG e fine-tuning;
- política de retenção e transferência internacional;
- tipos de dados pessoais/sensíveis enviados para IA;
- público: a quem o sistema é oferecido (usuários em geral, clientes, só funcionários) e se há usuários menores de 18 anos.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `ai_llm_system`:
- `core`, `legal`, `governance`, `ai-llm`, `appsec`.

Adicione `eca-digital` se o sistema for IA generativa ou agente conversacional oferecido a usuários — a lei presume o acesso provável por menores, salvo fundamentação concreta em contrário, como o uso restrito a funcionários — ou se menores forem expostos a recomendação algorítmica ou perfilamento (gatilho normativo do router — ECA Digital, Lei nº 15.211/2025, e Decreto nº 12.880/2026, art. 11).

Adicione `plataformas-digitais` se a IA puder gerar ou alterar imagem ou som de pessoas (vedação de conteúdo íntimo do art. 9º do Decreto nº 12.976/2026) ou moderar conteúdo de terceiros (gatilho normativo do router — Decretos nº 12.975/2026 e nº 12.976/2026).

Adicione `cloud` se houver Firebase ou storage cloud, `mobile` se houver app iOS ou Android (nativo, Flutter ou React Native) e `devsecops` se houver CI/CD ativo ou Kubernetes (gatilhos técnicos do router).

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- validar risco de prompt injection e vazamento contextual;
- exigir base legal para tratamento de dados em IA;
- consolidar score e relatório no padrão de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
