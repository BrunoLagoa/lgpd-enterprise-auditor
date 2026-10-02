# Router

## Objetivo
Ativar apenas módulos relevantes ao contexto do projeto, preservando cobertura completa no modo `full_audit`.

## Entradas mínimas
- stack (frontend/backend/mobile);
- cloud provider;
- integrações de terceiros;
- presença de IA/LLM;
- maturidade de DevSecOps;
- faixa etária do público: serviço direcionado a menores, de acesso provável por eles ou com cadastro sem bloqueio etário (insumo do gatilho normativo de `eca-digital`).

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
- `digital_platform`: `core`, `legal`, `plataformas-digitais`, `governance`, `appsec`, `cloud`.

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

### Gatilho normativo — plataformas digitais
Adicionar `plataformas-digitais` a **qualquer** cenário quando o auditado for provedor de aplicações de internet que:
- intermedeie conteúdo gerado por terceiros com difusão pública (rede social, vídeo, fórum, comentários públicos, marketplace com anúncios de usuários, grupos abertos);
- ofereça, mediante pagamento, ferramentas de anúncio ou impulsionamento de conteúdo;
- disponibilize IA ou recurso equivalente capaz de gerar ou alterar imagem ou som de pessoas.

Serviços exclusivamente de e-mail, mensageria interpessoal ou videoconferência restrita estão fora dos arts. 16-B a 16-J (art. 16-O do Decreto nº 8.771/2016). Mesmo sem o módulo ativo, os deveres gerais do art. 16-A e a guarda de registros de acesso (MCI art. 15) são verificados por `governance` e `cloud` em todo provedor de aplicações.

## Auditoria completa
`full_audit` ativa todos os módulos (cobertura em `orchestrator/full-audit.md`):
`core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

## Saída do roteador
- lista de módulos ativos;
- justificativa de ativação por módulo;
- escopo excluído explicitamente (módulos não acionados).

## Convenção de nomes
- O roteador ativa módulos por ID de módulo (kebab-case), ex.: `ai-llm`.
- O cálculo de score usa IDs de área (snake_case), ex.: `ai_llm`.
