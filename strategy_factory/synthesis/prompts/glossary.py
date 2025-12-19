"""Prompt para Glossário de Termos de IA."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Glossário de Termos de IA

Crie um glossário abrangente de termos de IA e tecnologia relevantes para a jornada de IA da {company_name}.

## Seções Obrigatórias

### 1. Introdução

Este glossário fornece definições para termos-chave relacionados à inteligência artificial, machine learning e tecnologias de dados. Foi desenvolvido para ajudar todos os membros da equipe na {company_name} a se comunicarem efetivamente sobre iniciativas de IA.

---

### 2. Conceitos Fundamentais de IA

#### A

**IA Agêntica**
Sistemas de IA capazes de ação autônoma e tomada de decisão sem intervenção humana constante. Esses sistemas podem planejar, executar e ajustar estratégias para alcançar objetivos.

**Inteligência Artificial Geral (IAG)**
IA hipotética com raciocínio e resolução de problemas em nível humano em qualquer domínio. Os sistemas de IA atuais são IA "estreita", destacando-se em tarefas específicas.

**Inteligência Artificial (IA)**
Sistemas computacionais projetados para realizar tarefas que tipicamente requerem inteligência humana, incluindo percepção visual, reconhecimento de fala, tomada de decisão e tradução de idiomas.

#### B

**Viés (em IA)**
Erros sistemáticos em resultados de IA que refletem preconceitos nos dados de treinamento ou no design do algoritmo. Pode levar a resultados injustos para certos grupos.

#### C

**Chatbot**
Aplicação de software que simula conversação humana através de interações por texto ou voz. Chatbots modernos frequentemente usam modelos de linguagem grandes.

**Visão Computacional**
Capacidade de IA para interpretar e entender informações visuais de imagens ou vídeos, permitindo tarefas como detecção de objetos e reconhecimento facial.

#### D

**Data Lake**
Repositório centralizado que armazena dados brutos em seu formato nativo até serem necessários para análise. Permite exploração flexível de dados e treinamento de IA.

**Deep Learning**
Subconjunto de machine learning usando redes neurais com múltiplas camadas. Alimenta capacidades avançadas de IA como reconhecimento de imagem e compreensão de linguagem.

#### E

**Embeddings**
Representações numéricas de texto, imagens ou outros dados que capturam significado semântico. Permite que a IA encontre similaridades e relacionamentos.

#### F

**Fine-tuning**
Processo de adaptar um modelo de IA pré-treinado para uma tarefa ou domínio específico, treinando-o em dados adicionais relevantes.

**Modelo de Fundação**
Modelo grande de IA treinado em dados amplos que pode ser adaptado para várias tarefas. Exemplos: GPT-4, Claude, Gemini.

#### G

**IA Generativa**
Sistemas de IA que criam novo conteúdo (texto, imagens, código, áudio) baseado em padrões aprendidos. A tecnologia por trás do ChatGPT e ferramentas similares.

**GPT (Generative Pre-trained Transformer)**
Arquitetura que alimenta muitos modelos de linguagem grandes. Pré-treinado em vastos dados de texto, depois ajustado para aplicações específicas.

#### H

**Alucinação**
Quando a IA gera informação que soa plausível mas é falsa ou fabricada. Consideração importante para todas as aplicações de IA generativa.

#### I

**Inferência**
O processo de usar um modelo de IA treinado para fazer previsões ou gerar resultados em novos dados.

#### L

**Modelo de Linguagem Grande (LLM)**
Modelo de IA treinado em conjuntos massivos de dados de texto para entender e gerar linguagem humana. Alimenta chatbots e assistentes de escrita.

#### M

**Machine Learning (ML)**
Subconjunto de IA onde sistemas aprendem com dados para melhorar performance sem programação explícita. Fundação para a maioria das aplicações modernas de IA.

**Modelo**
Representação matemática aprendida com dados que pode fazer previsões ou gerar resultados. O componente central dos sistemas de IA.

#### N

**Processamento de Linguagem Natural (PLN)**
Capacidade de IA para entender, interpretar e gerar linguagem humana. Permite chatbots, tradução e análise de sentimento.

**Rede Neural**
Sistema computacional inspirado em neurônios biológicos. Aprende padrões através de nós interconectados processando informação.

#### P

**Prompt**
Texto de entrada ou instruções dadas a um modelo de IA generativa. A qualidade do prompt afeta significativamente a qualidade do resultado.

**Engenharia de Prompt**
A prática de projetar prompts eficazes para obter os resultados desejados de modelos de IA.

#### R

**RAG (Geração Aumentada por Recuperação)**
Técnica que combina geração de texto por IA com recuperação de informação de bases de conhecimento. Reduz alucinações ao fundamentar respostas em dados reais.

**RLHF (Aprendizado por Reforço com Feedback Humano)**
Técnica de treinamento usando preferências humanas para melhorar o comportamento do modelo de IA e alinhamento com expectativas dos usuários.

#### S

**Análise de Sentimento**
Técnica de IA para determinar o tom emocional em texto. Usado para análise de feedback de clientes e monitoramento de redes sociais.

**Aprendizado Supervisionado**
Abordagem de machine learning usando dados de treinamento rotulados. O modelo aprende a mapear entradas para saídas conhecidas.

#### T

**Token**
Unidade de texto processada por modelos de linguagem. Pode ser uma palavra, parte de uma palavra ou pontuação. Importante para entender precificação e limites de IA.

**Dados de Treinamento**
Conjunto de dados usado para ensinar padrões e relacionamentos a modelos de IA. Qualidade e diversidade dos dados de treinamento impactam diretamente a performance do modelo.

**Transformer**
Arquitetura de rede neural que permite processamento eficiente de dados sequenciais. Alimenta modelos de linguagem modernos.

#### U

**Aprendizado Não Supervisionado**
Abordagem de machine learning que encontra padrões em dados não rotulados. Usado para clustering, detecção de anomalias e exploração de dados.

#### V

**Banco de Dados Vetorial**
Banco de dados otimizado para armazenar e pesquisar embeddings. Permite busca semântica e capacidades de memória de IA.

---

### 3. Termos de Negócio e Estratégia

**Maturidade de IA**
Sofisticação da organização em adotar e aproveitar IA. Medida em dimensões como estratégia, dados, talentos e governança.

**Prontidão para IA**
Preparação da organização para implementar iniciativas de IA. Inclui fatores de qualidade de dados, infraestrutura, habilidades e cultura.

**Centro de Excelência (CoE)**
Equipe dedicada que fornece liderança em IA, melhores práticas e suporte em toda a organização.

**Transformação Digital**
Mudança fundamental em como uma organização opera e entrega valor através da adoção de tecnologia digital.

**MLOps**
Práticas para implantar e manter modelos de machine learning em produção de forma confiável e eficiente.

**ROI (Retorno sobre Investimento)**
Medida de lucratividade de iniciativa de IA. Calculado como (Benefícios - Custos) / Custos × 100.

**TCO (Custo Total de Propriedade)**
Custo completo de implementar e operar uma solução de IA ao longo de seu ciclo de vida.

---

### 4. Termos de Dados

**Governança de Dados**
Framework para gerenciar disponibilidade, usabilidade, integridade e segurança de dados em toda a organização.

**Data Lake**
Repositório de armazenamento que mantém grandes quantidades de dados brutos em formato nativo.

**Pipeline de Dados**
Processo automatizado que move e transforma dados de origens para destinos.

**Qualidade de Dados**
Medida de precisão, completude, consistência e confiabilidade dos dados.

**Data Warehouse**
Repositório central de dados integrados e estruturados otimizado para análise.

**ETL (Extrair, Transformar, Carregar)**
Processo de extrair dados de fontes, transformá-los e carregá-los em um sistema de destino.

**Metadados**
Dados sobre dados - descrevendo estrutura, origem, qualidade e relacionamentos.

---

### 5. Termos Técnicos

**API (Interface de Programação de Aplicações)**
Interface que permite que diferentes sistemas de software se comuniquem. Como aplicações se integram com serviços de IA.

**Computação em Nuvem**
Entrega de serviços de computação pela internet. Principais provedores: AWS, Azure, Google Cloud.

**Edge Computing**
Processamento de dados próximo à sua fonte ao invés de em nuvem centralizada. Permite aplicações de IA em tempo real.

**GPU (Unidade de Processamento Gráfico)**
Hardware que acelera treinamento e inferência de modelos de IA. Essencial para cargas de trabalho de IA computacionalmente intensivas.

**Latência**
Atraso de tempo entre entrada e resposta. Métrica crítica para aplicações de IA em tempo real.

**SaaS (Software como Serviço)**
Modelo de entrega de software baseado em nuvem. A maioria das ferramentas de IA é entregue como SaaS.

---

### 6. Termos Específicos do Setor

[Adicione termos relevantes para o setor da {company_name}]

---

### 7. Referência Rápida de Siglas

| Sigla | Termo Completo |
|-------|----------------|
| IA | Inteligência Artificial |
| IAG | Inteligência Artificial Geral |
| API | Interface de Programação de Aplicações |
| CoE | Centro de Excelência |
| ETL | Extrair, Transformar, Carregar |
| GPU | Unidade de Processamento Gráfico |
| LLM | Modelo de Linguagem Grande |
| ML | Machine Learning |
| MLOps | Operações de Machine Learning |
| PLN | Processamento de Linguagem Natural |
| RAG | Geração Aumentada por Recuperação |
| RLHF | Aprendizado por Reforço com Feedback Humano |
| ROI | Retorno sobre Investimento |
| SaaS | Software como Serviço |
| TCO | Custo Total de Propriedade |

## Formato de Saída
- Organização alfabética
- Definições claras e não técnicas
- Exemplos quando útil
- Relevância para contexto de negócios
- Incluir termos específicos do setor
"""
