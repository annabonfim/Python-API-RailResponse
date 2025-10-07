# RailResponse - Sistema de Gestão de Alertas Ferroviários

## 📋 Sobre o Projeto

O **RailResponse** é um sistema desenvolvido para a CCR com o objetivo de centralizar e automatizar o gerenciamento de alertas de emergência em sistemas ferroviários. O projeto foi criado pelo grupo CodeGirls (Alane Rocha da Silva, Anna Beatriz de Araujo Bonfim e Maria Eduarda Araujo Penas) como solução para o desafio de alertas e respostas automáticas.

## 🎯 Problema Resolvido

A CCR utiliza diversos sistemas fragmentados para monitorar e gerar alertas sobre situações de emergência, o que dificulta respostas rápidas e eficientes. O RailResponse centraliza essas informações em uma única plataforma, permitindo:

- Monitoramento unificado de alertas
- Classificação automática por gravidade
- Resposta rápida a emergências
- Histórico completo de ocorrências

## 🚀 Funcionalidades

### 1. Gestão de Alertas
- ✅ Cadastro de novos alertas de emergência
- ✅ Consulta de alertas com filtros (Pendentes, Concluídos, Todos)
- ✅ Atualização de status de alertas
- ✅ Exclusão de alertas
- ✅ Exportação de alertas pendentes para JSON

### 2. Integração com APIs Externas
- 🌦️ Consulta de temperatura via API OpenWeather
- 📊 Possibilidade de integração com outras fontes de dados

### 3. Banco de Dados
- 💾 Armazenamento persistente em Oracle Database
- 📈 Histórico completo de emergências
- 🔍 Consultas otimizadas com filtros

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Oracle Database** - Armazenamento de dados
- **oracledb** - Driver para conexão com Oracle
- **requests** - Consumo de APIs externas
- **JSON** - Exportação de dados

## 📦 Pré-requisitos

```bash
pip install oracledb
pip install requests
```

## ⚙️ Configuração

### Configuração do Banco de Dados

Atualize as credenciais de conexão no código:

```python
conn = oracledb.connect(
    user="SEU_USUARIO",
    password="SUA_SENHA",
    dsn="oracle.fiap.com.br:1521/ORCL"
)
```

### Configuração da API OpenWeather

Substitua a chave da API no código:

```python
chave_api = "SUA_CHAVE_API_AQUI"
```

Obtenha sua chave gratuita em: [OpenWeather API](https://openweathermap.org/api)

## 🎮 Como Usar

### Executando o Sistema

```bash
python menu.py
```

### Menu Principal

Ao executar o programa, você verá as seguintes opções:

```
=== Menu Principal ===
1. Cadastrar alerta
2. Concluir alerta
3. Excluir alerta
4. Consultar alertas
5. Exportar alertas pendentes para JSON
6. Ver temperatura atual (API OpenWeather)
0. Sair
```

### Exemplos de Uso

#### Cadastrar um Alerta
1. Selecione a opção `1`
2. Informe o tipo de emergência (ex: "Falha no sistema de freios")
3. Informe o número da linha (ex: 4)
4. O alerta será registrado com status "Pendente"

#### Consultar Alertas
1. Selecione a opção `4`
2. Escolha o filtro desejado:
   - `1` - Apenas alertas concluídos
   - `2` - Apenas alertas pendentes
   - `3` - Todos os alertas

#### Exportar Alertas
1. Selecione a opção `5`
2. Os alertas pendentes serão exportados para `alertas_pendentes.json`

## 📊 Estrutura da Tabela

A tabela `alertas_sprint4` possui a seguinte estrutura:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | NUMBER | Identificador único (auto-incremento) |
| tipo_emergencia | VARCHAR2(100) | Descrição do tipo de emergência |
| linha | NUMBER | Número da linha ferroviária |
| status | VARCHAR2(20) | Status do alerta (Pendente/Concluído) |
| resposta | VARCHAR2(255) | Resposta dada ao alerta |
| data_envio | TIMESTAMP | Data e hora do registro |
| data_conclusao | TIMESTAMP | Data e hora da conclusão |

## 📄 Formato de Exportação JSON

```json
[
    {
        "id": 1,
        "tipo_emergencia": "Falha no sistema de freios",
        "linha": 4,
        "status": "Pendente",
        "resposta": "-",
        "data_envio": "2024-10-06T14:30:00",
        "data_conclusao": null
    }
]
```

## 🔄 Atualizações da Sprint 4

### Melhorias Implementadas

1. **Integração com Oracle Database**
   - Substituição de arquivos JSON por banco de dados real
   - Criação automática de tabelas
   - Operações CRUD completas

2. **Menu Interativo Aprimorado**
   - Submenus para consultas filtradas
   - Feedback visual melhorado
   - Tratamento de erros

3. **Exportação de Dados**
   - Função para exportar alertas pendentes em JSON
   - Conversão automática de tipos de dados

4. **Integração com API Externa**
   - Consulta de temperatura via OpenWeather
   - Base para futuras integrações climáticas

5. **Código Modular**
   - Funções reutilizáveis
   - Melhor organização
   - Manutenibilidade aprimorada

## 👥 Equipe - CodeGirls

- **Alane Rocha da Silva** - RM561052
- **Anna Beatriz de Araujo Bonfim** - RM559561
- **Maria Eduarda Araujo Penas** - RM560944

## 🏫 Instituição

**FIAP** - Faculdade de Informática e Administração Paulista  
Curso Superior de Análise e Desenvolvimento de Sistemas

## 📝 Licença

Projeto acadêmico desenvolvido para a CCR - 2024

## 🔮 Próximos Passos

- [ ] Implementação de interface web
- [ ] Integração com WhatsApp via Twilio
- [ ] Sistema de classificação automática de gravidade
- [ ] Dashboard de monitoramento em tempo real
- [ ] Notificações automáticas para alertas críticos

## 📞 Suporte

Para dúvidas ou sugestões, entre em contato com a equipe CodeGirls.

---

**Desenvolvido com ❤️ pela equipe CodeGirls para a CCR**
