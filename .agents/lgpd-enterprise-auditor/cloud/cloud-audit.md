# Cloud Module - Cloud, PaaS and Hosting Audit

## Escopo
Avaliar postura de segurança e privacidade de onde a aplicação roda:
- **IaaS** (AWS, Azure, GCP);
- **PaaS e serverless** (ex.: Vercel, Netlify, Render, Heroku, Cloudflare);
- **hospedagem compartilhada** (ex.: Hostinger, Locaweb, HostGator).

Os itens abaixo usam termos de IaaS; em PaaS e hospedagem, aplicar o equivalente do painel do provedor e registrar como `PARCIAL` ou fora de alcance o que o provedor não expõe ao cliente.

## Checklist atômico
- Há ativos públicos indevidos (ex.: buckets com dados pessoais)?
- Permissões de acesso ao provedor (IAM, membros do painel, tokens de deploy) seguem privilégio mínimo, com MFA?
- A divisão de responsabilidades com o provedor está clara (o que é do provedor e o que é do auditado: certificados, DNS, CDN, backups, atualizações)?
- A camada da hospedagem ou CDN altera o que a aplicação envia (cabeçalhos de segurança e CSP, cache de páginas com dados pessoais, scripts ou analytics injetados pelo provedor)? Validar as respostas de **produção**, não só o código.
- Analytics, logs de acesso e métricas nativos do provedor coletam dados pessoais? Têm retenção, acesso e base legal definidos?
- Variáveis de ambiente e segredos ficam no cofre do provedor, fora do repositório e de builds ou previews públicos?
- Há contrato de operador (DPA) com o provedor de hospedagem?
- Chaves/secrets estão em serviço dedicado (KMS/Secrets Manager equivalente)?
- Bancos de dados com dados pessoais têm criptografia em repouso, controle de acesso, segregação e mascaramento em ambientes não produtivos?
- Backups e réplicas são criptografados, têm acesso restrito e seguem a política de retenção (a eliminação também os alcança)?
- Há firewall/WAF, IDS/IPS e monitoramento centralizado (SIEM ou equivalente) capaz de detectar acesso indevido a dados pessoais?
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
- regras de firewall/security groups;
- cabeçalhos HTTP coletados das respostas de produção (ex.: `curl -I`) comparados com a configuração do código;
- configurações e termos do provedor de PaaS ou hospedagem (analytics nativo, logs, região, DPA).

## Mapeamento para severidade e score
- Exposição pública de dado pessoal/sensível: `CRITICO`.
- Hospedagem ou CDN que remove ou enfraquece cabeçalhos de segurança configurados no código, ou injeta rastreamento sem base legal: `ALTO`.
- Acesso excessivo e ausência de trilha de auditoria: `ALTO`.
- Banco de dados, backup ou réplica com dados pessoais sem criptografia em repouso: `ALTO`.
- Logs com dados pessoais exportados a terceiros sem contrato de operador ou sem mecanismo do art. 33: `ALTO`.
- Logs de observabilidade sem política de retenção: `MEDIO`.
- Registros de acesso a aplicações sem guarda de 6 meses, sem porta lógica ou retidos além do prazo sem base legal: `MEDIO`.
- Falhas pontuais de hardening: `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `infraestrutura` (domínio 7); os itens de transferência internacional e de contrato com o provedor pontuam em `governanca` (domínio 14).
