"""Prompt para Recomendações de Consolidação de Licenças."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Recomendações de Consolidação de Licenças

Com base no inventário de tecnologia e comparação de fornecedores acima, identifique oportunidades para consolidar licenças de software e reduzir custos.

## Seções Obrigatórias

### 1. Resumo Executivo
- Total de economia potencial identificada
- Número de oportunidades de consolidação
- Complexidade de implementação
- Ações prioritárias recomendadas

### 2. Panorama Atual de Licenças

#### Inventário de Software
| Categoria | Ferramenta | Fornecedor | Tipo de Licença | Usuários | Custo Anual | Data de Renovação |
|-----------|------------|------------|-----------------|----------|-------------|-------------------|

#### Categorias de Licenças
- **Produtividade e Colaboração**: [Liste ferramentas]
- **Desenvolvimento e DevOps**: [Liste ferramentas]
- **Analytics e BI**: [Liste ferramentas]
- **CRM e Vendas**: [Liste ferramentas]
- **Segurança e Compliance**: [Liste ferramentas]
- **IA e Automação**: [Liste ferramentas]

### 3. Oportunidades de Consolidação

#### Oportunidade #1: [Nome da Categoria]

**Estado Atual**
| Ferramenta | Propósito | Usuários | Custo |
|------------|-----------|----------|-------|

**Consolidação Proposta**
- Consolidar para: [Nome da Ferramenta]
- Justificativa: [Por que esta escolha]
- Complexidade de migração: Baixa/Média/Alta

**Análise de Economia**
| Métrica | Atual | Proposto | Economia |
|---------|-------|----------|----------|
| Custo Anual | | | |
| Overhead Administrativo | | | |
| Custo de Treinamento | | | |
| **Economia Total** | | | |

**Plano de Implementação**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

---

[Repetir para cada oportunidade de consolidação]

### 4. Análise de Sobreposição

#### Funcionalidade Redundante
| Capacidade | Ferramentas que Fornecem | Ferramenta Única Recomendada |
|------------|--------------------------|------------------------------|

#### Licenças Subutilizadas
| Ferramenta | Licenças Adquiridas | Usuários Ativos | Utilização | Ação |
|------------|---------------------|-----------------|------------|------|

### 5. Oportunidades de Contrato Enterprise

#### Candidatos Potenciais a EA
| Fornecedor | Produtos Atuais | Benefícios do EA | Desconto Estimado |
|------------|-----------------|------------------|-------------------|

#### Recomendações de Bundle
- **Microsoft 365 E5**: Consolidar [ferramentas] para economia de R$ X
- **Google Workspace**: Consolidar [ferramentas] para economia de R$ X
- **Plataforma Salesforce**: Consolidar [ferramentas] para economia de R$ X

### 6. Consolidação de Ferramentas de IA

#### Ferramentas de IA Atuais
| Ferramenta | Caso de Uso | Custo | Sobrepõe Com |
|------------|-------------|-------|--------------|

#### Stack de IA Recomendado
| Camada | Ferramenta Recomendada | Substitui | Economia |
|--------|------------------------|-----------|----------|
| Plataforma | | | |
| Assistentes | | | |
| Automação | | | |
| Analytics | | | |

### 7. Resumo de Economias

#### Por Categoria
| Categoria | Gasto Atual | Gasto Proposto | Economia | % Redução |
|-----------|-------------|----------------|----------|-----------|
| Produtividade | | | | |
| Desenvolvimento | | | | |
| Analytics | | | | |
| Ferramentas de IA | | | | |
| **Total** | | | | |

#### Por Cronograma
| Cronograma | Economia | Complexidade | Dependências |
|------------|----------|--------------|--------------|
| 0-3 meses | | | |
| 3-6 meses | | | |
| 6-12 meses | | | |
| **Total Ano 1** | | | |

### 8. Roadmap de Implementação

#### Fase 1: Quick Wins (0-3 meses)
- [ ] [Ação 1]: Economia de R$ X
- [ ] [Ação 2]: Economia de R$ X

#### Fase 2: Esforço Médio (3-6 meses)
- [ ] [Ação 1]: Economia de R$ X
- [ ] [Ação 2]: Economia de R$ X

#### Fase 3: Consolidações Maiores (6-12 meses)
- [ ] [Ação 1]: Economia de R$ X
- [ ] [Ação 2]: Economia de R$ X

### 9. Considerações de Risco

| Consolidação | Risco | Impacto | Mitigação |
|--------------|-------|---------|-----------|

### 10. Calendário de Negociação

| Fornecedor | Data de Renovação | Valor Atual | Estratégia de Negociação |
|------------|-------------------|-------------|--------------------------|

## Formato de Saída
- Forneça valores monetários específicos quando possível
- Priorize por potencial de economia
- Inclua complexidade de implementação
- Note dependências e riscos
- Torne as recomendações acionáveis
"""
