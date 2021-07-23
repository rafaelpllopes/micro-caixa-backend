# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Vendedor(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome=db.Column(db.String(100), nullable=False)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)


    def get_all(self):
        """
            Metodo faz a consulta na tabela vendedor no banco de dados e traz todos os cadastrados
        """
        resposta = []
        try:
            resposta = db.session.query(Vendedor).all()
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao listar os vendedores')
        finally:
            db.session.close()
        
        return resposta
    
    def get_by_id(self, id):
        """
            Metodo traz um vendedor no tabela vendedor no banco de dados pelo seu id
        """
        resposta = []
        try:
            resposta = db.session.query(Vendedor).filter_by(id=id).one()
        except Exception as erro:
            print(erro)
        finally:
            db.session.close()
        
        return resposta
    
    def add(self, nome):
        """
            Metodo adiciona um vendedor pelo nome, tabela vendedor no banco de dados
        """
        try:
            db.session.add(nome)
            db.session.commit()
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao inserir o vendedor')
        finally:
            db.session.close()
        
    def update(self, id, nome):
        """
            Metodo responsavel por realizar a atualizaçao de um vendedor pela sua id
        """
        try:
            atualizar = db.session.query(Vendedor).filter_by(id=id).first()
            atualizar.nome = nome
            db.session.commit()
        except Exception as erro:
            print(f"Erro: {erro}")
            raise Exception('Erro ao atualizar o vendedor')
        finally:
            db.session.close()

    def delete(self, id):
        """
            Metodo responsavle por deletar um vendedor para id
        """
        try:
            deletar = db.session.query(Vendedor).filter_by(id=id).first()
            db.session.delete(deletar)
            db.session.commit()
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao deletar o vendedor')
        finally:
            db.session.close()

    def __repr__(self) -> str:
        return f"Vendedor -> id: {self.id}, nome: {self.nome}, criado: {self.criado}, atualizado: {self.atualizado}"