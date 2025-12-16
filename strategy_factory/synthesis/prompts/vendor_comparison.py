"""Prompt for Vendor Comparison & Build vs Buy Framework."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Comparativo de Fornecedores e Framework Build vs Buy

Com base no inventário tecnológico e nos casos de uso identificados acima, crie uma análise abrangente de comparação de fornecedores e análise de construir versus comprar.

## Seções Obrigatórias

### 1. Resumo Executivo
- Principais recomendações de fornecedores por categoria
- Recomendações de construir vs comprar
- Custo total de propriedade estimado
- Fatores críticos de decisão

### 2. Comparativo de Plataformas de IA

#### Plataformas Enterprise de IA
| Fornecedor | Pontos Fortes | Pontos Fracos | Melhor Para | Modelo de Precificação |
|------------|---------------|---------------|-------------|------------------------|
| Microsoft Azure AI | | | | |
| Google Cloud AI | | | | |
| AWS AI Services | | | | |
| OpenAI/ChatGPT Enterprise | | | | |
| Anthropic Claude | | | | |

#### Ferramentas por Categoria

**Processamento de Documentos**
| Fornecedor | Funcionalidades | Integração | Precificação | Score de Adequação |
|------------|-----------------|------------|--------------|-------------------|

**IA Conversacional**
| Fornecedor | Funcionalidades | Integração | Precificação | Score de Adequação |
|------------|-----------------|------------|--------------|-------------------|

**Analytics & BI**
| Fornecedor | Funcionalidades | Integração | Precificação | Score de Adequação |
|------------|-----------------|------------|--------------|-------------------|

**Automação de Processos**
| Fornecedor | Funcionalidades | Integração | Precificação | Score de Adequação |
|------------|-----------------|------------|--------------|-------------------|

### 3. Framework Build vs Buy

#### Matriz de Decisão
Para cada caso de uso, avaliar:

| Fator | Peso | Score Construir | Score Comprar |
|-------|------|-----------------|---------------|
| Tempo para Valor | 25% | | |
| Custo Total (3 anos) | 20% | | |
| Necessidade de Customização | 15% | | |
| Valor Estratégico | 15% | | |
| Capacidade Interna | 10% | | |
| Carga de Manutenção | 10% | | |
| Nível de Risco | 5% | | |
| **Total Ponderado** | 100% | | |

#### Recomendações por Caso de Uso

| Caso de Uso | Recomendação | Justificativa | Fornecedor (se Comprar) |
|-------------|--------------|---------------|-------------------------|

### 4. Critérios de Avaliação de Fornecedores

#### Requisitos Obrigatórios
- [ ] Conformidade SOC 2
- [ ] Opções de residência de dados
- [ ] Disponibilidade de API
- [ ] Integração SSO
- [ ] Logs de auditoria

#### Requisitos Desejáveis
- [ ] Treinamento de modelo customizado
- [ ] Opção on-premise
- [ ] Capacidade white-label
- [ ] Suporte 24/7

### 5. Análise de Custos

#### Cenário Construir (Desenvolvimento Interno)
| Categoria de Custo | Ano 1 | Ano 2 | Ano 3 | Total |
|--------------------|-------|-------|-------|-------|
| Desenvolvimento | | | | |
| Infraestrutura | | | | |
| Manutenção | | | | |
| Treinamento | | | | |
| **Total** | | | | |

#### Cenário Comprar (Solução de Fornecedor)
| Categoria de Custo | Ano 1 | Ano 2 | Ano 3 | Total |
|--------------------|-------|-------|-------|-------|
| Licenciamento | | | | |
| Implementação | | | | |
| Integração | | | | |
| Treinamento | | | | |
| **Total** | | | | |

### 6. Lista de Fornecedores Selecionados

#### Fornecedores Primários Recomendados
1. **[Nome do Fornecedor]** - [Categoria]
   - Por quê: [Justificativa]
   - Score de adequação: X/10
   - Custo estimado: R$ X/ano

2. **[Nome do Fornecedor]** - [Categoria]
   - Por quê: [Justificativa]
   - Score de adequação: X/10
   - Custo estimado: R$ X/ano

#### Recomendados para Avaliação
- [Fornecedor]: Agendar demo para [caso de uso]
- [Fornecedor]: POC para [caso de uso]

### 7. Considerações de Integração

#### Compatibilidade com Stack Atual
| Fornecedor | Integração CRM | Integração ERP | Data Warehouse | Auth/SSO |
|------------|----------------|----------------|----------------|----------|

#### API & Extensibilidade
| Fornecedor | REST API | Webhooks | SDK | Modelos Custom |
|------------|----------|----------|-----|----------------|

### 8. Avaliação de Riscos

| Fornecedor | Risco do Fornecedor | Risco de Lock-in | Risco de Segurança | Mitigação |
|------------|---------------------|------------------|-------------------|-----------|

### 9. Orientações para Negociação

#### Pontos de Alavancagem
- Descontos por compromisso multi-ano
- Faixas de preço por volume
- Oportunidades de bundling
- Alternativas competitivas

#### Termos-Chave para Negociar
- Cláusulas de portabilidade de dados
- Garantias de SLA
- Proteção de preço
- Provisões de saída

### 10. Resumo de Recomendações

| Categoria | Recomendação | Fornecedor | Ação |
|-----------|--------------|------------|------|
| Plataforma | Construir/Comprar | [Nome] | [Próximo passo] |
| Document AI | Construir/Comprar | [Nome] | [Próximo passo] |
| IA Conversacional | Construir/Comprar | [Nome] | [Próximo passo] |

## Formato de Saída
- Use tabelas comparativas extensivamente
- Inclua nomes específicos de fornecedores
- Forneça estimativas de custo quando possível
- Faça recomendações claras e acionáveis
- Anote as premissas nos cálculos de custo
"""
