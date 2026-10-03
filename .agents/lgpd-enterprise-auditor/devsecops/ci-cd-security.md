# Módulo DevSecOps — CI/CD e cadeia de suprimentos

## Escopo
Auditar pipeline CI/CD, cadeia de dependências e segurança de containers.

## Checklist atômico
- Segredos no pipeline estão protegidos e sem exposição em logs?
- Há scanning de dependências e policy de atualização?
- SAST/DAST são executados em estágio apropriado?
- SBOM é gerado e armazenado?
- Imagens Docker passam por scanning de vulnerabilidades?
- Infraestrutura como código (Terraform, CloudFormation, Helm etc.) passa por scanning de configuração (IaC scanning)?
- Ambiente Kubernetes segue controles de RBAC e hardening?

## Critérios de evidência
- configuração de CI/CD com controles de segredo;
- histórico de scans (dependência, SAST, DAST);
- artefatos SBOM;
- relatórios de segurança de imagem/container;
- políticas RBAC e segurança de cluster.

## Mapeamento para severidade e score
- Segredo exposto em pipeline/artefato público: `CRITICO`.
- Ausência total de varredura de segurança: `ALTO`.
- Cobertura parcial de scanning e hardening: `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `seguranca` (domínio 10) para todos os itens deste módulo.
