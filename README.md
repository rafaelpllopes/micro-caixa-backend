# Micro Caixa (Backend)

## Sobre o projeto
API Rest responsavel controlar um sistema de vendas para consumidor

## Ambiente
- Python 3.8.10
- Postgresql
- Docker 

### Requisitos para a API
- Flask==2.0.1
- Flask-Migrate==3.0.1
- Flask-Script==2.0.6
- Flask-SQLAlchemy==2.5.1
- SQLAlchemy==1.4.21
- psycopg2-binary==2.9.1

### Estrutura do Banco de Dados 
- **Produto**
   - id
   - nome
   - valor
   - imagem
   - qtd
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
    - data e hora
    - cliente (fk)
    - produto (fk)
    - quantidade

### Migrate
```python migrate.py db init``` gerar as configurações do migrate, executa somente na primeira vez
```python migrate.py db migrate```
```python migrate.py db upgrade```

## Objetivos

1. Consultar e cadastrar os produtos ou serviços e seus percentuais de comissão;
2. Consultar e cadastrar os clientes (apenas nome);
3. Consultar e cadastrar os vendedores (apenas nome);
4. Lançar uma venda (data/hora, vendedor, cliente, itens e quantidades;
5. Consultar comissões de dado vendedor em dado período;

## Estrutura do projeto

## Como executar
