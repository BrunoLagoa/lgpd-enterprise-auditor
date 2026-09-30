---
name: lgpd-devsecops
description: Executa auditoria LGPD direcionada para pipelines DevSecOps.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.1.0"
---

# LGPD DevSecOps Pipeline

Antes de iniciar, se ainda nao estiver mapeado, solicite:
- plataforma de CI/CD;
- estrategia de containers e Kubernetes;
- gestao de segredos e scans de seguranca;
- fluxo de deploy e ambientes.

Ative o cenario `devsecops_pipeline`:
- `core`, `legal`, `devsecops`, `cloud`, `appsec`.

Regras obrigatorias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canonico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- validar segredos, supply chain e hardening de deploy;
- exigir evidencia para todos os achados;
- gerar score e relatorio tecnico/compliance.
