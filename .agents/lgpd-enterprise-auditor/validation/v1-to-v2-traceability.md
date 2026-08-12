# Validation - V1 to V2 Traceability Matrix

| Domínio V1 | Módulo(s) V2 | Contratos do core usados |
|---|---|---|
| Mapeamento de dados | `legal`, `governance` | `check_item`, `finding`, `reporting` |
| Consentimento | `legal`, `appsec` | `check_item`, `finding` |
| Direitos do titular | `legal`, `governance` | `check_item`, `finding` |
| Política de privacidade | `templates`, `legal` | `reporting` |
| Cookies e tracking | `appsec`, `mobile`, `templates` | `check_item`, `finding` |
| Segurança da informação | `appsec`, `cloud`, `devsecops` | `severity`, `evidence` |
| Cloud security | `cloud` | `severity`, `evidence`, `scoring` |
| Mobile security | `mobile` | `severity`, `evidence`, `scoring` |
| APIs e integrações | `appsec` | `severity`, `evidence`, `scoring` |
| DevSecOps | `devsecops` | `severity`, `evidence`, `scoring` |
| Logs e observabilidade | `cloud`, `devsecops`, `governance` | `check_item`, `finding` |
| IA/LLM | `ai-llm` | `severity`, `evidence`, `scoring` |
| Governança | `governance` | `check_item`, `finding`, `scoring` |
| Compartilhamento de dados | `legal`, `governance` | `check_item`, `finding` |
| Retenção e exclusão | `legal`, `governance`, `ai-llm` | `check_item`, `finding` |
| Proteção de crianças e adolescentes no ambiente digital (ECA Digital) | `eca-digital`, `legal`, `governance`, `mobile`, `templates` | `check_item`, `finding`, `severity`, `evidence`, `scoring` |

## Observação
Esta matriz deve ser atualizada sempre que um domínio mudar de módulo primário.
