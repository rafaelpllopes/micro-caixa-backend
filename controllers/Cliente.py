# -*- coding: utf-8 -*-
from models.Cliente import Cliente

class ClienteController:
    """
        Classe cliente com o metodos realizar as funções para o cliente
    """
    def __init__(self):
        self.cliente_model = Cliente()
    
    def listar_tudo(self):
        try:
            resposta = self.cliente_model.get_all()
            return list(map(lambda cliente: self.__traduz(cliente), resposta))
        except Exception as erro:
            print(f'Erro: {erro}')
            raise Exception('Erro ao listar os clientes')
        
        return []
    
    def lista_por_id(self, id: int):
        try:
            resposta = self.cliente_model.get_by_id(id)
            if resposta:
                return self.__traduz(resposta)
        except Exception as erro:
            print(f'Erro: {erro}')
            raise Exception('Erro ao lista o cliente por id')
        
        return {}
        
    def inserir(self, cliente):
        try:
            self.cliente_model.add(Cliente(nome = cliente['nome']))
        except Exception as erro:
            print(f'Erro: {erro}')
            raise Exception('Erro ao inserir o cliente')

    def __traduz(self, cliente):
        return { 'id': cliente.id, 'nome': cliente.nome, 'criado': cliente.criado, 'atualizado': cliente.atualizado }
