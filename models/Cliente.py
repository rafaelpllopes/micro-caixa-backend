# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Cliente(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome=db.Column(db.String(100), nullable=False)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def get_all(self):
        resposta = []
        try:
            resposta = db.session.query(Cliente).all()
        except Exception as erro:
            print(erro)
        finally:
            db.session.close()
        
        return resposta
    
    def get_by_id(self, id):
        resposta = []
        try:
            resposta = db.session.query(Cliente).filter_by(id=id).one()
        except Exception as erro:
            print(erro)
        finally:
            db.session.close()
        
        return resposta
    
    def add(self, nome):
        try:
            db.session.add(nome)
            db.session.commit()
        except Exception as erro:
            print(erro)
        finally:
            db.session.close()

    def __repr__(self) -> str:
        return f"id: {self.id}, nome: {self.nome}, criado: {self.criado}, atualizado: {self.atualizado}"
        
            