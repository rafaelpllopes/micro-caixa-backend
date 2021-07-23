from logging import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import app_config, app_active
config = app_config[app_active]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = config.SECRET

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Cliente(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome=db.Column(db.String(100), nullable=False)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

class Produto(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome=db.Column(db.String(100), nullable=False)
    valor=db.Column(db.Numeric(10,2), nullable=False)
    imagem=db.Column(db.Text(), nullable=False)
    qtd=db.Column(db.Integer, nullable=True, default=0)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

class Vendedor(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome=db.Column(db.String(100), nullable=False)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

class Venda(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    vendedor=db.Column(db.Integer, db.Foreignkey(Vendedor.id), nullable=False)
    data_hora=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    cliente=db.Column(db.Integer, db.Foreignkey(Cliente.id), nullable=False)
    item=db.Column(db.Integer, db.Foreignkey(Produto.id), nullable=False)
    quantidade=db.Column(db.Integer, nullable=True, default=0)
    
if __name__ == '__main__':
    manager.run()
    