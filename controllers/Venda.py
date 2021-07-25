# -*- coding: utf-8 -*-
from models.Venda import Venda
from models.Carrinho import Carrinho

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
        pass
        # try:
        #     resposta = self.model.get_all()
        #     return list(map(lambda venda: self.__traduz(venda), resposta)), 200
        # except Exception as erro:
        #     print(f'Erro: {erro}')
        
        # return [], 404
    
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

    def __traduz(self, vendedor):
        """
            Metodo responsavel por traduzir a resposta vinda do banco de dados
        """
        pass
    
    def __calcular_comissao(self, valor, percentual):
        """
            Metodo responsavel por calcular a comissão
        """
        pass
        
