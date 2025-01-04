# SalesTracker

SalesTracker é um sistema de gerenciamento de vendas que permite cadastrar clientes, vendedores, produtos e vendas, além de gerar relatórios detalhados das transações realizadas. O objetivo é proporcionar uma interface simples e intuitiva para gerenciar vendas e acompanhar o desempenho comercial.


O projeto é parte do estudo sobre API REST utilizando Django e DRF.

## Funcionalidades Principais

- Cadastro de clientes com informações básicas como nome, email e telefone.
- Cadastro de vendedores com nome e número de registro.
- Cadastro de produtos.
- Registro de vendas com vinculação a clientes, vendedores e produtos, incluindo a quantidade e preço de cada produto vendido.
- Geração de relatórios de vendas filtrados por período, cliente e vendedor.

---

## Tecnologias Utilizadas

- **Python** (3.9 ou superior)
- **Django** (versão 5.1.4)
- **Django REST Framework** (para APIs)
- **HTML/CSS** (para os templates)
- **SQLite** (banco de dados padrão)

---

## Requisitos

- Python 3.9 ou superior
- Git
- Poetry (para gerenciamento de dependências)

---

## Como Rodar o Projeto Localmente

### 1. Clonar o Repositório

Execute o seguinte comando no terminal para clonar o repositório:

```
git clone https://github.com/seu-usuario/salestracker.git
cd salestracker
```

### 2. Configurar o Ambiente Virtual

Instale as dependências usando o Poetry:

```
poetry install
```

Ative o ambiente virtual gerenciado pelo Poetry:

```
poetry shell
```

### 3. Configurar o Banco de Dados

Aplique as migrações para configurar o banco de dados:

```
python manage.py migrate
```

### 4. Popular o Banco de Dados (Opcional)

Se desejar, pode criar dados iniciais no sistema:

```
python manage.py createsuperuser
```

Preencha os dados solicitados para criar um usuário administrador.

### 5. Iniciar o Servidor Local

Execute o servidor local do Django:

```
python manage.py runserver
```

Acesse o sistema no navegador usando o endereço:

```
http://127.0.0.1:8000/
```

---

## Estrutura do Projeto

- **core**: App principal contendo as funcionalidades de cadastro e gerenciamento.
- **templates**: Arquivos HTML para renderização das páginas.
- **static**: Arquivos de estilo (CSS) e JavaScript.
- **manage.py**: Arquivo de gerenciamento do Django.

---

## Rotas Principais

### Cadastro

- `http://127.0.0.1:8000/cliente/create/`: Cadastro de clientes
- `http://127.0.0.1:8000/vendedor/create/`: Cadastro de vendedores
- `http://127.0.0.1:8000/produto/create/`: Cadastro de produtos
- `http://127.0.0.1:8000/venda/create/`: Registro de vendas

### Relatórios

- `http://127.0.0.1:8000/relatorio/vendas/`: Geração de relatório de vendas

---

## Melhorias Futuras

- Implementação de autenticação de usuários com permissões diferenciadas.
- Integração com APIs de pagamento.
- Visualização de relatórios em gráficos.
- Exportação de relatórios em PDF e Excel.

---

## Contribuições

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

1. Fork este repositório.
2. Crie uma branch para a funcionalidade/correção: `git checkout -b minha-feature`
3. Envie suas modificações: `git commit -m 'Adiciona nova funcionalidade'`
4. Envie para o repositório remoto: `git push origin minha-feature`
5. Abra um Pull Request.

---

## Licença

Este projeto é licenciado sob a Licença MIT. Para mais informações, leia o arquivo LICENSE.