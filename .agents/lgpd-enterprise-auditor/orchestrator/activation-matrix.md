# Activation Matrix (V2)

## Matriz por cenário

| Cenário | core | legal | eca-digital | plataformas-digitais | governance | cloud | appsec | mobile | devsecops | ai-llm |
|---|---|---|---|---|---|---|---|---|---|---|
| SaaS Web (React/Node/Postgres/AWS) | X | X |  |  | X | X | X |  | X |  |
| Web Site / Landing Page | X | X |  |  | X | X | X |  |  |  |
| Sistema IA/LLM (RAG + OpenAI/Pinecone) | X | X |  |  | X |  | X |  |  | X |
| App Mobile (Flutter/Firebase) | X | X |  |  | X | X | X | X |  |  |
| Pipeline (GitHub Actions + Docker + K8s) | X | X |  |  |  | X | X |  | X |  |
| Plataforma com público infantojuvenil (ECA Digital) | X | X | X |  | X |  | X | X |  |  |
| Plataforma digital com conteúdo de terceiros (Decretos nº 12.975 e 12.976/2026) | X | X |  | X | X | X | X |  |  |  |
| Full Audit (compatibilidade V1) | X | X | X | X | X | X | X | X | X | X |

Identificadores de cenário: `saas_web`, `web_site`, `ai_llm_system`, `mobile_app`, `devsecops_pipeline`, `eca_digital_platform`, `digital_platform`, `full_audit`.

## Notas de aplicação
- Módulos não marcados podem ser adicionados por gatilho de risco.
- `eca-digital` é adicionado a qualquer cenário pelo gatilho normativo de público infantojuvenil descrito em `router.md`, mesmo quando não marcado na linha.
- `plataformas-digitais` é adicionado a qualquer cenário pelo gatilho normativo de plataformas digitais descrito em `router.md` (conteúdo de terceiros com difusão pública, anúncios/impulsionamento pagos ou IA que gera ou altera imagem/som de pessoas).
- Se houver dados sensíveis ou processamento crítico, elevar cobertura para `full_audit`.
