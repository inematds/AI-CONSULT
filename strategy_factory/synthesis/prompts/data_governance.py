"""Prompt para Framework de Governança de Dados."""

PROMPT = """
**IMPORTANTE: Responda todo o conteúdo em português brasileiro.**


# Tarefa: Gerar Framework de Governança de Dados

Com base no inventário de tecnologia, contexto regulatório e política de IA acima, crie um framework abrangente de governança de dados para iniciativas de IA.

## Seções Obrigatórias

### 1. Resumo Executivo
- Avaliação de maturidade de governança de dados
- Principais riscos identificados
- Recomendações prioritárias
- Requisitos de recursos

### 2. Visão de Governança de Dados

#### Princípios
1. **Dados como Ativo**: Tratar dados como recurso estratégico
2. **Qualidade na Origem**: Garantir precisão no ponto de entrada
3. **Segurança por Design**: Construir proteção em todos os processos
4. **Transparência**: Propriedade e linhagem claras
5. **Compliance em Primeiro Lugar**: Requisitos regulatórios são inegociáveis

#### Objetivos
- Habilitar iniciativas de IA com dados confiáveis
- Minimizar riscos relacionados a dados
- Estabelecer responsabilidades claras
- Simplificar acesso a dados

### 3. Estrutura de Governança de Dados

#### Modelo Organizacional

```
[Conselho de Governança de Dados]
        |
[Escritório de Governança de Dados]
        |
    ----------
    |        |
[Stewards de Domínio] [Stewards Técnicos]
```

#### Papéis e Responsabilidades

| Papel | Responsabilidades | Reporta Para |
|-------|-------------------|--------------|
| Sponsor Executivo | Estratégia, orçamento, escalações | CEO |
| Conselho de Governança de Dados | Aprovação de políticas, prioridades | Sponsor Exec |
| Chief Data Officer | Liderança do programa | Conselho |
| Stewards de Dados de Domínio | Propriedade de dados de negócio | CDO |
| Stewards de Dados Técnicos | Qualidade de dados, metadados | CDO |
| Custodiantes de Dados | Gestão em nível de sistema | Stewards Técnicos |

### 4. Framework de Classificação de Dados

#### Níveis de Classificação

| Nível | Definição | Exemplos | Requisitos de Tratamento |
|-------|-----------|----------|--------------------------|
| Público | Livremente compartilhável | Conteúdo de marketing | Nenhum |
| Interno | Apenas uso da empresa | Organogramas, políticas | Controles de acesso |
| Confidencial | Sensível ao negócio | Dados financeiros, estratégias | Criptografia, logs |
| Restrito | Altamente sensível | PII, dados de saúde, segredos | Controles completos, aprovação |

#### Classificações Específicas para IA

| Tipo de Dado | Treinamento de IA | Entrada de IA | Saída de IA |
|--------------|-------------------|---------------|-------------|
| Dados de clientes | Proibido | Restrito | Revisão necessária |
| Dados transacionais | Com consentimento | Anonimizado | Permitido |
| Dados operacionais | Permitido | Permitido | Permitido |
| Dados públicos | Permitido | Permitido | Permitido |

### 5. Framework de Qualidade de Dados

#### Dimensões de Qualidade

| Dimensão | Definição | Medição | Meta |
|----------|-----------|---------|------|
| Precisão | Correção | Taxa de erros | <1% |
| Completude | Sem valores faltantes | Taxa de nulos | >95% |
| Consistência | Igual entre sistemas | Taxa de correspondência | >99% |
| Atualidade | Atual/atualizado | Frescor | <24 hrs |
| Unicidade | Sem duplicatas | Taxa de duplicação | <0,1% |
| Validade | Conforme regras | Taxa de validação | >99% |

#### Monitoramento de Qualidade

| Sistema | Verificações de Qualidade | Frequência | Responsável |
|---------|---------------------------|------------|-------------|
| [Sistema 1] | | Diária | |
| [Sistema 2] | | Semanal | |

### 6. Gestão do Ciclo de Vida de Dados

#### Estágios do Ciclo de Vida

| Estágio | Atividades | Controles | Retenção |
|---------|------------|-----------|----------|
| Criação | Captura, entrada | Validação | - |
| Armazenamento | Persistência | Criptografia | Por política |
| Processamento | Transformação, análise | Logging | - |
| Compartilhamento | Distribuição | Controle de acesso | - |
| Arquivamento | Armazenamento de longo prazo | Verificações de integridade | Por regulação |
| Descarte | Exclusão segura | Verificação | - |

#### Ciclo de Vida de Dados para IA

| Estágio | Considerações | Requisitos |
|---------|---------------|------------|
| Coleta | Consentimento, propósito | Documentação |
| Preparação | Anonimização | Verificações de qualidade |
| Treinamento | Controle de versão | Trilha de auditoria |
| Inferência | Validação de entrada | Monitoramento |
| Atualizações de Modelo | Dados de retreinamento | Aprovação |

### 7. Privacidade e Proteção de Dados

#### Princípios de Privacidade
- Minimização de dados
- Limitação de propósito
- Gestão de consentimento
- Direitos individuais

#### Requisitos de Compliance

| Regulamentação | Escopo | Requisitos Principais | Status |
|----------------|--------|----------------------|--------|
| LGPD | Dados brasileiros | Consentimento, direitos | |
| GDPR | Dados da UE | Consentimento, direitos | |
| [Específico do setor] | | | |

#### Controles de Privacidade
| Controle | Propósito | Implementação |
|----------|-----------|---------------|
| Anonimização | Remover identificadores | [Método] |
| Pseudonimização | Substituir identificadores | [Método] |
| Criptografia | Proteger dados | [Padrão] |
| Controles de acesso | Limitar acesso | [Sistema] |

### 8. Gestão de Metadados

#### Padrões de Metadados

| Tipo de Metadados | Descrição | Campos Obrigatórios |
|-------------------|-----------|---------------------|
| Técnicos | Schema, formatos | Nome da tabela, colunas, tipos |
| Negócio | Definições, propriedade | Definição, steward, domínio |
| Operacionais | Qualidade, linhagem | Score de qualidade, origem, atualizações |

#### Requisitos do Catálogo de Dados
- Inventário pesquisável de todos os ativos de dados
- Integração com glossário de negócios
- Visualização de linhagem
- Exibição de métricas de qualidade

### 9. Acesso e Segurança de Dados

#### Modelo de Controle de Acesso

| Classificação de Dados | Modelo de Acesso | Aprovação Necessária |
|------------------------|------------------|----------------------|
| Público | Aberto | Não |
| Interno | Baseado em papel | Não |
| Confidencial | Need-to-know | Gestor |
| Restrito | Concessão explícita | Proprietário + Segurança |

#### Acesso de Modelos de IA
| Tipo de Modelo | Acesso a Dados | Restrições |
|----------------|----------------|------------|
| Modelos internos | Completo (dados aprovados) | Log de auditoria |
| Ferramentas de IA externas | Limitado | Sem dados restritos |
| Modelos de fornecedores | Conforme contrato | DPA obrigatório |

### 10. Roadmap de Implementação

#### Fase 1: Fundação (Meses 1-3)
- [ ] Estabelecer conselho de governança
- [ ] Definir esquema de classificação
- [ ] Identificar ativos de dados críticos
- [ ] Nomear stewards de dados

#### Fase 2: Construção (Meses 4-6)
- [ ] Implementar catálogo de dados
- [ ] Implantar monitoramento de qualidade
- [ ] Criar controles de privacidade
- [ ] Desenvolver programa de treinamento

#### Fase 3: Escala (Meses 7-12)
- [ ] Expandir cobertura
- [ ] Automatizar verificações de qualidade
- [ ] Rastreamento avançado de linhagem
- [ ] Melhoria contínua

### 11. Métricas e Monitoramento

| Métrica | Meta | Frequência | Responsável |
|---------|------|------------|-------------|
| Score de qualidade de dados | >90% | Semanal | |
| Compliance com políticas | 100% | Mensal | |
| Tempo de resposta a incidentes | <4 hrs | Por incidente | |
| Conclusão de treinamento | 100% | Trimestral | |

## Formato de Saída
- Use linguagem profissional de governança
- Inclua políticas e procedimentos específicos
- Customize para requisitos do setor
- Torne papéis e responsabilidades claros
- Inclua passos de implementação acionáveis
"""
