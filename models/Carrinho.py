# -*- coding: utf-8 -*-
from models.Produto import Produto
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from models.Venda import Venda
from models.Produto import Produto

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Carrinho(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    venda=db.Column(db.Integer, db.ForeignKey(Venda.id), nullable=False)
    produto=db.Column(db.Integer, db.ForeignKey(Produto.id), nullable=False)
    valor=db.Column(db.Numeric(10,2), nullable=False)
    quantidade=db.Column(db.Integer, nullable=True, default=0)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)