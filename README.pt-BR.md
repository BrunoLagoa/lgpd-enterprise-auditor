# LGPD Enterprise Auditor

<p align="left">
  <img src="./assets/logo-lgpd-enterprise-auditor.webp" alt="Logo LGPD Enterprise Auditor" width="355" />
</p>

<p align="center">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/stargazers"><img src="https://img.shields.io/github/stars/BrunoLagoa/lgpd-enterprise-auditor?style=social" alt="GitHub stars" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License MIT" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor"><img src="https://hits.sh/github.com/BrunoLagoa/lgpd-enterprise-auditor.svg?label=Project%20views&color=f1c40f" alt="Project views" /></a>
</p>

<!-- README-I18N:START -->

[English](./README.md) | **Português (Brasil)**

<!-- README-I18N:END -->

Framework de auditoria LGPD orientado a evidências, com foco em segurança, governança e uso de IA em engenharia de software.

Este projeto foi desenhado para funcionar como um sistema auditável e modular, pronto para ser reutilizado em diferentes produtos e times.

## O que é este projeto

O `lgpd-enterprise-auditor` é um framework que combina:

- auditoria jurídica (LGPD + ANPD);
- auditoria técnica (appsec, cloud, mobile, devsecops, IA/LLM);
- modelo de severidade e score;
- formato de relatório padronizado;
- comandos práticos para execução por cenário.

Na prática, ele permite rodar auditorias completas ou direcionadas com consistência de critérios, evidências e plano de adequação.

## Base legal e atualização

Este framework usa como referência principal a **Lei Geral de Proteção de Dados (LGPD)**:

- **Texto oficial (Planalto):** [Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- **Órgão regulador:** [ANPD](https://www.gov.br/anpd/)

| Item | Valor |
|------|--------|
| Última sincronização | `2026-05` |

## Como o projeto está organizado

```text
.
├── SKILL.md
├── commands/
│   ├── lgpd-full-audit.md
│   ├── lgpd-saas.md
│   ├── lgpd-mobile.md
│   ├── lgpd-ai-llm.md
│   └── lgpd-devsecops.md
└── .agents/
    └── lgpd-enterprise-auditor/
        ├── core/
        ├── legal/
        ├── governance/
        ├── cloud/
        ├── appsec/
        ├── mobile/
        ├── devsecops/
        ├── ai-llm/
        ├── orchestrator/
        ├── templates/
        ├── reports/
        ├── validation/
        └── legacy/
```

### Fonte canônica

O caminho base canônico do framework modular é:

`.agents/lgpd-enterprise-auditor/`

Esse é o padrão esperado para projetos que adotarem a mesma estrutura.

## Como funciona

O fluxo da auditoria segue 5 passos:

1. **Contexto do projeto**: stack, dados tratados, integrações e operação.
2. **Roteamento inteligente**: o orquestrador ativa módulos por cenário.
3. **Checklist com evidência**: nada é marcado como conforme sem comprovação.
4. **Consolidação**: severidade, score e classificação final.
5. **Saída padronizada**: relatório executivo/técnico/compliance + plano de adequação.

## Modos de uso

### 1) Auditoria completa

Use quando quiser cobertura total:

- comando: `commands/lgpd-full-audit.md`
- cenário: `full_audit`

Módulos acionados: `core`, `legal`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

### 2) Auditoria por cenário

Use para escopo focado:

- `lgpd-saas` -> SaaS web
- `lgpd-mobile` -> app mobile
- `lgpd-ai-llm` -> sistemas com IA/LLM
- `lgpd-devsecops` -> pipelines e supply chain

## Comandos disponíveis

Os comandos em `commands/` são atalhos de execução para o agente.

Todos incluem:

- metadados (`name`, `description`, `license`, `author`, `version`);
- coleta de contexto mínimo quando não mapeado;
- regras obrigatórias de evidência e consistência com o framework modular.

## Contratos de auditoria (resumo)

Os contratos centrais estão em `.agents/lgpd-enterprise-auditor/core/`:

- `auditor-core.md`: estruturas canônicas (`finding`, `check_item`, `module_output`);
- `evidence-engine.md`: regras de evidência;
- `severity-model.md`: classificação de severidade;
- `scoring-engine.md`: cálculo de score;
- `reporting-engine.md`: formato obrigatório da saída.

## Para quem este projeto é útil

- times de engenharia e plataforma;
- segurança da informação e AppSec;
- compliance e privacidade;
- consultorias de adequação LGPD;
- squads com uso de IA generativa em produção.

## Boas práticas de adoção

- manter `.agents/lgpd-enterprise-auditor/` versionado junto ao produto;
- adaptar comandos por domínio, sem quebrar contratos do core;
- registrar evidências técnicas e documentais por item;
- revisar score e não conformidades por release;
- tratar auditoria como processo contínuo, não evento isolado.

## Roadmap sugerido

- templates mais ricos por setor (healthtech, fintech, gov);
- automação de coleta de evidências;
- geração de matriz de risco por ambiente;
- relatórios comparativos entre releases;
- integração com pipelines CI/CD.

## Pessoas por trás do Memflow

Este projeto evolui com contribuições de pessoas que acreditam em engenharia de software com IA de forma disciplinada, prática e auditável.

<p align="left">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=BrunoLagoa/lgpd-enterprise-auditor&max=100" alt="Contribuidores do projeto" width="45" />
  </a>
</p>

Quer aparecer aqui também? Abra uma issue, sugira melhorias ou envie um PR.

## Suporte

Para obter suporte, abra uma issue no GitHub. Relatos de bugs, solicitações de recursos e dúvidas de uso são bem-vindos.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [`LICENSE`](LICENSE) para os termos completos.
