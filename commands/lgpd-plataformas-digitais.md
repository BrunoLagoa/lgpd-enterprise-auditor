---
name: lgpd-plataformas-digitais
description: Executa auditoria LGPD + deveres de plataformas digitais (Decretos 12.975/2026 e 12.976/2026, regulamentacao do Marco Civil da Internet) para provedores de aplicacoes com conteudo de terceiros.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.3.0"
---

# LGPD + Plataformas Digitais (conteudo de terceiros)

Antes de perguntar, leia o que o projeto ja documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependencias e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou nao puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou juridica, com ou sem fins economicos, porte (agente de pequeno porte, Res. CD/ANPD 2/2022) e se ha tratamento de alto risco;
- tipo de servico (rede social, plataforma de video, forum, marketplace, comentarios publicos, mensageria com grupos abertos, IA generativa de imagem/voz);
- se ha intermediacao de conteudo gerado por terceiros com difusao publica;
- canal de denuncia, fluxo de notificacao, remocao e contestacao, com metricas de prazo;
- politicas de moderacao, gestao de riscos sistemicos e deteccao de redes artificiais;
- ferramentas de anuncio ou impulsionamento pago e politica de aceite de anuncios;
- guarda de registros de acesso (IP, porta logica, data/hora) e politica de expurgo;
- sede e representante legal no Brasil;
- termos de uso e relatorio anual de transparencia;
- funcionalidades de IA capazes de gerar ou alterar imagem ou som de pessoas.

Ative o cenario `digital_platform`:
- `core`, `legal`, `plataformas-digitais`, `governance`, `appsec`, `cloud`.

Adicione `ai-llm` se houver IA generativa ou moderacao automatizada, e `eca-digital` se o servico for direcionado ou provavelmente acessado por menores de 18 anos (gatilhos do router).

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- aplicar `.agents/lgpd-enterprise-auditor/legal/plataformas-digitais.md`;
- verificar as exclusoes do art. 16-O (e-mail, mensageria interpessoal, videoconferencia restrita) e o regime de ordem judicial para crimes contra a honra (art. 16-J) antes de emitir achado;
- nunca tratar conteudo ilicito isolado como falha sistemica: o achado aponta processos ausentes ou insuficientes (art. 16-B, par. 3);
- nao unificar os prazos: conteudo intimo em ate 2 horas (Decreto 12.976, art. 7, par. 1); prazos transitorios de 6 horas e 24 horas e 24 horas apos contestacao (art. 12);
- fundamentar cada achado no dispositivo do decreto (e do Marco Civil, quando houver) e no correlato da LGPD;
- registrar exposicao cumulativa: sancoes do art. 12 do Marco Civil e do art. 52 da LGPD (e do art. 35 do ECA Digital, havendo menores);
- exigir evidencia por requisito;
- produzir relatorio conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
