# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from models.Cliente import Cliente
from models.Produto import Produto
from models.Vendedor import Vendedor

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Venda(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    vendedor=db.Column(db.Integer, db.Foreignkey(Vendedor.id), nullable=False)
    data_hora=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    cliente=db.Column(db.Integer, db.Foreignkey(Cliente.id), nullable=False)
    item=db.Column(db.Integer, db.Foreignkey(Produto.id), nullable=False)
    quantidade=db.Column(db.Integer, nullable=True, default=0)