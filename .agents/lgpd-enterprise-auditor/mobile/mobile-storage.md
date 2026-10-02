# Mobile Module - Mobile Privacy and Security

## Escopo
Avaliar riscos de privacidade e segurança em apps iOS/Android/Flutter/React Native.

## Checklist atômico
- Dados sensíveis são armazenados de forma segura no dispositivo?
- Permissões solicitadas seguem necessidade mínima?
- Existe prevenção de vazamento via clipboard/log local?
- O app detecta jailbreak/root e reduz a exposição de dados pessoais nesses dispositivos?
- Deep links e app links são validados, sem expor dados ou ações sensíveis por URL?
- SDKs de tracking/analytics possuem controle de consentimento?
- Regras de backend mobile (ex.: Firebase rules) estão restritivas?
- Identificadores de dispositivo são usados com base legal adequada?
- O app é classificado ou acessível a menores de 18 anos nas lojas (App Store, Google Play)? Se sim, ativar [[eca-digital]].
- O app consome o **sinal de idade** exposto pela loja/SO via API (art. 12, III da Lei nº 15.211/2025) e mantém mecanismo próprio de bloqueio (art. 14), ou depende apenas de autodeclaração?
- SDKs de publicidade recebem identificadores de usuários menores?

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
