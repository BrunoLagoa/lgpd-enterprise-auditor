# Mobile Module - Mobile Privacy and Security

## Escopo
Avaliar riscos de privacidade e segurança em apps iOS/Android/Flutter/React Native.

## Checklist atômico
- Dados sensíveis são armazenados de forma segura no dispositivo?
- Permissões solicitadas seguem necessidade mínima?
- Existe prevenção de vazamento via clipboard/log local?
- SDKs de tracking/analytics possuem controle de consentimento?
- Regras de backend mobile (ex.: Firebase rules) estão restritivas?
- Identificadores de dispositivo são usados com base legal adequada?

## Critérios de evidência
- configuração de storage seguro;
- manifesto de permissões e justificativa;
- inventário de SDKs terceiros;
- regras de acesso backend para mobile;
- fluxo de consentimento para tracking.

## Mapeamento para severidade e score
- Exposição local de dado sensível sem proteção: `CRITICO`.
- Tracking sem consentimento granular: `ALTO`.
- Permissões excessivas sem exploração direta: `MEDIO`.
- Área de scoring primária: `seguranca` (25%), `infraestrutura` (10%) e `bases_legais` (15%).
