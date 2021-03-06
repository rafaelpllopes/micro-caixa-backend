# Micro Caixa (Backend)

## Sobre o projeto
API Rest responsavel controlar um sistema de vendas para consumidor

## Ambiente
- Python 3.8.10
- Postgresql
- Docker (Para rodar o postgresql)

### Requisitos para a API
- Flask==1.1.2
- Flask-Cors==3.0.10
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
12. Configurar as variaveis de ambiente ```export FLASK_ENV=development && export SECRET_FLASK=*djjuqWEGJ3355@3fdf && export DATABASE_URL=postgresql+psycopg2://postgres:senha_do_db@localhost:5445/micro_caixa```, caso já tenha a pasta de migrations com as versions, senão executar a migração conforme baixo
13. Entrar no ambiente virtual ```source venv/bin/activate```
14. Executar as migrations ```python migrate.py db upgrade```
15. Executar o projeto ```python run.py```

### Migrate
- ```python migrate.py db init``` gerar as configurações do migrate, executa somente na primeira vez
- ```python migrate.py db migrate```
- ```python migrate.py db upgrade```

## Como usar a API (Request/Response)

### Cliente
| Rota | Method | Request | Response |
| --- | --- | --- | --- |
| /clientes | POST | { "nome": "" } | { "msg": "Cliente cadastrado com sucesso", "status": 201 } |
| /clientes | GET |  | { "atualizado": "", "criado": "", "id": , "nome": ""} |
| /clientes/id | GET |  | { "atualizado": "", "criado": "", "id": , "nome": ""} |
| /clientes/id | PUT | { "nome": "" } | { "msg": "Cliente alterado com sucesso", "status": 202 } |
| /clientes/id | DELETE | | { "msg": "Cliente deletado com sucesso", "status": 202 } |

### Vendedor
| Rota | Method | Request | Response |
| --- | --- | --- | --- |
| /vendedores | POST | { "nome": "" } | { "msg": "Vendedor cadastrado com sucesso", "status": 201 } |
| /vendedores | GET |  | { "atualizado": "", "criado": "", "id": , "nome": ""} |
| /vendedores/id | GET |  | { "atualizado": "", "criado": "", "id": , "nome": ""} |
| /vendedores/id | PUT | { "nome": "" } | { "msg": "Vendedor alterado com sucesso", "status": 202 } |
| /vendedores/id | DELETE | | { "msg": "Vendedor deletado com sucesso", "status": 202 } |
    
### Produto
| Rota | Method | Request | Response |
| --- | --- | --- | --- |
| /produtos | POST | { "nome": "", "valor": , "comissao" } | { "msg": "Produto cadastrado com sucesso", "status": 201 } |
| /produtos | GET |  | { "atualizado": , "comissao": , "criado": , "id": , "nome": , "valor":  } |
| /produtos/id | GET |  | { "atualizado": , "comissao": , "criado": , "id": , "nome": , "valor":  }|
| /produtos/id | PUT | { "nome": "", "valor": , "comissao" }  | { "msg": "Produto alterado com sucesso", "status": 202 } |
| /produtos/id | DELETE | | { "msg": "Produto deletado com sucesso", "status": 202 } |
    
### Venda
| Rota | Method | Request | Response |
| --- | --- | --- | --- |
| /vendas | POST | { "vendedor": , "cliente": 5, "produtos": [ { "id": , "valor": , "quantidade": , "comissao":  } ] } | { "msg": "Venda cadastrado com sucesso", "status": 201 } |
| /vendas | GET |  | [ { "id": , "comissao_vendedor": , { "cliente": { "id": , "nome": }, "itens:": [ { "carrinho_id": , "comissao": , "produto": , "produto_id": , "quantidade": , "valor":  },], "total_venda": ,   "vendedor": { "id": , "nome": "" } } ] |
| /vendas/id | GET |  | { "id": , "comissao_vendedor": , { "cliente": { "id": , "nome": }, "itens:": [ { "carrinho_id": , "comissao": , "produto": , "produto_id": , "quantidade": , "valor":  },], "total_venda": ,   "vendedor": { "id": , "nome": "" } } |
| /vendas/id | PUT | {"vendedor": 3,"cliente": 5,	"produtos": [ { "carrinho_id": 34, "id": 3, "valor": 150, "quantidade": 2, "comissao": 2 }]} | { "msg": "Venda alterado com sucesso", "status": 202 } |
| /vendas/id | DELETE | | { "msg": "Venda deletado com sucesso", "status": 202 } |
| /vendas/vendedor/id | GET | { "inicial": "2021-07-26 00:00:00",	"final": "2021-07-26 23:59:59" } | { "comissao": ,  "periodo": { "final": , "inicial":   }, "vendedor":  } |
    

### Estrutura do Banco de Dados 
- **Produto**
   - id
   - nome
   - valor
   - comissao_percentual
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
    - comissao
    - quantidade
    - criado
    - atualizado

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
│   ├── Produto.py
│   ├── Venda.py
│   └── Vendedor.py
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
