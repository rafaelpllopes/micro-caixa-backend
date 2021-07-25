# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from models.Cliente import Cliente
from models.Vendedor import Vendedor
from models.Produto import Produto

config = app_config[app_active]
db = SQLAlchemy(config.APP)
    
class Venda(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    vendedor=db.Column(db.Integer, db.ForeignKey(Vendedor.id), nullable=False)
    cliente=db.Column(db.Integer, db.ForeignKey(Cliente.id), nullable=False)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    
    def get_all(self):
        """
            Metodo faz a consulta na tabela carrinho no banco de dados e traz todos os cadastrados
        """
        resposta = []
        try:
            resposta = (db.session.query(Venda, Vendedor, Cliente, Carrinho)
                        .outerjoin(Vendedor, Venda.vendedor == Vendedor.id)
                        .outerjoin(Cliente, Venda.cliente == Cliente.id)
                        .outerjoin(Venda.carrinho == Carrinho.id)
                        .order_by(Venda.criado)
                        ).all()
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao listar as vendas')
        finally:
            db.session.close()
        
        return resposta
    
    def get_by_id(self, id):
        """
            Metodo traz uma venda no tabela produto no banco de dados pelo seu id
        """
        resposta = []
        try:
            resposta = (db.session.query(Venda, Vendedor, Cliente, Carrinho)
                        .outerjoin(Vendedor, Venda.vendedor == Vendedor.id)
                        .outerjoin(Cliente, Venda.cliente == Cliente.id)
                        .outerjoin(Venda.carrinho == Carrinho.id)
                        .order_by(Venda.criado)
                        .filter_by(id=id)
                        ).one()
        except Exception as erro:
            print(erro)
        finally:
            db.session.close()
        
        return resposta
    
    def add(self, venda, produtos):
        """
            Metodo adiciona uma venda pelo nome, tabela vendas e incluir os itens no carrinho
        """
        try:
            if not self.__verificar_existencia_produto(produtos):
               raise Exception('Erro ao inserir o venda')
            db.session.add(venda)
            db.session.commit()
            self.__add_produtos_carrinho(venda.id, produtos)
        except Exception as erro:
            print(erro)
            raise Exception('Erro ao inserir o venda')
        finally:
            db.session.close()
    
    def __verificar_existencia_produto(self, produtos):
        """
            Metodo responsavel por verificar a existencia de um produto
        """
        try:
            for produto in produtos:
                produto = db.session.query(Produto).filter_by(id=produto['id']).one()
                db.session.commit()
            return True
        except Exception as erro:
            print(erro)
        finally:
            db.session.close()
    
    def __add_produtos_carrinho(self, venda_id, produtos):
        """
            Metodo adicionar os produtos do carrinho
        """
        try:           
            for produto in produtos:
                db.session.add(Carrinho(venda=venda_id, produto=produto['id'], valor=produto['valor'], quantidade=produto['quantidade']))     
                db.session.commit()
        except Exception as erro:
            print(f"Erro: {erro}")
            raise Exception('Erro ao inserir ao produtos do carrinho')
        
    # def update(self, id, nome, valor, comissao):
    #     """
    #         Metodo responsavel por realizar a atualizaçao de um produto pela sua id
    #     """
    #     try:
    #         atualizar = db.session.query(Produto).filter_by(id=id).first()
    #         if nome:
    #             atualizar.nome = nome
            
    #         if valor:
    #             atualizar.valor = valor

    #         if comissao:
    #             atualizar.comissao_percentual = comissao
                
    #         db.session.commit()
    #     except Exception as erro:
    #         print(f"Erro: {erro}")
    #         raise Exception('Erro ao atualizar o produto')
    #     finally:
    #         db.session.close()

    # def delete(self, id):
    #     """
    #         Metodo responsavle por deletar um produto para id
    #     """
    #     try:
    #         deletar = db.session.query(Produto).filter_by(id=id).first()
    #         db.session.delete(deletar)
    #         db.session.commit()
    #     except Exception as erro:
    #         print(erro)
    #         raise Exception('Erro ao deletar o produto')
    #     finally:
    #         db.session.close()

    def __repr__(self) -> str:
        return f"Venda -> id: {self.id}, vendedor: {self.vendedor}, cliente: {self.cliente}, criado: {self.criado}, atualizado: {self.atualizado}"

from models.Carrinho import Carrinho