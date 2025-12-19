"""Prompt para Calculadora de ROI e Análise de Custos."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Calculadora de ROI e Análise de Custos

Com base nos quick wins e biblioteca de casos de uso acima, crie uma análise de ROI abrangente usando o framework de ROI do Google Cloud e benchmarks do setor.

## Seções Obrigatórias

### 1. Resumo Executivo
- ROI projetado total (Ano 1)
- Período de payback
- Valor Presente Líquido (3 anos)
- Principais direcionadores de valor
- Requisitos de investimento

### 2. Visão Geral do Framework de ROI

Usando o framework de criação de valor:
- **Ganhos de Eficiência**: Economia de tempo e custos
- **Aumento de Receita**: Nova receita ou aumento de vendas
- **Redução de Risco**: Custos evitados e compliance
- **Valor Estratégico**: Vantagem competitiva e inovação

### 3. Requisitos de Investimento

#### Custos de Tecnologia
| Categoria | Ano 1 | Ano 2 | Ano 3 | Total |
|-----------|-------|-------|-------|-------|
| Licenças de Plataforma de IA | | | | |
| Infraestrutura | | | | |
| Integração | | | | |
| Segurança/Compliance | | | | |
| **Subtotal** | | | | |

#### Custos de Implementação
| Categoria | Ano 1 | Ano 2 | Ano 3 | Total |
|-----------|-------|-------|-------|-------|
| Consultoria/Serviços Profissionais | | | | |
| Tempo da Equipe Interna | | | | |
| Treinamento e Gestão de Mudanças | | | | |
| Contingência (15%) | | | | |
| **Subtotal** | | | | |

#### Custos Contínuos
| Categoria | Ano 1 | Ano 2 | Ano 3 | Total |
|-----------|-------|-------|-------|-------|
| Manutenção e Suporte | | | | |
| Atualizações/Retreinamento de Modelos | | | | |
| Computação Adicional | | | | |
| **Subtotal** | | | | |

**Investimento Total**: R$ [X] em 3 anos

### 4. Análise de Criação de Valor

#### Ganhos de Eficiência
| Iniciativa | Métrica | Atual | Melhorado | Economia/Ano |
|------------|---------|-------|-----------|--------------|
| [Caso de Uso 1] | Horas economizadas | | | |
| [Caso de Uso 2] | Redução de custos | | | |
| [Caso de Uso 3] | Redução de erros | | | |

**Total de Ganhos de Eficiência**: R$ [X]/ano

#### Aumento de Receita
| Iniciativa | Métrica | Atual | Melhorado | Receita/Ano |
|------------|---------|-------|-----------|-------------|
| [Caso de Uso 1] | Taxa de conversão | | | |
| [Caso de Uso 2] | Velocidade de negócios | | | |
| [Caso de Uso 3] | Retenção de clientes | | | |

**Total de Aumento de Receita**: R$ [X]/ano

#### Redução de Risco
| Iniciativa | Tipo de Risco | Probabilidade | Impacto | Custo Evitado |
|------------|---------------|---------------|---------|---------------|
| [Caso de Uso 1] | Compliance | | | |
| [Caso de Uso 2] | Segurança | | | |
| [Caso de Uso 3] | Operacional | | | |

**Total de Redução de Risco**: R$ [X]/ano

### 5. Cálculos de ROI

#### ROI Simples
```
Benefícios Totais (Ano 1): R$ [X]
Investimento Total (Ano 1): R$ [Y]
ROI = (Benefícios - Investimento) / Investimento × 100
ROI = [Z]%
```

#### Período de Payback
```
Investimento Total: R$ [X]
Benefícios Mensais: R$ [Y]
Período de Payback: [Z] meses
```

#### Valor Presente Líquido (3 Anos)
| Ano | Benefícios | Custos | Líquido | Fator de Desconto | VPL |
|-----|------------|--------|---------|-------------------|-----|
| 0 | | | | 1,00 | |
| 1 | | | | 0,91 | |
| 2 | | | | 0,83 | |
| 3 | | | | 0,75 | |
| **Total** | | | | | |

(Usando taxa de desconto de 10%)

### 6. Análise por Iniciativa

| Iniciativa | Investimento | Valor Ano 1 | ROI | Payback | Prioridade |
|------------|--------------|-------------|-----|---------|------------|
| Quick Win 1 | | | | | |
| Quick Win 2 | | | | | |
| Projeto Principal 1 | | | | | |
| **Total** | | | | | |

### 7. Análise de Sensibilidade

#### Cenário Otimista
- Premissas: [Lista]
- ROI: [X]%
- VPL: R$ [X]

#### Cenário Base
- Premissas: [Lista]
- ROI: [X]%
- VPL: R$ [X]

#### Cenário Conservador
- Premissas: [Lista]
- ROI: [X]%
- VPL: R$ [X]

### 8. Benchmarks do Setor

| Métrica | Projeção da Empresa | Média do Setor | Quartil Superior |
|---------|---------------------|----------------|------------------|
| ROI de IA | | | |
| Período de Payback | | | |
| Ganho de Produtividade | | | |

### 9. Cronograma de Realização de Valor

| Marco | Cronograma | Valor Liberado | Acumulado |
|-------|------------|----------------|-----------|
| Primeiro Quick Win | Mês 2 | | |
| Quick Wins Completos | Mês 4 | | |
| Fase de Escala | Mês 8 | | |
| Valor Total | Mês 12 | | |

### 10. Recomendações

#### Prioridades de Investimento
1. [Iniciativa de maior ROI]
2. [Segunda maior]
3. [Terceira maior]

#### Ações de Captura de Valor
- Rastrear métricas desde o dia 1
- Estabelecer medições de baseline
- Reportar progresso mensalmente
- Ajustar com base nos resultados reais

## Formato de Saída
- Use valores monetários específicos
- Mostre metodologia de cálculo
- Inclua faixas de sensibilidade
- Referencie benchmarks do setor
- Torne as premissas explícitas
"""
