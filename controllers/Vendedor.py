# -*- coding: utf-8 -*-
from models.Vendedor import Vendedor

class VendedorController:
    """
        Classe vendedor com o metodos realizar as funções para o vendedor
    """
    def __init__(self):
        self.vendedor_model = Vendedor()
    
    def listar_tudo(self):
        """
            Metodo que lista os vendedors e traduz
        """
        try:
            resposta = self.vendedor_model.get_all()
            return list(map(lambda vendedor: self.__traduz(vendedor), resposta)), 200
        except Exception as erro:
            print(f'Erro [Controllers - Vendedor.py - listar_tudo]: {erro}')
        
        return [], 404
    
    def lista_por_id(self, id: int):
        """
            Metodo que lista um vendedor pela sua id e traduz
        """
        try:
            resposta = self.vendedor_model.get_by_id(id)
            if resposta:
                return self.__traduz(resposta), 200
        except Exception as erro:
            print(f'Erro [Controllers - Vendedor.py - lista_por_id]: {erro}')
            return { 'msg': 'vendedor não encontrado', 'status': 404 }, 404

        return {}, 404
        
    def inserir(self, nome):
        """
            Metodo que insere um novo vendedor
        """
        try:
            self.vendedor_model.add(Vendedor(nome = nome))
            return { 'msg': 'vendedor cadastrado com sucesso', 'status': 201 }, 201
        except Exception as erro:
            print(f'Erro [Controllers - Vendedor.py - inserir]: {erro}')
            return { 'msg': 'Não foi possivel cadastrar o vendedor', 'status': 400 }, 400

    def atualizar(self, id, nome):
        """
            Metodo responsavel por atualizar um vendedor pelo sua id
        """
        try:
            self.vendedor_model.update(id, nome)
            return { 'msg': 'vendedor alterado com sucesso', 'status': 202 }, 202
        except Exception as erro:
            print(f'Erro [Controllers - Vendedor.py - atualizar]: {erro}')
            return { 'msg': 'vendedor não encontrado', 'status': 404 }, 404

    def deletar(self, id):
        """
            Metodo responsavel por deletar um vendedor pela id
        """
        try:
            self.vendedor_model.delete(id)
            return { 'msg': 'vendedor deletado com sucesso', 'status': 202 }, 202
        except Exception as erro:
            print(f'Erro [Controllers - Vendedor.py - deletar]: {erro}')
            return { 'msg': 'vendedor não encontrado', 'status': 404 }, 404

    def __traduz(self, vendedor):
        """
            Metodo responsavel por traduzir a resposta vinda do banco de dados
        """
        return { 'id': vendedor.id, 'nome': vendedor.nome, 'criado': vendedor.criado, 'atualizado': vendedor.atualizado }
