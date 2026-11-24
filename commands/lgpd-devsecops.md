---
name: lgpd-devsecops
description: Executa auditoria LGPD direcionada para pipelines DevSecOps (cenário devsecops_pipeline). Use para CI/CD, containers e Kubernetes, com foco em segredos, supply chain, scans de segurança e hardening de deploy.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.13.1"
---

# LGPD DevSecOps Pipeline

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- plataforma de CI/CD;
- estratégia de containers e Kubernetes;
- gestão de segredos e scans de segurança;
- fluxo de deploy e ambientes;
- uso de IA/LLM (chamada a provedor ou SDK, modelo próprio, embeddings, RAG);
- público: serviço direcionado a menores de 18 anos, provavelmente acessado por eles ou com cadastro sem bloqueio etário.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `devsecops_pipeline`:
- `core`, `legal`, `devsecops`, `cloud`, `appsec`.

Adicione `eca-digital` se o serviço for direcionado ou provavelmente acessado por menores de 18 anos, ou se estiver em categoria com presunção de acesso provável (rede social, jogo, conteúdo adulto, IA generativa, venda de produtos proibidos a menores); aferição de idade não afasta o gatilho (gatilho normativo do router — ECA Digital, Lei nº 15.211/2025).

Adicione `plataformas-digitais` se o serviço intermediar conteúdo de terceiros com difusão pública, vender anúncios/impulsionamento ou oferecer IA que gere ou altere imagem ou som de pessoas (gatilho normativo do router — Decretos nº 12.975/2026 e nº 12.976/2026).

Adicione `ai-llm` se houver chamada a provedor ou SDK de LLM ou de IA generativa, modelo próprio, embeddings, RAG ou fine-tuning (gatilho técnico do router).

Adicione `mobile` se houver app iOS ou Android (nativo, Flutter ou React Native; gatilho técnico do router).

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- validar segredos, supply chain e hardening de deploy;
- exigir evidência para todos os achados;
- gerar score e relatório técnico/compliance;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
