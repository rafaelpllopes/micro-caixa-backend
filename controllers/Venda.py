# -*- coding: utf-8 -*-
from datetime import datetime
from functools import reduce

from sqlalchemy.ext.declarative.api import declared_attr
from models.Venda import Venda

class VendaController:
    """
        Classe venda com o metodos realizar as funções para o Vendas
    """
    def __init__(self):
        self.model = Venda()
    
    def listar_tudo(self):
        """
            Metodo que lista os vendas e traduz
        """
        try:
            resposta = self.model.get_all()
            return list(map(lambda venda: self.__traduz(venda), resposta)), 200
        except Exception as erro:
            print(f'Erro: {erro}')
        
        return [], 404
    
    def lista_por_id(self, id: int):
        """
            Metodo que lista um venda pela sua id e traduz
        """
        pass
        # try:
        #     resposta = self.model.get_by_id(id)
        #     if resposta:
        #         return self.__traduz(resposta), 200
        # except Exception as erro:
        #     print(f'Erro: {erro}')
        #     return { 'msg': 'Venda não encontrado', 'status': 404 }, 404

        # return {}, 404
        
    def inserir(self, vendedor, cliente, produtos):
        """
            Metodo que insere um novo venda
        """
        if not vendedor and not cliente and not produtos:
            return { 'msg': 'Não foi possivel cadastrar o venda', 'status': 400 }, 400
        
        try:
            venda = Venda(vendedor=vendedor, cliente=cliente)
            self.model.add(venda=venda, produtos=produtos)
            return { 'msg': 'Venda cadastrado com sucesso', 'status': 201 }, 201
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Não foi possivel cadastrar o venda', 'status': 400 }, 400

    def atualizar(self, id, nome):
        """
            Metodo responsavel por atualizar uma venda pelo sua id
        """
        pass
        # try:
        #     self.vendedor_model.update(id, nome)
        #     return { 'msg': 'Venda alterado com sucesso', 'status': 202 }, 202
        # except Exception as erro:
        #     print(f'Erro: {erro}')
        #     return { 'msg': 'Venda não encontrado', 'status': 404 }, 404

    def deletar(self, id):
        """
            Metodo responsavel por deletar uma venda pela id
        """
        pass
        # try:
        #     self.vendedor_model.delete(id)
        #     return { 'msg': 'Venda deletado com sucesso', 'status': 202 }
        # except Exception as erro:
        #     print(f'Erro: {erro}')
        #     return { 'msg': 'Venda não encontrado', 'status': 404 }

    def __consulta_produtos(self, venda_id):
        return self.model.get_itens_carrinho(venda_id)

    def __traduz(self, venda):
        """
            Metodo responsavel por traduzir a resposta vinda do banco de dados
        """
        venda_id = venda.Venda.id
        itens = self.__consulta_produtos(venda.Venda.id)
        return { 
            'id': venda_id,
            'comissao_vendedor': self.__calcular_comissao(itens),
            'total_venda': self.__calcular_total_venda(itens),
            'vendedor': { 'id': venda.Vendedor.id, "nome": venda.Vendedor.nome }, 
            'cliente': { 'id': venda.Cliente.nome, 'nome': venda.Cliente.nome  },
            'itens:': self.__traz_produtos(itens)
        }
    

    def __traz_produtos(self, itens):        
        return list(map(lambda item: self.__traduz_carrinho(item), itens))

    def __traduz_carrinho(self, item):
        """
            Metodo responsavel por traduzir a resposta vinda do banco de dados
        """
        return {
                    'produto_id': item.Produto.id,
                    'produto': item.Produto.nome,
                    'comissao': "{:.2f} %".format(float(item.Carrinho.comissao)),
                    'carrinho_id': item.Carrinho.id,
                    'quantidade': item.Carrinho.quantidade,
                    'valor': "{:.2f}".format(float(item.Carrinho.valor)),
                }
    
    def __calcular_comissao(self, itens):
        """
            Metodo responsavel por calcular a comissão
        """
        itens_calcular = list(map(lambda item: (item.Carrinho.valor * item.Carrinho.quantidade) * (item.Carrinho.comissao / 100), itens))
        print(itens_calcular)
        return "{:.2f}".format(reduce(lambda a, b: a + b, itens_calcular))

    def __calcular_total_venda(self, itens):
        """
            Metodo responsavel por calcular o total da venda
        """
        itens_calcular = list(map(lambda item: item.Carrinho.valor * item.Carrinho.quantidade, itens))
        return "{:.2f}".format(reduce(lambda a, b: a + b, itens_calcular))