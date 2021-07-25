# -*- coding: utf-8 -*-
from models.Produto import Produto
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from models.Produto import Produto
from models.Venda import Venda

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Carrinho(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    venda=db.Column(db.Integer, db.ForeignKey(Venda.id), nullable=False)
    produto=db.Column(db.Integer, db.ForeignKey(Produto.id), nullable=False)
    valor=db.Column(db.Numeric(10,2), nullable=False)
    comissao=db.Column(db.Numeric(10,2), nullable=False, default=0)
    quantidade=db.Column(db.Integer, nullable=True, default=0)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def __repr__(self) -> str:
        return f"Carrinho -> id: {self.id}, venda: {self.venda}, produto: {self.produto}, valor: {self.valor}, comissao: {self.comissao}, quantidade: {self.quantidade}, criado: {self.criado}, atualizado: {self.atualizado}"