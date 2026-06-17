# Transferência Internacional de Dados (arts. 33-36, LGPD)

## Objetivo
Avaliar a legalidade da transferência de dados pessoais para fora do Brasil, comum em uso de cloud, SaaS e APIs de IA hospedadas no exterior.

## Quando se aplica
Sempre que dados pessoais saem do território nacional, incluindo:
- provedores de cloud com regiões fora do Brasil (AWS, Azure, GCP);
- SaaS e analytics estrangeiros;
- APIs de IA/LLM de terceiros (ex.: OpenAI, Anthropic, Google) — ver [[llm-audit]];
- subprocessadores e CDNs internacionais.

## Mecanismos legais válidos (art. 33)
A transferência só é permitida quando houver pelo menos um:
- país/organismo com **grau de proteção adequado** reconhecido pela ANPD;
- **cláusulas-padrão contratuais (CPC)** aprovadas pela ANPD, cláusulas contratuais específicas, normas corporativas globais ou selos/certificados;
- cooperação jurídica internacional, proteção da vida, execução de política pública;
- **consentimento específico e em destaque** do titular, com informação sobre o caráter internacional;
- obrigação legal, execução de contrato ou exercício regular de direitos.

## Checklist atômico
- O fluxo de dados para o exterior está mapeado (destino, provedor, finalidade)?
- Há mecanismo legal do art. 33 documentado para cada transferência?
- Existem CPC/DPA com os operadores e subprocessadores internacionais?
- O titular é informado sobre a transferência internacional na política de privacidade?
- Dados sensíveis transferidos têm proteção e base legal reforçadas?

## Mapeamento para severidade e score
- Transferência internacional de dados sensíveis sem mecanismo legal: `CRITICO`.
- Transferência sem CPC/DPA ou sem informação ao titular: `ALTO`.
- Área de scoring primária: `bases_legais` e `governanca`; contribui também para `infraestrutura`.

## Relação com outros módulos
- Postura cloud e exposição: ver [[aws-audit]].
- Gestão de operadores/subprocessadores e DPA: ver [[dpo-framework]].
