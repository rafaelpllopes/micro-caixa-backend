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
        """
            Metodo faz a consulta na tabela cliente no banco de dados e traz todos os cadastrados
        """
        resposta = []
        try:
            resposta = db.session.query(Cliente).all()
        except Exception as erro:
            print(f'Erro [models - Cliente.py - get_all]: {erro}')
            raise Exception('Erro ao listar os clientes')
        finally:
            db.session.close()
        
        return resposta
    
    def get_by_id(self, id):
        """
            Metodo traz um cliente no tabela cliente no banco de dados pelo seu id
        """
        resposta = []
        try:
            resposta = db.session.query(Cliente).filter_by(id=id).one()
        except Exception as erro:
            print(f'Erro [models - Cliente.py - get_by_id]: {erro}')
        finally:
            db.session.close()
        
        return resposta
    
    def add(self, cliente):
        """
            Metodo adiciona um cliente pelo nome, tabela cliente no banco de dados
        """
        try:
            db.session.add(cliente)
            db.session.commit()
        except Exception as erro:
            print(f'Erro [models - Cliente.py - add]: {erro}')
            raise Exception('Erro ao inserir o cliente')
        finally:
            db.session.close()
        
    def update(self, id, nome):
        """
            Metodo responsavel por realizar a atualizaçao de um cliente pela sua id
        """
        try:
            atualizar = db.session.query(Cliente).filter_by(id=id).first()
            atualizar.nome = nome
            db.session.commit()
        except Exception as erro:
            print(f'Erro [models - Cliente.py - update]: {erro}')
            raise Exception('Erro ao atualizar o cliente')
        finally:
            db.session.close()

    def delete(self, id):
        """
            Metodo responsavle por deletar um cliente para id
        """
        try:
            deletar = db.session.query(Cliente).filter_by(id=id).first()
            db.session.delete(deletar)
            db.session.commit()
        except Exception as erro:
            print(f'Erro [models - Cliente.py - delete]: {erro}')
            raise Exception('Erro ao deletar o cliente')
        finally:
            db.session.close()

    def __repr__(self) -> str:
        return f"Cliente -> id: {self.id}, nome: {self.nome}, criado: {self.criado}, atualizado: {self.atualizado}"
        
            