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
- `eca_digital_platform`: `core`, `legal`, `eca-digital`, `governance`, `appsec`, `mobile`.

### Gatilhos técnicos adicionais
- Se usar `Firebase` ou storage cloud, adicionar `cloud`.
- Se houver API pública, adicionar `appsec`.
- Se houver uso de embeddings/RAG/fine-tuning, adicionar `ai-llm`.
- Se houver Kubernetes ou CI/CD ativo, adicionar `devsecops`.

### Gatilho normativo — público infantojuvenil
Adicionar `eca-digital` a **qualquer** cenário quando houver indício de usuários menores de 18 anos:
- serviço direcionado a crianças ou adolescentes;
- serviço provavelmente acessado por menores (rede social, vídeo, jogo, mensageria, fórum, marketplace);
- cadastro que aceite ou não bloqueie usuários menores de 18 anos;
- jogos eletrônicos, itens virtuais pagos ou monetização por engajamento;
- app classificado para faixa etária inferior a 18 anos nas lojas.

Esse gatilho é **normativo, não técnico**: na dúvida sobre a presença de menores, ativar o módulo e registrar a incerteza como evidência `PARCIAL`.

## Modo de compatibilidade V1
`full_audit` ativa todos os módulos:
`core`, `legal`, `eca-digital`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

## Saída do roteador
- lista de módulos ativos;
- justificativa de ativação por módulo;
- escopo excluído explicitamente (módulos não acionados).

## Convenção de nomes
- O roteador ativa módulos por ID de módulo (kebab-case), ex.: `ai-llm`.
- O cálculo de score usa IDs de área (snake_case), ex.: `ai_llm`.
