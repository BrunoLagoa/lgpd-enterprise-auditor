# Legacy V1 Monolith Compatibility

## Objetivo
Preservar referência operacional da V1 enquanto a V2 modular entra em produção.

## Fonte de verdade da V1
- Arquivo monolítico original: `SKILL.md`, na raiz do repositório do framework (caminho relativo ao projeto que adota `.agents/lgpd-enterprise-auditor/`).

## Regra de compatibilidade
- O modo `full_audit` da V2 deve cobrir os mesmos 15 domínios da V1:
  1. mapeamento de dados
  2. consentimento
  3. direitos do titular
  4. política de privacidade
  5. cookies e tracking
  6. segurança da informação
  7. cloud security
  8. mobile security
  9. APIs e integrações
  10. DevSecOps
  11. logs e observabilidade
  12. IA/LLM
  13. governança
  14. compartilhamento de dados
  15. retenção e exclusão

## Critérios mínimos de paridade
- manter classificação de severidade em 4 níveis;
- manter score global 0-100 e classificação final canônica;
- manter formato obrigatório do relatório;
- manter exigência de evidência para conclusões.
