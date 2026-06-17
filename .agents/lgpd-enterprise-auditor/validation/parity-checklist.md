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
- [ ] Bases legais distinguem art. 7º (dados pessoais) de art. 11 (sensíveis) em V1 e V2.
- [ ] Dados de crianças/adolescentes (art. 14) cobertos em V1 (`SKILL.md`) e V2 (`legal/children-adolescents.md`).
- [ ] Transferência internacional (arts. 33-36) coberta em V1 e V2 (`legal/international-transfer.md`).
- [ ] Prazo de comunicação de incidente (Res. CD/ANPD nº 15/2024, 3 dias úteis) presente em governança e template de incidente.

## Evidências de teste esperadas
- execução de cenário `saas_web`;
- execução de cenário `mobile_app`;
- execução de cenário `ai_llm_system`;
- execução de cenário `devsecops_pipeline`;
- execução `full_audit`.
