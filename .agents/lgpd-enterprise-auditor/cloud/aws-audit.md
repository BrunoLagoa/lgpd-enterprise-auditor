# Cloud Module - Cloud Security Audit

## Escopo
Avaliar postura de segurança e privacidade em ambientes cloud (AWS/Azure/GCP).

## Checklist atômico
- Há ativos públicos indevidos (ex.: buckets com dados pessoais)?
- Políticas IAM seguem privilégio mínimo?
- Chaves/secrets estão em serviço dedicado (KMS/Secrets Manager equivalente)?
- Logs de auditoria cloud estão ativos e protegidos?
- Segmentação de rede e regras de exposição externa estão adequadas?
- Há processo de hardening e gestão de vulnerabilidades em infra?
- A região/armazenamento implica transferência internacional de dados? Se sim, há mecanismo legal do art. 33 (ver `legal/international-transfer.md`)?

## Critérios de evidência
- políticas IAM e evidências de revisão;
- configuração de bucket/object storage;
- evidência de uso de KMS/secret manager;
- trilhas de auditoria cloud habilitadas;
- regras de firewall/security groups.

## Mapeamento para severidade e score
- Exposição pública de dado pessoal/sensível: `CRITICO`.
- Acesso excessivo e ausência de trilha de auditoria: `ALTO`.
- Falhas pontuais de hardening: `MEDIO`.
- Área de scoring primária: `infraestrutura` (10%) e `seguranca` (25%).
