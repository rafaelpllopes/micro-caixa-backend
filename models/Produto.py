# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Produto(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome=db.Column(db.String(100), nullable=False)
    valor=db.Column(db.Numeric(10,2), nullable=False)
    comissao_percentual=db.Column(db.Numeric(10,2), default=0)
    imagem=db.Column(db.Text(), nullable=True)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def get_all(self):
        """
            Metodo faz a consulta na tabela produto no banco de dados e traz todos os cadastrados
        """
        resposta = []
        try:
            resposta = db.session.query(Produto).all()
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao listar os produtos')
        finally:
            db.session.close()
        
        return resposta
    
    def get_by_id(self, id):
        """
            Metodo traz um produto no tabela produto no banco de dados pelo seu id
        """
        resposta = []
        try:
            resposta = db.session.query(Produto).filter_by(id=id).one()
        except Exception as erro:
            print(erro)
        finally:
            db.session.close()
        
        return resposta
    
    def add(self, produto):
        """
            Metodo adiciona um produto pelo nome, tabela produto no banco de dados
        """
        try:
            db.session.add(produto)
            db.session.commit()
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao inserir o produto')
        finally:
            db.session.close()
        
    def update(self, id, nome, valor, imagem):
        """
            Metodo responsavel por realizar a atualizaçao de um produto pela sua id
        """
        try:
            atualizar = db.session.query(Produto).filter_by(id=id).first()
            if nome:
                atualizar.nome = nome
            
            if valor:
                atualizar.valor = valor

            if imagem:
                atualizar.imagem = imagem
                
            db.session.commit()
        except Exception as erro:
            print(f"Erro: {erro}")
            raise Exception('Erro ao atualizar o produto')
        finally:
            db.session.close()

    def delete(self, id):
        """
            Metodo responsavle por deletar um produto para id
        """
        try:
            deletar = db.session.query(Produto).filter_by(id=id).first()
            db.session.delete(deletar)
            db.session.commit()
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao deletar o produto')
        finally:
            db.session.close()

    def __repr__(self) -> str:
        return f"Produto -> id: {self.id}, nome: {self.nome}, valor: {self.valor}, comissao: {self.comissao_percentual}%, imagem: {self.imagem}, criado: {self.criado}, atualizado: {self.atualizado}"