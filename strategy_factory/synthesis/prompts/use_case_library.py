"""Prompt para Biblioteca de Casos de Uso por Departamento."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Biblioteca de Casos de Uso por Departamento

Com base na análise de pontos de dor, panorama tecnológico e contexto do setor acima, crie uma biblioteca abrangente de casos de uso de IA organizados por departamento.

## Seções Obrigatórias

### 1. Resumo Executivo
- Total de casos de uso identificados
- Oportunidades de alta prioridade
- Potencial de valor total estimado
- Pontos de partida recomendados

### 2. Framework de Classificação de Casos de Uso

#### Matriz de Prioridade
Casos de uso são classificados por:
- **Impacto**: Potencial de valor para o negócio (Alto/Médio/Baixo)
- **Viabilidade**: Complexidade de implementação (Fácil/Médio/Difícil)
- **Prontidão**: Prontidão de dados e infraestrutura (Pronto/Algum Trabalho/Trabalho Significativo)

#### Framework TACO da KPMG para Casos de Uso Agênticos
- **T**arefa (Automação): Tarefas rotineiras e repetitivas
- **A**nálise: Interpretação de dados e insights
- **C**riação: Geração de conteúdo e ativos
- **O**rquestração: Coordenação de fluxos de trabalho multi-etapas

---

### 3. Casos de Uso de Vendas e Marketing

#### Caso de Uso VM-001: Scoring e Priorização de Leads

| Atributo | Valor |
|----------|-------|
| Categoria | Análise |
| Impacto | Alto |
| Viabilidade | Fácil |
| Tempo para Valor | 30-60 dias |

**Descrição**
Scoring de leads potencializado por IA que analisa dados de prospects, comportamento e engajamento para priorizar esforços de vendas.

**Estado Atual**
- Avaliação manual de leads
- Critérios inconsistentes
- Oportunidades perdidas

**Solução de IA**
- Modelo de ML treinado em conversões históricas
- Scoring em tempo real baseado em sinais de engajamento
- Roteamento automatizado para representantes de vendas apropriados

**Potencial de Valor**
- 20-30% de aumento nas taxas de conversão
- 15% de redução no ciclo de vendas
- Melhor alocação de recursos

**Pré-requisitos**
- Histórico de dados do CRM
- Critérios de scoring definidos
- Buy-in da equipe de vendas

**Ferramentas Recomendadas**
- Salesforce Einstein
- HubSpot AI
- Modelo de ML customizado

---

#### Caso de Uso VM-002: Personalização de Conteúdo
[Estrutura similar]

#### Caso de Uso VM-003: Otimização de Performance de Campanhas
[Estrutura similar]

#### Caso de Uso VM-004: Automação de Inteligência Competitiva
[Estrutura similar]

---

### 4. Casos de Uso de Atendimento ao Cliente

#### Caso de Uso AC-001: Roteamento Inteligente de Tickets

| Atributo | Valor |
|----------|-------|
| Categoria | Orquestração |
| Impacto | Alto |
| Viabilidade | Médio |
| Tempo para Valor | 60-90 dias |

**Descrição**
IA que analisa tickets recebidos, classifica problemas, avalia urgência e roteia para o agente mais adequado.

[Continuar com detalhes completos...]

#### Caso de Uso AC-002: Suporte via Chat com IA
[Estrutura similar]

#### Caso de Uso AC-003: Análise de Sentimento e Escalação
[Estrutura similar]

#### Caso de Uso AC-004: Atualização Automática da Base de Conhecimento
[Estrutura similar]

---

### 5. Casos de Uso de Operações

#### Caso de Uso OP-001: Geração de Documentação de Processos

| Atributo | Valor |
|----------|-------|
| Categoria | Criação |
| Impacto | Médio |
| Viabilidade | Fácil |
| Tempo para Valor | 30 dias |

[Continuar com detalhes completos...]

#### Caso de Uso OP-002: Automação de Controle de Qualidade
[Estrutura similar]

#### Caso de Uso OP-003: Otimização de Estoque
[Estrutura similar]

#### Caso de Uso OP-004: Análise de Performance de Fornecedores
[Estrutura similar]

---

### 6. Casos de Uso de Finanças

#### Caso de Uso FN-001: Automação de Processamento de Faturas

| Atributo | Valor |
|----------|-------|
| Categoria | Automação de Tarefa |
| Impacto | Alto |
| Viabilidade | Fácil |
| Tempo para Valor | 45 dias |

[Continuar com detalhes completos...]

#### Caso de Uso FN-002: Automação de Relatórios Financeiros
[Estrutura similar]

#### Caso de Uso FN-003: Detecção de Anomalias em Transações
[Estrutura similar]

#### Caso de Uso FN-004: Previsão de Fluxo de Caixa
[Estrutura similar]

---

### 7. Casos de Uso de Recursos Humanos

#### Caso de Uso RH-001: Triagem e Ranking de Currículos

| Atributo | Valor |
|----------|-------|
| Categoria | Análise |
| Impacto | Alto |
| Viabilidade | Fácil |
| Tempo para Valor | 30 dias |

[Continuar com detalhes completos...]

#### Caso de Uso RH-002: Assistente de Onboarding de Funcionários
[Estrutura similar]

#### Caso de Uso RH-003: Análise de Avaliação de Desempenho
[Estrutura similar]

#### Caso de Uso RH-004: Personalização de Trilhas de Aprendizagem
[Estrutura similar]

---

### 8. Casos de Uso de TI e Engenharia

#### Caso de Uso TI-001: Assistência em Revisão de Código

| Atributo | Valor |
|----------|-------|
| Categoria | Análise |
| Impacto | Médio |
| Viabilidade | Fácil |
| Tempo para Valor | 14 dias |

[Continuar com detalhes completos...]

#### Caso de Uso TI-002: Automação de Resposta a Incidentes
[Estrutura similar]

#### Caso de Uso TI-003: Geração de Documentação
[Estrutura similar]

#### Caso de Uso TI-004: Detecção de Ameaças de Segurança
[Estrutura similar]

---

### 9. Casos de Uso Transversais

#### Caso de Uso TR-001: Sumarização de Reuniões

| Atributo | Valor |
|----------|-------|
| Categoria | Criação |
| Impacto | Médio |
| Viabilidade | Fácil |
| Tempo para Valor | 7 dias |

[Continuar com detalhes completos...]

#### Caso de Uso TR-002: Assistente de Elaboração de E-mails
[Estrutura similar]

#### Caso de Uso TR-003: Assistente de Pesquisa e Análise
[Estrutura similar]

---

### 10. Matriz Resumo de Casos de Uso

| ID | Caso de Uso | Dept | Impacto | Viabilidade | Prioridade |
|----|-------------|------|---------|-------------|------------|
| VM-001 | Scoring de Leads | Vendas | Alto | Fácil | 1 |
| AC-001 | Roteamento de Tickets | Atendimento | Alto | Médio | 2 |
| FN-001 | Processamento de Faturas | Finanças | Alto | Fácil | 1 |
[Continuar para todos os casos de uso...]

### 11. Recomendações de Implementação

#### Início Rápido (Mês 1)
Baseado em impacto e viabilidade:
1. [ID do Caso de Uso]: [Nome]
2. [ID do Caso de Uso]: [Nome]
3. [ID do Caso de Uso]: [Nome]

#### Fase 2 (Meses 2-3)
[Listar casos de uso]

#### Fase 3 (Meses 4-6)
[Listar casos de uso]

### 12. Resumo de Valor

| Departamento | Casos de Uso | Valor Anual Est. | Investimento |
|--------------|--------------|------------------|--------------|
| Vendas e Marketing | X | R$ Y | R$ Z |
| Atendimento ao Cliente | X | R$ Y | R$ Z |
| Operações | X | R$ Y | R$ Z |
| Finanças | X | R$ Y | R$ Z |
| RH | X | R$ Y | R$ Z |
| TI | X | R$ Y | R$ Z |
| **Total** | | | |

## Formato de Saída
- Análise detalhada para cada caso de uso
- Estrutura consistente em todas as entradas
- Priorização baseada em valor e viabilidade
- Recomendações específicas de ferramentas
- Pré-requisitos e dependências claros
"""
