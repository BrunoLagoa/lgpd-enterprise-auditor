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

## Regulamento da ANPD (Res. CD/ANPD nº 19/2024)
- A **Resolução CD/ANPD nº 19/2024** (23/08/2024) aprovou o Regulamento de Transferência Internacional de Dados e as **cláusulas-padrão contratuais (CPC)**.
- O prazo de 12 meses para incorporar as CPC aos instrumentos contratuais **encerrou em 23/08/2025**. Não existe mais período de adaptação.
- Consequência para a auditoria: contrato de transferência internacional que ainda não incorporou as CPC — ou outro mecanismo aprovado equivalente — é **não conformidade atual**, e não item "em adequação".
- As CPC não podem ser alteradas de forma a reduzir o nível de proteção; cláusulas contratuais específicas exigem submissão à ANPD.

## Países e organismos com grau adequado reconhecido
- **Resolução CD/ANPD nº 32/2026** (26/01/2026) — reconhece a **União Europeia** como organismo internacional com grau adequado de proteção.
- Efeito prático: transferência para destinatário na UE que se enquadre no reconhecimento **dispensa CPC** como fundamento do art. 33; a decisão de adequação passa a ser o mecanismo legal.
- A dispensa é **apenas do mecanismo do art. 33** — permanecem obrigatórios base legal do art. 7º/11, informação ao titular, contrato de operador (art. 39) e as garantias de segurança do art. 46.
- Estados Unidos, Reino Unido e demais destinos **não** possuem reconhecimento de adequação pela ANPD: continuam exigindo CPC ou outro mecanismo do art. 33.

## Checklist atômico
- O fluxo de dados para o exterior está mapeado (destino, provedor, finalidade)?
- Há mecanismo legal do art. 33 documentado para cada transferência?
- Para destinos fora da UE, as CPC da Res. 19/2024 foram incorporadas aos contratos (prazo vencido em 23/08/2025)?
- Para destinos na UE, a adequação da Res. 32/2026 está documentada como mecanismo aplicável?
- Existem CPC/DPA com os operadores e subprocessadores internacionais, incluindo subprocessadores de segundo nível?
- O titular é informado sobre a transferência internacional na política de privacidade?
- Dados sensíveis transferidos têm proteção e base legal reforçadas?

## Mapeamento para severidade e score
- Transferência internacional de dados sensíveis sem mecanismo legal: `CRITICO`.
- Transferência para destino sem adequação e sem CPC após 23/08/2025: `CRITICO`.
- Transferência sem CPC/DPA ou sem informação ao titular: `ALTO`.
- Contrato com CPC incorporadas, mas sem cobertura dos subprocessadores: `MEDIO`.
- Área de scoring primária: `bases_legais` e `governanca`; contribui também para `infraestrutura`.

## Relação com outros módulos
- Postura cloud e exposição: ver [[aws-audit]].
- Gestão de operadores/subprocessadores e DPA: ver [[dpo-framework]].
