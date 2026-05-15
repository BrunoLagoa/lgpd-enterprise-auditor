# Validation - Parity Checklist V1 to V2

## Objetivo
Validar que a V2 modular mantém cobertura e consistência funcional da V1.

## Checklist de validação
- [ ] Todos os 15 domínios da V1 estão mapeados em módulos V2.
- [ ] Nenhum módulo redefine severidade fora do `core/severity-model.md`.
- [ ] Nenhum módulo redefine score fora do `core/scoring-engine.md`.
- [ ] Todos os achados usam contrato `finding`.
- [ ] Todos os itens avaliados usam contrato `check_item`.
- [ ] Relatório final segue `core/reporting-engine.md`.
- [ ] Toda não conformidade possui evidência associada.
- [ ] Rótulos de classificação final seguem padrão canônico V2.
- [ ] Modo `full_audit` ativa todos os módulos.
- [ ] Matriz de ativação por cenário está coerente com o router.

## Evidências de teste esperadas
- execução de cenário `saas_web`;
- execução de cenário `mobile_app`;
- execução de cenário `ai_llm_system`;
- execução de cenário `devsecops_pipeline`;
- execução `full_audit`.
