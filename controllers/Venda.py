# -*- coding: utf-8 -*-
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
        try:
            resposta = self.model.get_by_id(id)
            if resposta:
                return self.__traduz(resposta), 200
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'venda não encontrado', 'status': 404 }, 404

        return {}, 404
        
    def inserir(self, vendedor, cliente, itens):
        """
            Metodo que insere um novo venda
        """
        try:
            self.vendedor_model.add(Venda(vendedor=vendedor, cliente=cliente, itens=itens, valor_venda=valor, comissao=comissao))
            return { 'msg': 'vendedor cadastrado com sucesso', 'status': 201 }, 201
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Não foi possivel cadastrar o vendedor', 'status': 400 }, 400

    def atualizar(self, id, nome):
        """
            Metodo responsavel por atualizar um vendedor pelo sua id
        """
        try:
            self.vendedor_model.update(id, nome)
            return { 'msg': 'vendedor alterado com sucesso', 'status': 202 }, 202
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'vendedor não encontrado', 'status': 404 }, 404

    def deletar(self, id):
        """
            Metodo responsavel por deletar um vendedor pela id
        """
        try:
            self.vendedor_model.delete(id)
            return { 'msg': 'vendedor deletado com sucesso', 'status': 202 }
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'vendedor não encontrado', 'status': 404 }

    def __traduz(self, vendedor):
        """
            Metodo responsavel por traduzir a resposta vinda do banco de dados
        """
        return { 'id': vendedor.id, 'nome': vendedor.nome, 'criado': vendedor.criado, 'atualizado': vendedor.atualizado }
    
    def __calcular_comissao(self, valor, percentual):
        """
            Metodo responsavel por calcular a comissão
        """
        
