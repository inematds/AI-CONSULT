"""Prompt para Kit Inicial de Biblioteca de Prompts."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Kit Inicial de Biblioteca de Prompts

Com base na biblioteca de casos de uso e análise departamental acima, crie uma biblioteca abrangente de prompts para tarefas comuns de IA.

## Seções Obrigatórias

### 1. Introdução

#### Propósito
Esta biblioteca de prompts fornece prompts prontos para uso em tarefas comuns na {company_name}, otimizados para [ferramentas de IA aprovadas].

#### Como Usar
1. Encontre a categoria relevante
2. Copie o template de prompt
3. Substitua os [marcadores entre colchetes] com suas especificidades
4. Revise e refine o resultado

#### Melhores Práticas
- Seja específico com o contexto
- Inclua exemplos quando útil
- Itere sobre os resultados
- Sempre revise conteúdo gerado por IA

### 2. Prompts de Vendas e Marketing

#### Qualificação de Leads
```
Analise estas informações do lead e forneça uma pontuação de qualificação:

Empresa: [Nome da Empresa]
Setor: [Setor]
Porte: [Número de Funcionários]
Orçamento: [Se Conhecido]
Prazo: [Se Conhecido]
Pontos de Dor: [Desafios Conhecidos]

Forneça:
1. Pontuação de qualificação (1-10)
2. Principais sinais de compra
3. Potenciais objeções
4. Próximos passos recomendados
5. Roteiro de conversa sugerido
```

#### Personalização de E-mail
```
Escreva um e-mail de prospecção personalizado para:

Prospect: [Nome, Cargo]
Empresa: [Empresa]
Setor: [Setor]
Contexto: [Notícia recente, conexão em comum, ou evento gatilho]
Nossa Proposta de Valor: [Proposta de valor relevante]

Requisitos:
- Tom profissional mas conversacional
- Menos de 150 palavras
- Call to action claro
- Referenciar o contexto específico
```

#### Análise Competitiva
```
Analise nosso concorrente [Nome do Concorrente] para o mercado de [Produto/Serviço]:

Informações disponíveis:
[Cole qualquer pesquisa, conteúdo do site, ou anotações]

Forneça:
1. Comparação de produto/serviço
2. Análise de preços (se disponível)
3. Pontos fortes e fracos
4. Objeções comuns ao competir
5. Estratégias vencedoras contra eles
```

### 3. Prompts de Atendimento ao Cliente

#### Geração de Respostas
```
Gere uma resposta para esta consulta do cliente:

Mensagem do Cliente:
[Cole a mensagem do cliente]

Contexto:
- Produto/Serviço: [Sobre o que estão perguntando]
- Histórico do Cliente: [Qualquer histórico relevante]
- Sentimento: [Frustrado/Neutro/Satisfeito]

Requisitos:
- Tom profissional e empático
- Abordar todas as preocupações
- Fornecer próximos passos claros
- Voz da marca [Empresa]
```

#### Resumo de Escalação de Problemas
```
Resuma este problema do cliente para escalação:

Cliente: [Nome/Conta]
Linha do Tempo do Problema:
[Cole a conversa ou anotações]

Forneça:
1. Resumo do problema (2-3 frases)
2. Impacto no cliente
3. Passos já realizados
4. Resolução recomendada
5. Nível de urgência (Baixo/Médio/Alto/Crítico)
```

### 4. Prompts de Operações

#### Documentação de Processos
```
Crie um procedimento operacional padrão para:

Processo: [Nome do Processo]
Propósito: [Por que este processo existe]
Passos Atuais:
[Liste os passos atuais ou descreva o processo]

Gere:
1. POP formatado com passos numerados
2. Entradas necessárias
3. Saídas esperadas
4. Exceções comuns e tratamento
5. Pontos de verificação de qualidade
```

#### Resumo de Reunião
```
Resuma esta transcrição de reunião:

Reunião: [Nome/Propósito]
Participantes: [Lista]
Transcrição:
[Cole a transcrição ou anotações]

Forneça:
1. Resumo executivo (3-5 frases)
2. Principais decisões tomadas
3. Itens de ação com responsáveis
4. Questões em aberto
5. Próximos passos
```

### 5. Prompts de Finanças

#### Narrativa de Relatório
```
Escreva um resumo narrativo para estes dados financeiros:

Tipo de Relatório: [DRE Mensal / Revisão Trimestral / etc.]
Período: [Intervalo de Datas]
Métricas Principais:
[Cole métricas e valores principais]

Gere:
1. Resumo executivo
2. Destaque tendências positivas
3. Áreas de preocupação
4. Comparação com período anterior
5. Áreas de foco recomendadas
```

#### Análise de Despesas
```
Analise estes dados de despesas e identifique oportunidades de otimização:

Dados:
[Cole o resumo de despesas ou categorias]

Forneça:
1. Principais categorias de despesas
2. Tendências mês a mês
3. Anomalias ou outliers
4. Oportunidades de consolidação
5. Ações recomendadas
```

### 6. Prompts de RH

#### Aprimoramento de Descrição de Vaga
```
Melhore esta descrição de vaga para melhor atração de candidatos:

Descrição Atual:
[Cole a descrição da vaga]

Requisitos:
- Linguagem moderna e inclusiva
- Responsabilidades claras
- Pitch atraente da empresa
- Requisitos realistas vs. diferenciais
- Otimizado para SEO em sites de emprego
```

#### Perguntas de Entrevista
```
Gere perguntas de entrevista para:

Cargo: [Título da Posição]
Nível: [Júnior/Pleno/Sênior/Executivo]
Habilidades-Chave: [Top 3-5 habilidades necessárias]
Valores da Empresa: [Valores principais a avaliar]

Forneça:
1. 5 perguntas comportamentais
2. 3 perguntas técnicas/de habilidades
3. 2 perguntas de fit cultural
4. Exemplos de perguntas de follow-up
5. Sinais de alerta a observar
```

### 7. Prompts de Engenharia/TI

#### Revisão de Código
```
Revise este código quanto às melhores práticas:

Linguagem: [Linguagem de Programação]
Propósito: [O que o código faz]
Código:
[Cole o código]

Avalie:
1. Qualidade e legibilidade do código
2. Potenciais bugs ou problemas
3. Considerações de performance
4. Preocupações de segurança
5. Melhorias sugeridas
```

#### Geração de Documentação
```
Gere documentação para este código/API:

Código/API:
[Cole o código ou especificação da API]

Gere:
1. Descrição geral
2. Parâmetros/entradas
3. Valores de retorno/saídas
4. Exemplos de uso
5. Tratamento de erros
```

### 8. Prompts de Produtividade Geral

#### Elaboração de E-mail
```
Elabore um e-mail:

Propósito: [O que você quer alcançar]
Destinatário: [Quem, seu cargo/relacionamento]
Tom: [Formal/Casual/Urgente]
Pontos Principais:
[Liste os pontos principais a cobrir]

Requisitos:
- Linha de assunto clara
- Tamanho apropriado
- Assinatura profissional
```

#### Resumo de Pesquisa
```
Resuma esta pesquisa/artigo:

Conteúdo:
[Cole o artigo ou pesquisa]

Forneça:
1. Principais descobertas (bullet points)
2. Implicações para [nosso setor/empresa]
3. Ações recomendadas
4. Tópicos relacionados para explorar
5. Avaliação de confiabilidade da fonte
```

### 9. Dicas de Engenharia de Prompts

#### Tornando Prompts Melhores
1. **Seja Específico**: Inclua contexto, restrições e formato desejado
2. **Use Exemplos**: Mostre como é um bom resultado
3. **Itere**: Refine prompts com base nos resultados
4. **Encadeie Prompts**: Divida tarefas complexas em etapas

#### Erros Comuns a Evitar
- Muito vago ou aberto demais
- Sem contexto sobre público ou propósito
- Esquecer de especificar formato
- Não revisar/editar o resultado

### 10. Template de Prompt Personalizado

```
# Prompt de [Nome da Tarefa]

## Contexto
[Informações de background que a IA precisa]

## Entrada
[O que você está fornecendo]
[Cole a entrada aqui]

## Requisitos
- [Requisito 1]
- [Requisito 2]
- [Requisito 3]

## Formato de Saída
[Especifique como você quer a resposta estruturada]

## Notas Adicionais
[Quaisquer restrições, preferências ou diretrizes]
```

## Formato de Saída
- Forneça prompts prontos para copiar e colar
- Inclua indicadores claros de marcadores [assim]
- Organize por departamento/função
- Inclua dicas de uso
- Torne os prompts customizáveis
"""
