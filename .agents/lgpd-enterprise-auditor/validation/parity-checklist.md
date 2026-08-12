# Validation - Parity Checklist V1 to V2

## Objetivo
Validar que a V2 modular mantém cobertura e consistência funcional da V1.

## Checklist de validação
- [ ] Todos os 16 domínios da V1 estão mapeados em módulos V2.
- [ ] Nenhum módulo redefine severidade fora do `core/severity-model.md`.
- [ ] Nenhum módulo redefine score fora do `core/scoring-engine.md`.
- [ ] Todos os achados usam contrato `finding`.
- [ ] Todos os itens avaliados usam contrato `check_item`.
- [ ] Relatório final segue `core/reporting-engine.md`.
- [ ] Toda não conformidade possui evidência associada.
- [ ] Evidência usa os dois eixos canônicos em V1 e V2: `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`).
- [ ] Rótulos de classificação final seguem padrão canônico V2.
- [ ] Modo `full_audit` ativa todos os módulos.
- [ ] Matriz de ativação por cenário está coerente com o router.
- [ ] Bases legais distinguem art. 7º (dados pessoais) de art. 11 (sensíveis) em V1 e V2.
- [ ] Dados de crianças/adolescentes (art. 14) cobertos em V1 (`SKILL.md`) e V2 (`legal/children-adolescents.md`).
- [ ] Transferência internacional (arts. 33-36) coberta em V1 e V2 (`legal/international-transfer.md`).
- [ ] Prazo de comunicação de incidente (Res. CD/ANPD nº 15/2024, 3 dias úteis) presente em governança e template de incidente.
- [ ] Regulamento do encarregado (Res. CD/ANPD nº 18/2024 — ato escrito, datado e assinado; DPO pessoa jurídica; dispensa de indicação para pequeno porte) presente em V1 (`SKILL.md`) e V2 (`governance/dpo-framework.md`).
- [ ] Cláusulas-padrão contratuais (Res. CD/ANPD nº 19/2024) com prazo de adaptação encerrado em 23/08/2025 refletidas em V1, em `legal/international-transfer.md` e no `templates/dpa-template.md`.
- [ ] Adequação da União Europeia (Res. CD/ANPD nº 32/2026) reconhecida em V1 e V2, com a ressalva de que dispensa apenas o mecanismo do art. 33.
- [ ] ANPD tratada como agência reguladora (Lei nº 15.352/2026, art. 55-A) em V1 e V2, sem uso da denominação antiga em textos novos.
- [ ] ECA Digital (Lei nº 15.211/2025, Decretos nº 12.622/2025 e nº 12.880/2026) coberto em V1 (`SKILL.md`, domínio 16) e V2 (`legal/eca-digital.md` + manifesto `eca-digital`).
- [ ] Prazo do relatório semestral de transparência (limiar de 1 milhão de usuários menores; primeiro ciclo até 17/09/2026) presente em V1, no módulo `eca-digital` e no `templates/eca-transparency-report-template.md`.
- [ ] Autodeclaração simples de idade classificada como insuficiente em V1 e V2.
- [ ] Modo `full_audit` ativa também o módulo `eca-digital`.
- [ ] Normas não vigentes (ex.: PL nº 2338/2023) aparecem apenas em seções "Em monitoramento" e nunca originam `NAO_CONFORME`.

## Evidências de teste esperadas
- execução de cenário `saas_web`;
- execução de cenário `web_site`;
- execução de cenário `mobile_app`;
- execução de cenário `ai_llm_system`;
- execução de cenário `devsecops_pipeline`;
- execução de cenário `eca_digital_platform`;
- execução `full_audit`.
