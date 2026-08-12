# Manifest - eca-digital

- `module`: eca-digital
- `required`: false
- `inputs`: faixa etária da base de usuários, fluxo de cadastro, mecanismo de aferição de idade, configurações padrão de perfil, regras de publicidade e recomendação, mecânicas de jogo e monetização, fluxo de moderação/denúncia, volume de usuários menores registrados
- `prerequisites`: core, legal
- `activates_when`: cenário `eca_digital_platform`, cenário `full_audit`, ou gatilho normativo de público infantojuvenil (serviço direcionado ou provavelmente acessado por menores de 18 anos, cadastro sem bloqueio etário, jogos eletrônicos, app classificado abaixo de 18 anos)
- `primary_outputs`: conformidade com a Lei nº 15.211/2025 (ECA Digital) e o Decreto nº 12.880/2026 — aferição confiável de idade, vinculação de conta de menor a responsável, supervisão parental, privacidade por padrão, vedação de publicidade e perfilamento sobre menores, vedação de caixas-surpresa pagas, moderação e remoção de conteúdo com retenção mínima de 6 meses, relatório semestral de transparência (limiar de 1 milhão de usuários menores), representante legal no Brasil, exposição ao regime sancionatório do art. 35
- `notes`: o arquivo do módulo é `legal/eca-digital.md` — trata-se de módulo normativo derivado de lei própria, não de um diretório de domínio técnico. Todo `finding` deve citar o dispositivo do ECA Digital e o correlato na LGPD.
