"""Prompt para Template de Política de Uso Aceitável de IA."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Template de Política de Uso Aceitável de IA

Com base no contexto da empresa, regulamentações do setor e requisitos de governança acima, crie uma Política de Uso Aceitável de IA abrangente.

## Seções Obrigatórias

### 1. Visão Geral da Política

#### Propósito
Esta política estabelece diretrizes para o uso responsável de ferramentas e tecnologias de Inteligência Artificial (IA) na {company_name}.

#### Escopo
- Todos os funcionários, contratados e terceiros
- Todas as ferramentas de IA (internas e externas)
- Todos os casos de uso envolvendo IA

#### Data de Vigência
{current_date}

### 2. Definições

| Termo | Definição |
|-------|-----------|
| Inteligência Artificial (IA) | |
| IA Generativa | |
| Modelo de Machine Learning | |
| Conteúdo Gerado por IA | |
| Prompt | |
| Dados de Treinamento | |

### 3. Ferramentas de IA Aprovadas

#### Ferramentas Sancionadas
| Ferramenta | Casos de Uso Aprovados | Restrições | Classificação de Dados |
|------------|------------------------|------------|------------------------|
| [Ferramenta 1] | | | |
| [Ferramenta 2] | | | |

#### Processo de Avaliação para Novas Ferramentas
1. Enviar solicitação para [equipe/função]
2. Revisão de segurança
3. Avaliação de impacto de privacidade
4. Processo de aprovação

### 4. Diretrizes de Uso Aceitável

#### Usos Permitidos
- [Listar casos de uso permitidos]
- [Pesquisa e análise]
- [Elaboração de conteúdo]
- [Assistência em código]
- [Análise de dados]

#### Usos Proibidos
- [ ] Processar dados pessoais de clientes sem aprovação
- [ ] Gerar conteúdo para documentos legais/compliance sem revisão
- [ ] Treinar modelos com dados proprietários da empresa
- [ ] Compartilhar informações confidenciais com ferramentas de IA externas
- [ ] Tomada de decisão automatizada que afete indivíduos
- [ ] [Proibições específicas do setor]

### 5. Classificação de Dados e IA

#### Tratamento de Dados por Classificação

| Classificação | Pode Usar com IA? | Requisitos |
|---------------|-------------------|------------|
| Público | Sim | Nenhum |
| Interno | Sim | Apenas ferramentas aprovadas |
| Confidencial | Limitado | Aprovação necessária |
| Restrito | Não | Proibido |

#### Tipos de Dados Sensíveis
Nunca inserir em ferramentas de IA sem aprovação explícita:
- Informações pessoais de clientes
- Informações pessoais de funcionários
- Dados financeiros
- Informações de saúde (se aplicável)
- Segredos comerciais
- Informações com privilégio legal

### 6. Requisitos de Revisão de Conteúdo

#### Matriz de Revisão de Conteúdo Gerado por IA

| Tipo de Conteúdo | Revisão Necessária | Aprovador |
|------------------|-------------------|-----------|
| Comunicações externas | Sim | [Função] |
| Materiais voltados ao cliente | Sim | [Função] |
| Documentação interna | Não | Próprio |
| Código | Sim | Revisão por pares |
| Legal/Compliance | Sim | Equipe jurídica |

#### Requisitos de Atribuição
- Divulgar assistência de IA quando exigido por [contexto]
- Manter registros de conteúdo gerado por IA

### 7. Requisitos de Segurança

#### Autenticação
- Usar SSO da empresa quando disponível
- Nunca compartilhar credenciais
- Habilitar MFA onde suportado

#### Proteção de Dados
- Usar métodos aprovados de transferência de dados
- Criptografar comunicações sensíveis
- Registrar uso de ferramentas de IA

#### Comunicação de Incidentes
Reportar imediatamente:
- Incidentes de exposição de dados
- Comportamento inesperado de IA
- Violações de política

Contato: [Contato da equipe de segurança]

### 8. Considerações de Compliance

#### Requisitos Regulatórios
Com base no contexto do setor:
- [Regulamentação 1]: [Requisitos]
- [Regulamentação 2]: [Requisitos]
- [Regulamentações específicas de IA]: [Requisitos]

#### Auditoria e Monitoramento
- O uso de IA pode ser monitorado
- Logs retidos por [X] meses
- Revisão anual de compliance da política

### 9. Papéis e Responsabilidades

| Papel | Responsabilidades |
|-------|-------------------|
| Todos os Funcionários | Seguir a política, reportar problemas |
| Gestores | Garantir compliance da equipe |
| TI/Segurança | Avaliação de ferramentas, monitoramento |
| Jurídico/Compliance | Atualizações de política, orientação |
| Comitê de IA | Estratégia, governança |

### 10. Requisitos de Treinamento

| Papel | Treinamento | Frequência |
|-------|-------------|------------|
| Todos os funcionários | Básico de IA e política | Anual |
| Usuários avançados | Ferramentas avançadas de IA | Semestral |
| Desenvolvedores | Diretrizes de desenvolvimento de IA | Conforme necessário |

### 11. Violações de Política

#### Consequências
- Primeira violação: Orientação
- Segunda violação: Advertência escrita
- Violação grave: Ação disciplinar

#### Reportando Violações
- Linha anônima: [Contato]
- Reporte direto: [Contato]

### 12. Governança da Política

#### Ciclo de Revisão
- Revisão trimestral para atualizações
- Revisão anual abrangente

#### Gestão de Mudanças
- Mudanças comunicadas via [canal]
- Aviso de 30 dias para mudanças significativas

#### Dúvidas e Exceções
Contato: [Contato da Equipe de Governança de IA]

---

## Termo de Reconhecimento

Eu li e compreendo a Política de Uso Aceitável de IA. Concordo em cumprir seus termos.

Nome do Funcionário: _________________
Assinatura do Funcionário: _________________
Data: _________________

## Formato de Saída
- Use linguagem profissional de política
- Inclua exemplos específicos quando útil
- Customize com base no contexto do setor
- Torne os requisitos claros e acionáveis
- Inclua seção de termo de reconhecimento
"""
