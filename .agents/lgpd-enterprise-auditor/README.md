# LGPD Enterprise Auditor — framework modular

## Visão geral
O framework organiza a auditoria em camadas para facilitar manutenção, escalabilidade e especialização, com cobertura equivalente à da skill (`SKILL.md`).

## Estrutura
- `core/`: contratos canônicos (evidência, severidade, score, relatório).
- `legal/`: base normativa LGPD/ANPD, bases legais, ECA Digital (`legal/eca-digital.md`, módulo `eca-digital`) e deveres de plataformas digitais (`legal/plataformas-digitais.md`, módulo `plataformas-digitais`).
- `governance/`: governança, DPO, RIPD e terceiros.
- `cloud/`: postura cloud e exposição de infraestrutura.
- `appsec/`: segurança de aplicações e APIs.
- `mobile/`: segurança/privacidade mobile.
- `devsecops/`: CI/CD, supply chain, containers e Kubernetes.
- `ai-llm/`: riscos de IA generativa, RAG e retenção.
- `orchestrator/`: roteamento de módulos por cenário e cobertura do `full_audit` (`full-audit.md`).
- `templates/`: modelos de políticas e artefatos de conformidade.
- `reports/`: formatos de relatório por público.
- `validation/`: checklist de paridade com a skill e matriz de rastreabilidade dos domínios.

## Fluxo de execução
1. Capturar contexto do projeto (stack, dados, integrações).
2. Orquestrador ativa módulos aplicáveis.
3. Módulos executam checklist com evidência obrigatória.
4. Core consolida severidade, score e classificação.
5. Reporting engine gera relatório final.

## Modo de uso
- Modo direcionado: ativação por cenário (`saas_web`, `web_site`, `mobile_app`, `ai_llm_system`, `devsecops_pipeline`, `eca_digital_platform`, `digital_platform`).
- Auditoria completa (`full_audit`): ativa todos os módulos e cobre os 17 domínios de auditoria.

## Convenções de nomenclatura
- Módulos: kebab-case (ex.: `ai-llm`).
- Áreas de score: snake_case (ex.: `ai_llm`).
- Essa separação evita ambiguidade entre roteamento e cálculo de score.

## Cenários rápidos
- SaaS (React/Node/Postgres/AWS): `core`, `legal`, `governance`, `cloud`, `appsec`, `devsecops`.
- Site institucional ou landing page: `core`, `legal`, `governance`, `appsec`, `cloud`.
- IA/LLM (RAG): `core`, `legal`, `governance`, `ai-llm`, `appsec`.
- Mobile (Flutter/Firebase): `core`, `legal`, `governance`, `mobile`, `cloud`, `appsec`.
- Pipeline (GitHub Actions/Docker/K8s): `core`, `legal`, `devsecops`, `cloud`, `appsec`.
- Plataforma com público infantojuvenil (ECA Digital): `core`, `legal`, `eca-digital`, `governance`, `appsec`, `mobile`.
- Plataforma digital com conteúdo de terceiros (Decretos nº 12.975 e 12.976/2026): `core`, `legal`, `plataformas-digitais`, `governance`, `appsec`, `cloud`.
- Auditoria completa (`full_audit`): `core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

## Norma vigente x norma em monitoramento
- Só gera `finding` e `check_item` com status `NAO_CONFORME` a norma **vigente**.
- Normas em tramitação (ex.: PL nº 2338/2023 — Marco Legal da IA) e guias da ANPD em tomada de subsídios ficam em seções "Em monitoramento" nos módulos e só alimentam `recomendacoes_tecnicas` no relatório.
