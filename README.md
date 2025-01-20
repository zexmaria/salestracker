# SalesTracker

**SalesTracker** é um sistema de gerenciamento de 
vendas que permite cadastrar clientes, vendedores, 
produtos e vendas e gerar relatórios detalhados 
das transações. Este projeto pessoal foi desenvolvido 
como parte do estudo sobre API REST utilizando
**Django** e **Django REST Framework (DRF)**.


## 🛠️ Funcionalidades Principais

- API RESTful para integração e consulta de dados.
- Relatórios detalhados de vendas, filtrados por datas, cliente ou vendedor.
- Registro de vendas, vinculando clientes, vendedores e itens da venda.
- Cadastro de clientes com informações básicas como nome, email e telefone.
- Registro de vendedores com nome e número de registro único.
- Gerenciamento de produtos, incluindo nome, grupo de produtos e valor.
***
### Endpoint para relatório de vendas:
http://127.0.0.1:8000/api/vendas/?data_inicio=&data_fim=&vendedor=&cliente=
***
## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Django**: Framework web utilizado para o backend.
- **Django REST Framework (DRF)**: Para criação de APIs RESTful.
- **HTML**: Para o frontend básico com templates.
- **Bootstrap**: Para estilização e responsividade da interface.
***
## 🔗 Como Executar o Projeto

1. **Clone o repositório**:
    
    ```bash
    git clone https://github.com/zexmaria/salestracker.git 
    ```
    
2. **Acesse o diretório do projeto**:
    
    ```bash
    cd salestracker 
    ```
    
3. **Crie um ambiente virtual**:
    
    ```bash
    python -m venv .venv
    ```
    
4. **Ative o ambiente virtual**:
    - No Windows:
        
        ```bash
        .venv\Scripts\activate 
        ```
        
    - No Linux/Mac:
        
        ```bash
        source .venv/bin/activate
        ```
        
5. **Instale as dependências**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
6. **Execute as migrações**:
    
    ```bash
    python manage.py migrate
    ```
    
7. **Inicie o servidor local**:
    
    ```bash
    python manage.py runserver
    ```
    

Acesse o sistema em: [http://127.0.0.1:8000](http://127.0.0.1:8000/).

## 🧑‍💻 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

**Autor**: José Maria Duarte

**LinkedIn**: [José Maria](https://www.linkedin.com/in/zemariaduarte/)

**GitHub**: [ZexMaria](https://github.com/zexmaria)