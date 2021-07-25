# -*- coding: utf-8 -*-
from models.Produto import Produto

class ProdutoController:
    """
        Classe produto com o metodos realizar as funções para o produto
    """
    def __init__(self):
        self.produto_model = Produto()
    
    def listar_tudo(self):
        """
            Metodo que lista os produto e traduz
        """
        try:
            resposta = self.produto_model.get_all()
            return list(map(lambda produto: self.__traduz(produto), resposta)), 200
        except Exception as erro:
            print(f'Erro: {erro}')
        
        return [], 404
    
    def lista_por_id(self, id: int):
        """
            Metodo que lista um produto pela sua id e traduz
        """
        try:
            resposta = self.produto_model.get_by_id(id)
            if resposta:
                return self.__traduz(resposta), 200
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Produto não encontrado', 'status': 404 }, 404

        return {}, 404
        
    def inserir(self, nome, valor, comissao):
        """
            Metodo que insere um novo produto
        """
        if not nome and not valor and not comissao:
            return { 'msg': 'Não foi possivel cadastrar o produto', 'status': 400 }, 400

        try:
            self.produto_model.add(Produto(nome=nome, valor=valor, comissao_percentual=comissao))
            return { 'msg': 'Produto cadastrado com sucesso', 'status': 201 }, 201
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Não foi possivel cadastrar o produto', 'status': 400 }, 400

    def atualizar(self, id, nome, valor, comissao):
        """
            Metodo responsavel por atualizar um produto pelo sua id
        """
        if not id and not nome and not valor:
            return { 'msg': 'Não foi possivel atualizar o produto', 'status': 400 }, 400

        try:
            self.produto_model.update(id, nome, valor, comissao)
            return { 'msg': 'Cliente alterado com sucesso', 'status': 202 }, 202
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Cliente não encontrado', 'status': 404 }, 404

    def deletar(self, id):
        """
            Metodo responsavel por deletar um cliente pela id
        """
        if not id:
            return { 'msg': 'Não foi possivel deletar o produto', 'status': 400 }, 400

        try:
            self.produto_model.delete(id)
            return { 'msg': 'Cliente deletado com sucesso', 'status': 202 }
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Cliente não encontrado', 'status': 404 }

    def __traduz(self, produto):
        """
            Metodo responsavel por traduzir a resposta vinda do banco de dados
        """
        return { 'id': produto.id, 'nome': produto.nome, 'valor': "{:.2f}".format(float(produto.valor)), 'comissao': "{:.2f}".format(float(produto.comissao_percentual)), 'criado': produto.criado, 'atualizado': produto.atualizado }