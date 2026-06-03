# Router (V2)

## Objetivo
Ativar apenas módulos relevantes ao contexto do projeto, preservando cobertura completa no modo legado.

## Entradas mínimas
- stack (frontend/backend/mobile);
- cloud provider;
- integrações de terceiros;
- presença de IA/LLM;
- maturidade de DevSecOps.

## Regras de ativação

### Regra global
`core` e `legal` são sempre obrigatórios.

### Cenários base
- `saas_web`: `core`, `legal`, `governance`, `appsec`, `cloud`, `devsecops`.
- `web_site`: `core`, `legal`, `governance`, `appsec`, `cloud`.
- `mobile_app`: `core`, `legal`, `governance`, `mobile`, `appsec`, `cloud`.
- `ai_llm_system`: `core`, `legal`, `governance`, `ai-llm`, `appsec`.
- `devsecops_pipeline`: `core`, `legal`, `devsecops`, `cloud`, `appsec`.

### Gatilhos técnicos adicionais
- Se usar `Firebase` ou storage cloud, adicionar `cloud`.
- Se houver API pública, adicionar `appsec`.
- Se houver uso de embeddings/RAG/fine-tuning, adicionar `ai-llm`.
- Se houver Kubernetes ou CI/CD ativo, adicionar `devsecops`.

## Modo de compatibilidade V1
`full_audit` ativa todos os módulos:
`core`, `legal`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

## Saída do roteador
- lista de módulos ativos;
- justificativa de ativação por módulo;
- escopo excluído explicitamente (módulos não acionados).

## Convenção de nomes
- O roteador ativa módulos por ID de módulo (kebab-case), ex.: `ai-llm`.
- O cálculo de score usa IDs de área (snake_case), ex.: `ai_llm`.
