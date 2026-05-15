# AppSec Module - OWASP Web/API

## Escopo
Auditar segurança de aplicação web e APIs com foco em riscos LGPD.

## Checklist atômico
- Há proteção contra XSS, CSRF, SSRF e SQL Injection?
- Autenticação é robusta (MFA quando aplicável)?
- Autorização impede acesso indevido (RBAC/ABAC)?
- Sessões/tokens têm proteção adequada (expiração, rotação, escopo)?
- Há rate limiting e proteção contra abuso?
- Entradas/saídas são validadas e sanitizadas?

## Critérios de evidência
- configuração de headers e políticas de segurança;
- evidências de controles de autenticação/autorização;
- logs de tentativas de abuso e bloqueio;
- exemplos de validação/sanitização de entrada.

## Mapeamento para severidade e score
- Falha explorável com exfiltração de dados pessoais: `CRITICO`.
- Falha de autenticação/autorização sem exploração confirmada: `ALTO`.
- Ausência parcial de hardening e validações: `MEDIO`.
- Área de scoring primária: `seguranca` (25%) e `apis_integracoes` (10%).
