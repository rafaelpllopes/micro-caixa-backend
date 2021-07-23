# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Produto(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome=db.Column(db.String(100), nullable=False)
    valor=db.Column(db.Numeric(10,2), nullable=False)
    imagem=db.Column(db.Text(), nullable=False)
    qtd=db.Column(db.Integer, nullable=True, default=0)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)