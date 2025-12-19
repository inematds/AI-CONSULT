"""Prompt para Modelo de Maturidade de IA e Avaliação de Prontidão."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Modelo de Maturidade de IA e Avaliação de Prontidão

Com base na pesquisa e contexto fornecidos acima, crie uma avaliação abrangente de maturidade de IA usando o framework da Curva de Maturidade de IA da BCG e outros padrões do setor.

## Seções Obrigatórias

### 1. Resumo Executivo
- Nível de maturidade atual (escala 1-5)
- Principais forças e lacunas
- Áreas de foco recomendadas
- Cronograma estimado para próximo nível de maturidade

### 2. Avaliação de Maturidade de IA

#### Posição na Curva de Maturidade de IA da BCG

Avalie a empresa em relação a estes estágios:
1. **Passivo** - Sem iniciativas de IA, processos tradicionais
2. **Consciente** - Explorando IA, pilotos iniciais
3. **Ativo** - Múltiplos projetos de IA, alguns em produção
4. **Operacional** - IA integrada aos processos centrais
5. **Transformacional** - Organização nativa de IA, vantagem competitiva

**Avaliação Atual:** [Estágio X]

Forneça evidências da pesquisa que suportam esta avaliação.

### 3. Análise Dimensão por Dimensão

Avalie cada dimensão em uma escala de 1-5:

| Dimensão | Score | Evidências | Análise de Lacunas |
|----------|-------|------------|-------------------|
| Estratégia e Visão | | | |
| Dados e Infraestrutura | | | |
| Tecnologia e Ferramentas | | | |
| Talentos e Habilidades | | | |
| Governança e Ética | | | |
| Cultura e Mudança | | | |
| Casos de Uso e Valor | | | |

#### Análise Detalhada por Dimensão

Para cada dimensão, forneça:

##### Estratégia e Visão (X/5)
- Observações do estado atual
- Forças identificadas
- Lacunas e fraquezas
- Recomendações

##### Dados e Infraestrutura (X/5)
- Disponibilidade e qualidade de dados
- Prontidão de infraestrutura
- Capacidades de integração
- Recomendações

##### Tecnologia e Ferramentas (X/5)
- Ferramentas atuais de IA/ML
- Maturidade de plataforma
- Considerações de dívida técnica
- Recomendações

##### Talentos e Habilidades (X/5)
- Expertise em IA interna
- Programas de treinamento
- Parcerias externas
- Recomendações

##### Governança e Ética (X/5)
- Políticas de IA em vigor
- Abordagem de gestão de riscos
- Considerações de compliance
- Recomendações

##### Cultura e Mudança (X/5)
- Prontidão para mudança
- Cultura de inovação
- Apoio da liderança
- Recomendações

##### Casos de Uso e Valor (X/5)
- Casos de uso de IA atuais
- Realização de valor
- Abordagem de escala
- Recomendações

### 4. Gráfico Radar de Maturidade

Forneça dados para visualização de gráfico radar:
```
Estratégia e Visão: X
Dados e Infraestrutura: X
Tecnologia e Ferramentas: X
Talentos e Habilidades: X
Governança e Ética: X
Cultura e Mudança: X
Casos de Uso e Valor: X
```

### 5. Comparação com Pares

Compare com benchmarks do setor:
| Dimensão | Score da Empresa | Média do Setor | Lacuna |
|----------|------------------|----------------|--------|

### 6. Avaliação de Prontidão

#### Prontidão Imediata (Pronto para Iniciar)
Liste iniciativas de IA que a empresa poderia começar imediatamente.

#### Prontidão de Curto Prazo (3-6 meses)
Liste iniciativas de IA que requerem alguma preparação.

#### Prontidão de Longo Prazo (6-12 meses)
Liste iniciativas de IA que requerem investimento significativo.

### 7. Roadmap de Melhoria de Maturidade

#### Para alcançar o próximo nível de maturidade:
- Iniciativas-chave necessárias
- Áreas de investimento
- Estimativa de cronograma
- Fatores críticos de sucesso

## Formato de Saída
- Use tabelas markdown conforme especificado
- Inclua scores numéricos para avaliação quantitativa
- Forneça evidências específicas da pesquisa
- Seja realista sobre lacunas e desafios
- Torne as recomendações acionáveis
"""
