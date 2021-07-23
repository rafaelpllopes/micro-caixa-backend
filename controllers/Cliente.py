# -*- coding: utf-8 -*-
from models.Cliente import Cliente

class ClienteController:
    """
        Classe cliente com o metodos realizar as funções para o cliente
    """
    def __init__(self):
        self.cliente_model = Cliente()
    
    def listar_tudo(self):
        """
            Metodo que lista os clientes e traduz
        """
        try:
            resposta = self.cliente_model.get_all()
            return list(map(lambda cliente: self.__traduz(cliente), resposta)), 200
        except Exception as erro:
            print(f'Erro: {erro}')
        
        return [], 404
    
    def lista_por_id(self, id: int):
        """
            Metodo que lista um cliente pela sua id e traduz
        """
        try:
            resposta = self.cliente_model.get_by_id(id)
            if resposta:
                return self.__traduz(resposta), 200
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Cliente não encontrado', 'status': 404 }, 404

        return {}, 404
        
    def inserir(self, nome):
        """
            Metodo que insere um novo cliente
        """
        try:
            self.cliente_model.add(Cliente(nome = nome))
            return { 'msg': 'Cliente cadastrado com sucesso', 'status': 201 }, 201
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Não foi possivel cadastrar o cliente', 'status': 400 }, 400

    def atualizar(self, id, nome):
        """
            Metodo responsavel por atualizar um cliente pelo sua id
        """
        try:
            self.cliente_model.update(id, nome)
            return { 'msg': 'Cliente alterado com sucesso', 'status': 202 }, 202
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Cliente não encontrado', 'status': 404 }, 404

    def deletar(self, id):
        """
            Metodo responsavel por deletar um cliente pela id
        """
        try:
            self.cliente_model.delete(id)
            return { 'msg': 'Cliente deletado com sucesso', 'status': 202 }
        except Exception as erro:
            print(f'Erro: {erro}')
            return { 'msg': 'Cliente não encontrado', 'status': 404 }

    def __traduz(self, cliente):
        """
            Metodo responsavel por traduzir a resposta vinda do banco de dados
        """
        return { 'id': cliente.id, 'nome': cliente.nome, 'criado': cliente.criado, 'atualizado': cliente.atualizado }
