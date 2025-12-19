"""Prompt para Lista de Quick Wins."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Lista de Quick Wins

Com base na biblioteca de casos de uso e avaliação de maturidade fornecidos acima, identifique e priorize quick wins de IA que podem ser implementados em 30-60 dias.

## Seções Obrigatórias

### 1. Resumo Executivo
- Total de quick wins identificados
- Valor combinado estimado
- Resumo de requisitos de recursos
- Ponto de partida recomendado

### 2. Critérios de Seleção de Quick Wins

Explique os critérios utilizados:
- Tempo de implementação: < 60 dias
- Investimento: < R$ 250K (ou recursos internos)
- Nível de risco: Baixo
- Potencial de valor: ROI demonstrável
- Pré-requisitos: Mínimos

### 3. Top 10 Quick Wins

Para cada quick win, forneça:

---

#### Quick Win #1: [Nome]

**Visão Geral**
| Atributo | Valor |
|----------|-------|
| Departamento | |
| Tempo de Implementação | |
| Investimento Estimado | |
| ROI Esperado | |
| Nível de Risco | Baixo/Médio |
| Pré-requisitos | |

**Descrição**
[Descrição de 2-3 frases da iniciativa]

**Estado Atual**
- Como isso é feito hoje?
- Pontos de dor endereçados

**Solução Proposta**
- Abordagem de IA/automação
- Recomendação de ferramenta/plataforma
- Abordagem de implementação

**Passos de Implementação**
1. Semana 1: [Atividade]
2. Semana 2: [Atividade]
3. Semana 3-4: [Atividade]
4. Semana 5-6: [Lançamento e otimização]

**Métricas de Sucesso**
- KPI Primário: [Métrica e meta]
- KPIs Secundários: [Lista]

**Recursos Necessários**
- Internos: [Funções/tempo]
- Externos: [Ferramentas/fornecedores]
- Orçamento: R$ [X]

---

[Repetir para Quick Wins #2-10]

### 4. Matriz de Comparação de Quick Wins

| # | Quick Win | Dept | Tempo | Investimento | ROI | Risco | Prioridade |
|---|-----------|------|-------|--------------|-----|-------|------------|
| 1 | | | | | | | |
| 2 | | | | | | | |
[...]

### 5. Sequência de Implementação

Ordem recomendada de implementação:

```
Mês 1: Quick Wins 1, 2, 3
Mês 2: Quick Wins 4, 5, 6
Mês 3: Quick Wins 7, 8, 9, 10
```

Justificativa para sequenciamento:
- Dependências entre wins
- Otimização de recursos
- Construção de aprendizado e momentum

### 6. Oportunidades de Compartilhamento de Recursos

Identifique onde quick wins podem compartilhar:
- Ferramentas e plataformas
- Treinamento e gestão de mudanças
- Dados e integrações
- Recursos de equipe

### 7. Mitigação de Riscos

Riscos comuns e mitigação:
| Risco | Quick Wins Afetados | Mitigação |
|-------|---------------------|-----------|

### 8. Dashboard de Acompanhamento de Sucesso

Dashboard de métricas proposto:
| Quick Win | Status | Progresso | Valor Realizado |
|-----------|--------|-----------|-----------------|

### 9. Caminho de Escalação

Se um quick win encontrar obstáculos:
1. Semana 1-2: Equipe do projeto resolve
2. Semana 3: Escalar para sponsor
3. Semana 4+: Reavaliar ou pivotar

### 10. Preview da Próxima Onda

Quick wins que não entraram na lista mas devem ser considerados em seguida:
- [Nome da iniciativa]: Por que não agora, o que é necessário

## Formato de Saída
- Forneça análise detalhada para cada quick win
- Use formatação consistente em todas as entradas
- Inclua números específicos para estimativas de ROI
- Torne os passos de implementação acionáveis
- Priorize baseado em valor e viabilidade
"""
