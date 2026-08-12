# Checklist - Aferição de Idade (ECA Digital)

Roteiro auditável de mecanismos confiáveis de aferição de idade, alinhado à Lei nº 15.211/2025, às orientações preliminares da ANPD (março/2026) e ao Radar Tecnológico nº 5. Usar junto de [[eca-digital]].

## 1. Identificação de escopo
| Item | Resposta | Evidência |
|---|---|---|
| O serviço é direcionado a menores de 18 anos? | | |
| O serviço é provavelmente acessado por menores? | | |
| Há cadastro de usuário? | | |
| Quantos usuários menores de 18 anos registrados? | | |
| Classificação etária nas lojas de aplicativos | | |

Se qualquer resposta indicar presença de menores, o restante do checklist é obrigatório.

## 2. Mecanismo de aferição
| Requisito | Status | Evidência |
|---|---|---|
| Existe mecanismo de aferição de idade | `CONFORME / PARCIAL / NAO_CONFORME` | |
| O mecanismo vai além da autodeclaração simples | | |
| O mecanismo é proporcional ao risco do serviço | | |
| Há trilha técnica do resultado da aferição (log/atributo de conta) | | |
| Há reavaliação periódica ou em mudança de comportamento | | |

**Autodeclaração isolada = `NAO_CONFORME`.** Não aceitar checkbox "declaro ter mais de 18 anos" como evidência.

## 3. Minimização e finalidade
| Requisito | Status | Evidência |
|---|---|---|
| Dados de aferição usados **exclusivamente** para verificar idade | | |
| Vedado reuso para marketing, perfilamento, antifraude ou treinamento de modelo | | |
| Preferência por prova de faixa etária em vez de documento completo | | |
| Documento/biometria descartado após a verificação, ou retenção justificada e prazada | | |
| Dado biométrico tratado como sensível (art. 11, LGPD), com base legal própria | | |
| Transferência internacional do provedor de verificação com mecanismo do art. 33 | | |

## 4. Vinculação a responsável (menores de 16 anos)
| Requisito | Status | Evidência |
|---|---|---|
| Conta de menor de 16 anos vinculada à conta de responsável | | |
| O vínculo é verificado, não apenas declarado | | |
| Responsável tem controle sobre tempo de uso | | |
| Responsável tem controle sobre contatos | | |
| Responsável tem controle sobre conteúdos acessados | | |
| Consentimento parental específico e em destaque coletado (art. 14, §1º, LGPD) | | |

## 5. Efeitos da aferição no produto
| Requisito | Status | Evidência |
|---|---|---|
| Perfil de menor nasce com privacidade máxima por padrão | | |
| Geolocalização desativada por padrão | | |
| Descoberta por estranhos / mensagens de desconhecidos bloqueadas por padrão | | |
| Publicidade comportamental desativada para menores | | |
| Recomendação algorítmica ajustada ou desativada para menores | | |
| Itens virtuais pagos e caixas-surpresa bloqueados ou conformes | | |

## 6. Acessibilidade, inclusão e recurso
| Requisito | Status | Evidência |
|---|---|---|
| Existe rota alternativa para quem não possui documento | | |
| Existe canal de contestação de aferição incorreta | | |
| O mecanismo não discrimina por origem, deficiência ou condição socioeconômica (art. 6º, IX, LGPD) | | |
| Taxa de erro do mecanismo é medida e documentada | | |

## 7. Fecho de auditoria
- Severidade sugerida para ausência total de mecanismo: `CRITICO`.
- Severidade sugerida para reuso indevido dos dados de aferição: `ALTO`.
- Fundamentação obrigatória: dispositivo do ECA Digital **+** art. 14 e art. 6º, I da LGPD.
- Registrar `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`) por linha preenchida.
