# Cloud Module - Cloud Security Audit

## Escopo
Avaliar postura de segurança e privacidade em ambientes cloud (AWS/Azure/GCP).

## Checklist atômico
- Há ativos públicos indevidos (ex.: buckets com dados pessoais)?
- Políticas IAM seguem privilégio mínimo?
- Chaves/secrets estão em serviço dedicado (KMS/Secrets Manager equivalente)?
- Logs de auditoria cloud estão ativos e protegidos?
- Logs e observabilidade (CloudWatch, Datadog, Sentry, ELK etc.) têm retenção definida, acesso por privilégio mínimo e mascaramento de dados pessoais?
- A exportação de logs a ferramentas de terceiros está coberta por contrato de operador e, se os dados saírem do País, por mecanismo do art. 33?
- Provedor de aplicações de internet: os registros de acesso (IP, porta lógica de origem, data e hora) são guardados por 6 meses, sob sigilo e em ambiente controlado, e eliminados após o prazo salvo requisição cautelar (MCI art. 15; Decreto nº 8.771/2016, art. 15-A; LGPD arts. 7º, II e 16, I)? Ver [[plataformas-digitais]].
- Segmentação de rede e regras de exposição externa estão adequadas?
- Há processo de hardening e gestão de vulnerabilidades em infra?
- A região/armazenamento implica transferência internacional de dados? Se sim, há mecanismo legal do art. 33 (ver `legal/international-transfer.md`)?

## Critérios de evidência
- políticas IAM e evidências de revisão;
- configuração de bucket/object storage;
- evidência de uso de KMS/secret manager;
- trilhas de auditoria cloud habilitadas;
- configuração de retenção, acesso e destino das ferramentas de logs/observabilidade;
- regras de firewall/security groups.

## Mapeamento para severidade e score
- Exposição pública de dado pessoal/sensível: `CRITICO`.
- Acesso excessivo e ausência de trilha de auditoria: `ALTO`.
- Logs com dados pessoais exportados a terceiros sem contrato de operador ou sem mecanismo do art. 33: `ALTO`.
- Logs de observabilidade sem política de retenção: `MEDIO`.
- Registros de acesso a aplicações sem guarda de 6 meses, sem porta lógica ou retidos além do prazo sem base legal: `MEDIO`.
- Falhas pontuais de hardening: `MEDIO`.
- Área de scoring primária: `infraestrutura` (10%) e `seguranca` (25%).
