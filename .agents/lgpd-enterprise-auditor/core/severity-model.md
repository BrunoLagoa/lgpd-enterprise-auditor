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

## Modulação por porte e exposição
A severidade pode ser **reduzida em um nível** (ex.: `ALTO` → `MEDIO`) quando todas as condições abaixo forem verdadeiras:
- o agente de tratamento é de **pequeno porte** nos termos da Res. CD/ANPD nº 2/2022 (microempresa, empresa de pequeno porte, startup, pessoa jurídica de direito privado, inclusive sem fins lucrativos, ou pessoa natural e ente privado despersonalizado que atue como controlador ou operador), sem as exclusões da própria resolução (como faturamento acima do limite ou grupo econômico que o ultrapasse);
- não há **tratamento de alto risco** nos critérios da mesma resolução (larga escala ou impacto significativo, combinados com tecnologia emergente, vigilância, decisão automatizada, dados sensíveis ou de crianças, adolescentes e idosos);
- não há exposição explorável confirmada.

Nunca modular:
- achados `CRITICO` que envolvam dados sensíveis, dados de crianças e adolescentes, vazamento confirmado ou credenciais expostas;
- deveres que a própria norma não modula por porte (ex.: comunicação de incidente, prazos do titular).

Toda modulação é registrada no `finding` (`severity_modulation`: severidade original, aplicada e justificativa) e vale também para a `criticality` do item no score. Pessoa natural que trata dados para fins exclusivamente particulares e não econômicos está fora da LGPD (art. 4º, I): nesse caso, registrar a inaplicabilidade em vez de emitir achados.

## Regras de uso
- Cada `finding` deve ter um único nível de severidade.
- Quando mais de uma regra de severidade, do mesmo módulo ou de módulos diferentes, se aplicar ao mesmo achado, vale a mais específica; se forem igualmente específicas, a mais alta.
- Em dúvida entre dois níveis, usar o mais alto quando houver impacto jurídico potencial significativo.
- Achados `CRITICO` e `ALTO` devem ter plano de ação com prazo definido.
