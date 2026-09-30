---
name: lgpd-eca-digital
description: Executa auditoria direcionada de LGPD + ECA Digital (Lei 15.211/2025) para plataformas acessadas por criancas e adolescentes.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.1.0"
---

# LGPD + ECA Digital (publico infantojuvenil)

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- tipo de produto (rede social, plataforma de video, jogo, mensageria, marketplace, app educacional);
- publico-alvo declarado e publico real (ha usuarios menores de 18 anos?);
- volume de usuarios registrados menores de 18 anos (limiar de 1 milhao define o relatorio de transparencia);
- fluxo de cadastro e mecanismo de afericao de idade em uso;
- existencia de vinculacao de conta de menor a responsavel e de ferramentas de supervisao parental;
- configuracoes padrao de privacidade para perfis de menores;
- regras de publicidade, perfilamento e recomendacao algoritmica;
- mecanicas de jogo, itens virtuais pagos e caixas de recompensa (loot boxes);
- fluxo de denuncia, moderacao e remocao de conteudo, com politica de retencao;
- pais de origem do provedor e existencia de representante legal no Brasil.

Ative o cenario `eca_digital_platform`:
- `core`, `legal`, `eca-digital`, `governance`, `appsec`, `mobile`.

Adicione `ai-llm` se houver recomendacao algoritmica, moderacao automatizada ou IA generativa.

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- aplicar `.agents/lgpd-enterprise-auditor/legal/eca-digital.md` junto de `.agents/lgpd-enterprise-auditor/legal/children-adolescents.md`;
- usar `.agents/lgpd-enterprise-auditor/templates/age-assurance-checklist.md` para a afericao de idade;
- usar `.agents/lgpd-enterprise-auditor/templates/eca-transparency-report-template.md` quando o provedor superar 1 milhao de usuarios menores;
- tratar autodeclaracao simples de idade como NAO_CONFORME (vedacao expressa do art. 9º, §1º para conteudo improprio; insuficiencia perante os arts. 10, 12 e 14 nos demais casos);
- verificar a modulacao e a dispensa editorial do art. 39 antes de emitir achado;
- nao unificar os cortes etarios: crianca ate 12 anos incompletos (LGPD art. 14), vinculacao de conta ate 16 anos (art. 24) e conteudo improprio a menores de 18 anos (art. 9º);
- fundamentar cada achado no dispositivo do ECA Digital e no correlato da LGPD (art. 14 e/ou art. 6º);
- registrar exposicao cumulativa: sancoes do art. 35 da Lei 15.211/2025 e do art. 52 da LGPD;
- exigir evidencia por requisito;
- produzir relatorio conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
