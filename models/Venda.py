# -*- coding: utf-8 -*-
from datetime import datetime
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
            resposta = (db.session.query(Venda, Vendedor, Cliente)
                        .join(Vendedor, Venda.vendedor == Vendedor.id)
                        .join(Cliente, Venda.cliente == Cliente.id)
                        .order_by(Venda.criado)
                        ).all()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - get_all]: {erro}')
            raise Exception('Erro ao listar as vendas')
        finally:
            db.session.close()
        
        return resposta
    
    def get_itens_carrinho(self, venda_id: int):
        """
            Metodo que traz todos os produtos do carrinho de uma venda pelo id da venda
        """
        resposta = []
        try:
            resposta = (db.session.query(Carrinho, Produto)
                        .filter_by(venda=venda_id)
                        .join(Produto, Carrinho.produto == Produto.id)
                        .order_by(Carrinho.criado)
                        ).all()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - get_itens_carrinho]: {erro}')
            raise Exception('Erro ao listar os itens do carrinho')
        finally:
            db.session.close()
        
        return resposta
    
    def get_by_id(self, id):
        """
            Metodo traz uma venda no tabela produto no banco de dados pelo seu id
        """
        resposta = {}
        try:
            resposta = (db.session.query(Venda, Vendedor, Cliente)
                        .filter_by(id=id)
                        .join(Vendedor, Venda.vendedor == Vendedor.id)
                        .join(Cliente, Venda.cliente == Cliente.id)
                        ).one()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - get_by_id]: {erro}')
            raise Exception('Erro ao buscar uma venda')
        finally:
            db.session.close()
        
        return resposta
    
    def get_item_by_id(self, id):
        """
            Metodo item pelo seu id
        """
        resposta = {}
        try:
            resposta = db.session.query(Carrinho).filter_by(id=id).one()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - get_item_by_id]: {erro}')
            raise Exception('Erro ao buscar uma venda')
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

            if venda.id:
                self.__add_produtos_carrinho(venda.id, produtos)
        except Exception as erro:
            print(f'Erro [Models - Venda.py - add]: {erro}')
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
            print(f'Erro [Models - Venda.py - verificar_existencia_produto]: {erro}')
        finally:
            db.session.close()
    
    def __add_produtos_carrinho(self, venda_id, produtos):
        """
            Metodo adicionar os produtos do carrinho
        """
        try:           
            for produto in produtos:
                comissao = self.__verificar_comissao(produto['comissao'])
                db.session.add(Carrinho(venda=venda_id, produto=produto['id'], valor=produto['valor'], quantidade=produto['quantidade'], comissao=comissao))     
                db.session.commit()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - add_produtos_carrinho]: {erro}')
            raise Exception('Erro ao inserir ao produtos do carrinho')
        
    def __verificar_comissao(self, comissao):
        hora = datetime.now().strftime('%H:%M:%S')
        if hora >= '00:00:00' and hora <= '12:00:00':
            valor_comissao = 5
        else:
            if comissao < 4:
                valor_comissao = 4
            else:
                valor_comissao = comissao

        return float(valor_comissao)

    def update(self, id, vendedor, cliente, produtos):
        """
            Metodo responsavel por realizar a atualizaçao de venda pela sua id
        """
        try:
            atualizar = db.session.query(Venda).filter_by(id=id).first()
            self.__update_produtos_carrinho(atualizar.id, produtos)

            if vendedor:
                atualizar.vendedor = vendedor
            
            if cliente:
                atualizar.cliente = cliente
                
            db.session.commit()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - update]: {erro}')
            raise Exception('Erro ao atualizar o produto')
        finally:
            db.session.close()
    
    def __update_produtos_carrinho(self, venda_id, produtos):
        """
            Metodo atualizar os produtos do carrinho
        """
        novos = []
        try:           
            for produto in produtos:
                carrinho_id = produto['carrinho_id']
                produto_id = produto['id']
                quantidade = produto['quantidade']
                valor = produto['valor']
                comissao = self.__verificar_comissao(produto['comissao'])
                
                if not carrinho_id:
                    novos.append(produto)
                else:
                    item = db.session.query(Carrinho).filter_by(id=produto['carrinho_id'], venda=venda_id).first()

                    if produto_id:
                        item.produto = produto_id

                    if quantidade:
                        item.quantidade = quantidade

                    if comissao:
                        item.comissao = comissao

                    if valor:
                        item.valor = valor

                    db.session.commit()

            if novos:
                self.__add_produtos_carrinho(venda_id, novos)
                
        except Exception as erro:
            print(f'Erro [Models - Venda.py - update_produtos_carrinho]: {erro}')
            raise Exception('Erro ao atualizar a venda do carrinho')

    def delete_venda(self, id):
        """
            Metodo responsavel por deletar uma venda para id
        """
        try:
            deletar = db.session.query(Venda).filter_by(id=id).first()
            db.session.delete(deletar)
            db.session.commit()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - delete_venda]: {erro}')
            raise Exception('Erro ao deletar a venda')
        finally:
            db.session.close()

    def delete_item_carrinho(self, id_venda, id_item):
        """
            Metodo responsavel por deletar uma venda para id
        """
        try:
            deletar = db.session.query(Carrinho).filter_by(id=id_item, venda=id_venda).first()
            db.session.delete(deletar)
            db.session.commit()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - delete_item_carrinho]: {erro}')
            raise Exception('Erro ao deletar o produto da venda')
        finally:
            db.session.close()

    def comissao_vendedor_por_periodo(self, id: int, periodo: dict):
        resposta = []
        try:
            resposta = (db.session.query(Vendedor, Venda, Carrinho)
                        .filter_by(id=id)
                        .join(Venda, Venda.vendedor == Vendedor.id)
                        .filter(Venda.criado >= periodo['inicial'], Venda.criado <= periodo['final'])
                        .join(Carrinho, Carrinho.venda == Venda.id)
                        .order_by(Venda.criado)
                        ).all()
        except Exception as erro:
            print(f'Erro [Models - Venda.py - comissao_vendedor_por_periodo]: {erro}')
            raise Exception('Erro ao listar as vendas')
        finally:
            db.session.close()
        
        return resposta
    
    def __repr__(self) -> str:
        return f"Venda -> id: {self.id}, vendedor: {self.vendedor}, cliente: {self.cliente}, criado: {self.criado}, atualizado: {self.atualizado}"

class Carrinho(db.Model):
    id=db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    venda=db.Column(db.Integer, db.ForeignKey(Venda.id, ondelete='CASCADE'), nullable=False)
    produto=db.Column(db.Integer, db.ForeignKey(Produto.id), nullable=False)
    valor=db.Column(db.Numeric(10,2), nullable=False)
    comissao=db.Column(db.Numeric(10,2), nullable=False, default=0)
    quantidade=db.Column(db.Integer, nullable=True, default=0)
    criado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    atualizado=db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def __repr__(self) -> str:
        return f"Carrinho -> id: {self.id}, venda: {self.venda}, produto: {self.produto}, valor: {self.valor}, comissao: {self.comissao}, quantidade: {self.quantidade}, criado: {self.criado}, atualizado: {self.atualizado}"