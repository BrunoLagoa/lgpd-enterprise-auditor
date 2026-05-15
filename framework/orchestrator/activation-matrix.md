# Activation Matrix (V2)

## Matriz por cenário

| Cenário | core | legal | governance | cloud | appsec | mobile | devsecops | ai-llm |
|---|---|---|---|---|---|---|---|---|
| SaaS Web (React/Node/Postgres/AWS) | X | X | X | X | X |  | X |  |
| Sistema IA/LLM (RAG + OpenAI/Pinecone) | X | X | X |  | X |  |  | X |
| App Mobile (Flutter/Firebase) | X | X | X | X | X | X |  |  |
| Pipeline (GitHub Actions + Docker + K8s) | X | X |  | X | X |  | X |  |
| Full Audit (compatibilidade V1) | X | X | X | X | X | X | X | X |

## Notas de aplicação
- Módulos não marcados podem ser adicionados por gatilho de risco.
- Se houver dados sensíveis ou processamento crítico, elevar cobertura para `full_audit`.
