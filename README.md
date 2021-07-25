# Micro Caixa (Backend)

## Sobre o projeto
API Rest responsavel controlar um sistema de vendas para consumidor

## Ambiente
- Python 3.8.10
- Postgresql
- Docker (Para rodar o postgresql)

### Requisitos para a API
- Flask==1.1.2
- Flask-Migrate==2.6.0
- Flask-Script==2.0.6
- Flask-SQLAlchemy==2.4.4
- SQLAlchemy==1.3.23
- psycopg2-binary==2.9.1

## Como executar (Em Ambiente Linux)
1. Criar o container para o postgresql ```docker run -d --name database-dev -p 5445:5432 -v ~/database-dev/database:/var/lib/postgresql/data -e POSTGRES_PASSWORD=123 postgres```
2. Acessar o container ```docker exec -it database-dev /bin/bash```
3. Acessar o usuario postgres ```su postgres```
4. Acessar o ```psql```
5. Criar o banco de dados ```CREATE DATABASE micro_caixa ENCODING='UTF8';```
6. Sair do psql ```\q```
7. Sair do container ```ctrl + p e ctrl + q```
8. [baixar o projeto](https://github.com/rafaelpllopes/micro-caixa-backend/archive/refs/heads/main.zip) ou clonar: ```git clone https://github.com/rafaelpllopes/micro-caixa-backend.git```
9. Entra na pasta do projeto ```cd micro-caixa-backend```
10. Criar o ambiente virtual ```python3 -m venv venv```
11. Instalar as dependencias ```pip install -r requirements.txt```
12. Configurar as variaveis de ambiente ```export FLASK_ENV=development && export SECRET_FLASK=*djjuqWEGJ3355@3fdf && export DATABASE_URL=postgresql+psycopg2://postgres:senha_do_db@localhost:5445/micro_caixa```
13. Entrar no ambiente virtual ```source venv/bin/activate```
14. Executar as migrations ```python migrate.py db upgrade```
15. Executar o projeto ```python run.py```

### Estrutura do Banco de Dados 
- **Produto**
   - id
   - nome
   - valor
   - imagem
   - criado
   - atualizado
- **Cliente**
    - id
    - nome
    - criado
    - atualizado
- **Vendedor**
    - id
    - nome
    - criado
    - atualizado
- **Venda**
    - id
    - vendedor (fk)
    - cliente (fk)
    - criado
    - atualizado
- **Carrinho**
    - id
    - venda (fk)
    - produto (fk)
    - valor
    - quantidade
    - criado
    - atualizado

### Migrate
- ```python migrate.py db init``` gerar as configurações do migrate, executa somente na primeira vez
- ```python migrate.py db migrate```
- ```python migrate.py db upgrade```

## Objetivos

1. Consultar e cadastrar os produtos ou serviços e seus percentuais de comissão;
2. Consultar e cadastrar os clientes (apenas nome);
3. Consultar e cadastrar os vendedores (apenas nome);
4. Lançar uma venda (data/hora, vendedor, cliente, itens e quantidades;
5. Consultar comissões de dado vendedor em dado período;

## Estrutura do projeto
```
.
├── app.py
├── config.py
├── controllers
│   ├── Cliente.py
├── migrate.py
├── migrations
├── models
│   ├── Cliente.py
│   ├── Produto.py
│   ├── Venda.py
│   └── Vendedor.py
├── README.md
├── requirements.txt
├── run.py

```