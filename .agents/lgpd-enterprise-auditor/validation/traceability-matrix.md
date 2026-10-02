# Validação — matriz de rastreabilidade (domínios → módulos)

| Domínio de auditoria | Módulo(s) | Contratos do core usados |
|---|---|---|
| Mapeamento de dados | `governance` (registro das operações, art. 37), `legal` | `check_item`, `finding`, `reporting` |
| Consentimento | `legal` (`legal-bases-engine.md`, art. 8º), `appsec` (cookies) | `check_item`, `finding` |
| Direitos do titular | `legal` (`rights-of-data-subject.md`, arts. 18 e 19), `governance` | `check_item`, `finding` |
| Política de privacidade | `legal` (`rights-of-data-subject.md`, art. 9º), `templates` | `check_item`, `finding`, `reporting` |
| Cookies e tracking | `appsec` (seção de cookies de `owasp-api.md`), `mobile`, `templates` | `check_item`, `finding` |
| Segurança da informação | `appsec` (aplicação e backend), `cloud` (banco de dados e infraestrutura), `devsecops` | `severity`, `evidence` |
| Cloud security | `cloud` | `severity`, `evidence`, `scoring` |
| Mobile security | `mobile` | `severity`, `evidence`, `scoring` |
| APIs e integrações | `appsec` | `severity`, `evidence`, `scoring` |
| DevSecOps | `devsecops` | `severity`, `evidence`, `scoring` |
| Logs e observabilidade | `appsec` (logs de aplicação), `cloud` (observabilidade), `devsecops`, `governance` | `check_item`, `finding` |
| IA/LLM | `ai-llm` | `severity`, `evidence`, `scoring` |
| Governança | `governance` | `check_item`, `finding`, `scoring` |
| Compartilhamento de dados | `legal`, `governance` | `check_item`, `finding` |
| Retenção e exclusão | `governance` (arts. 15 e 16 em `dpo-framework.md`), `cloud` (backups e réplicas), `ai-llm` (retenção de prompts) | `check_item`, `finding` |
| Proteção de crianças e adolescentes no ambiente digital (ECA Digital) | `eca-digital`, `legal`, `governance`, `mobile`, `templates` | `check_item`, `finding`, `severity`, `evidence`, `scoring` |
| Plataformas digitais e conteúdo de terceiros (Decretos nº 12.975 e 12.976/2026) | `plataformas-digitais`, `governance` (art. 16-A), `cloud` (guarda de registros), `ai-llm` (deepfake íntimo) | `check_item`, `finding`, `severity`, `evidence`, `scoring` |

## Observação
Esta matriz deve ser atualizada sempre que um domínio mudar de módulo primário.
