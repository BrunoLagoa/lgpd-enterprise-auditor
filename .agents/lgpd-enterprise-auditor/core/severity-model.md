# Severity Model

## Objetivo
Normalizar severidade dos achados para priorização técnica e jurídica consistente.

## Níveis canônicos

### `CRITICO`
Violação grave com alto potencial de dano ao titular, infração relevante da LGPD ou exposição sensível imediata.

Exemplos:
- ausência de base legal para tratamento sensível;
- vazamento de dados sensíveis;
- credenciais em texto puro;
- bucket público com dados pessoais.

### `ALTO`
Risco jurídico/técnico elevado, com impacto relevante e alta probabilidade de incidente.

Exemplos:
- logs com dados pessoais sem mascaramento;
- ausência de criptografia em repouso para dados críticos;
- APIs com autenticação/autorização fraca.

### `MEDIO`
Não conformidade relevante, mas sem exposição imediata crítica.

Exemplos:
- retenção sem política clara;
- gestão parcial de direitos do titular;
- consentimento pouco granular.

### `BAIXO`
Melhoria recomendada com baixo risco imediato.

Exemplos:
- ajustes de clareza documental;
- melhoria de linguagem de política;
- pequenas melhorias de UX de consentimento.

## Regras de uso
- Cada `finding` deve ter um único nível de severidade.
- Em dúvida entre dois níveis, usar o mais alto quando houver impacto jurídico potencial significativo.
- Achados `CRITICO` e `ALTO` devem ter plano de ação com prazo definido.
