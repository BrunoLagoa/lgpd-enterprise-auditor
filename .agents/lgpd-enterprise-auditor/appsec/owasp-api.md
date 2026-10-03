# Módulo AppSec — segurança de aplicações web e APIs (OWASP)

## Escopo
Auditar segurança de aplicação web e APIs com foco em riscos LGPD, incluindo cookies/tracking no front-end e dados pessoais em logs de aplicação.

## Checklist atômico
- Todo tráfego usa HTTPS, com HSTS e cabeçalhos de segurança (CSP, entre outros) configurados?
- Há proteção contra XSS, CSRF, SSRF e SQL Injection?
- Autenticação é robusta (MFA quando aplicável)?
- Autorização impede acesso indevido (RBAC/ABAC)?
- Sessões/tokens têm proteção adequada (expiração, rotação, escopo)?
- Há rate limiting e proteção contra abuso?
- Há segregação de ambientes e de funções e trilha de auditoria dos acessos a dados pessoais no backend?
- APIs validam tokens corretamente (JWT: assinatura, algoritmo, expiração e audiência) e usam OAuth com escopos mínimos?
- As respostas das APIs expõem só os campos necessários, sem exposição excessiva de dados pessoais?
- APIs públicas estão inventariadas e API keys ficam fora do código, dos repositórios e do front-end?
- A comunicação com integrações e entre serviços é criptografada em trânsito?
- Entradas/saídas são validadas e sanitizadas?
- Logs da aplicação evitam registrar dados pessoais e sensíveis (CPF, e-mail, telefone, tokens, senhas, payloads completos) ou os mascaram antes da gravação?

## Cookies, tracking e consentimento no front-end
Aplicável a toda aplicação web que use cookies, pixels, tags ou SDKs de terceiros (ex.: Google Analytics, Meta Pixel, Hotjar, Google Ads).

- Existe banner/CMP funcional com informação clara sobre finalidades e terceiros?
- Cookies e scripts não essenciais ficam bloqueados até o aceite, sem requisições a terceiros de analytics/publicidade antes do consentimento — salvo outra base legal documentada (ex.: legítimo interesse com LIA para medição estritamente agregada)?
- O consentimento é granular por finalidade (desempenho, funcionalidade, publicidade), sem categorias pré-marcadas?
- Rejeitar está disponível na primeira camada com o mesmo destaque de aceitar?
- O usuário consegue revisar e revogar as preferências a qualquer momento?
- As escolhas ficam registradas (data, versão do banner, categorias aceitas) como prova do consentimento (art. 8º, §2º)?
- Pixels, fingerprinting e identificadores persistentes de terceiros estão inventariados e cobertos pela política de cookies?
- Os cookies classificados como estritamente necessários são de fato necessários (a categoria não mascara analytics ou publicidade)?

Fundamento: art. 7º, I e art. 8º (consentimento livre, informado, inequívoco, por finalidade e revogável), art. 9º (transparência) e art. 6º, III (necessidade). Referência orientativa, não vinculante: Guia Orientativo da ANPD sobre cookies e proteção de dados pessoais. Usar [[cookie-policy-template]].

## Critérios de evidência
- configuração de headers e políticas de segurança;
- evidências de controles de autenticação/autorização;
- logs de tentativas de abuso e bloqueio;
- exemplos de validação/sanitização de entrada;
- política de logging/mascaramento e amostras de log da aplicação;
- captura de rede (HAR/DevTools) antes e depois do aceite do banner;
- configuração do CMP e registro de consentimentos.

## Mapeamento para severidade e score
- Falha explorável com exfiltração de dados pessoais: `CRITICO`.
- Senhas ou tokens em texto puro nos logs: `CRITICO`.
- Falha de autenticação/autorização sem exploração confirmada: `ALTO`.
- Ausência de HTTPS em rotas com dados pessoais, API sem autenticação adequada ou com exposição excessiva de dados pessoais: `ALTO`.
- Logs da aplicação com dados pessoais sem mascaramento: `ALTO`.
- Cookies/pixels de publicidade ou analytics de terceiros disparados antes do aceite, sem outra base legal documentada: `ALTO`.
- Categorias de cookies pré-marcadas ou ausência de mecanismo de revogação: `ALTO`.
- Rejeição sem destaque equivalente, consentimento pouco granular ou ausência de registro das escolhas: `MEDIO`.
- Ausência parcial de hardening e validações: `MEDIO`.
- Imprecisões na classificação de cookies da política: `BAIXO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `seguranca` (domínios 6 e 11); itens de APIs e integrações (tokens JWT/OAuth e escopos, dados expostos em respostas, API keys, rate limiting de APIs, criptografia com integrações) pontuam em `apis_integracoes` (domínio 9); cookies e consentimento pontuam em `bases_legais` (domínio 5).
