# -*- coding: utf-8 -*-
from json.encoder import JSONEncoder
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from config import app_active, app_config
from controllers.Cliente import ClienteController
from controllers.Vendedor import VendedorController
from controllers.Produto import ProdutoController
from controllers.Venda import VendaController

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        """
            Metodo somente para informar se a API esta rodando
        """
        return jsonify({ 'status' : 'API está rodando' }), 200

    @app.route('/clientes', methods=['GET', 'POST'])
    def clientes_listar_inserir():
        """
            Metodo para inserir um cliente "POST", ou trazer todos os clientes "GET"
        """
        cliente_controller = ClienteController()
        if request.method == 'POST':
            try:
                resposta = request.json
                if resposta:
                    nome = request.json['nome']
                    res, status = cliente_controller.inserir(nome)
                    return jsonify(res), status
            except Exception as erro:
                print({ "Erro: ": erro })
        
        resposta, status = cliente_controller.listar_tudo()
        return jsonify(resposta), status

    @app.route('/clientes/<id>', methods=['GET', 'PUT', 'DELETE'])
    def cliente_consultar_atualizar_deletar(id: int):
        """
            Metodo para consultar "GET", ou atualizar "PUT", ou deletar "DELETE" um cliente pela id
        """
        cliente_controller = ClienteController()
        if not id:
            return jsonify({ 'msg': 'Requer id', 'status': 404 }), 404

        if request.method == 'PUT':
            try:
                resposta = request.json
                if resposta:
                    nome = resposta['nome']
                    res, status = cliente_controller.atualizar(id, nome)
                    return jsonify(res), status
            except Exception as erro:
                return jsonify({ "erro": erro })
        
        if request.method == 'DELETE':
            try:
                res = cliente_controller.deletar(id)
                return jsonify(res), res['status']                
            except Exception as erro:
                return jsonify({ "erro": erro })
        
        resposta, status = cliente_controller.lista_por_id(id)
        return jsonify(resposta), status

    @app.route('/vendedores', methods=['GET', 'POST'])
    def vendedor_listar_inserir():
        """
            Metodo para inserir um vendedor "POST", ou trazer todos os vendedores "GET"
        """
        controller = VendedorController()
        if request.method == 'POST':
            try:
                resposta = request.json
                if resposta:
                    nome = request.json['nome']
                    res, status = controller.inserir(nome)
                    return jsonify(res), status
            except Exception as erro:
                print({ "Erro: ": erro })
        
        resposta, status = controller.listar_tudo()
        return jsonify(resposta), status

    @app.route('/vendedores/<id>', methods=['GET', 'PUT', 'DELETE'])
    def vendedor_consultar_atualizar_deletar(id: int):
        """
            Metodo para consultar "GET", ou atualizar "PUT", ou deletar "DELETE" um vendedor pela id
        """
        controller = VendedorController()
        if not id:
            return jsonify({ 'msg': 'Requer id', 'status': 404 }), 404

        if request.method == 'PUT':
            try:
                resposta = request.json
                if resposta:
                    nome = resposta['nome']
                    res, status = controller.atualizar(id, nome)
                    return jsonify(res), status
            except Exception as erro:
                return jsonify({ "erro": erro })
        
        if request.method == 'DELETE':
            try:
                res = controller.deletar(id)
                return jsonify(res), res['status']                
            except Exception as erro:
                return jsonify({ "erro": erro })
        
        resposta, status = controller.lista_por_id(id)
        return jsonify(resposta), status

    @app.route('/produtos', methods=['GET', 'POST'])
    def produto_listar_inserir():
        """
            Metodo para inserir um produto "POST", ou trazer todos os Produto "GET"
        """
        controller = ProdutoController()
        if request.method == 'POST':
            try:
                
                nome = request.json['nome']
                valor = request.json['valor']
                comissao = request.json['comissao']
                
                if nome and valor and comissao:
                    res, status = controller.inserir(nome=nome, valor=valor, comissao=comissao)
                    return jsonify(res), status
                else:
                    return jsonify({ 'msg': 'Os dados nome, valor, comissao são obrigatorios', "status": 404 }), 404
            except Exception as erro:
                print({ "Erro: ": erro })
        
        resposta, status = controller.listar_tudo()
        return jsonify(resposta), status

    @app.route('/produtos/<id>', methods=['GET', 'PUT', 'DELETE'])
    def produto_consultar_atualizar_deletar(id: int):
        """
            Metodo para consultar "GET", ou atualizar "PUT", ou deletar "DELETE" um produto pela id
        """
        controller = ProdutoController()
        if not id:
            return jsonify({ 'msg': 'Requer id', 'status': 404 }), 404

        if request.method == 'PUT':
            try:
                nome = request.json['nome']
                valor = request.json['valor']
                comissao = request.json['comissao']
                
                if nome and valor and comissao:
                    res, status = controller.atualizar(id, nome, valor, comissao)
                    return jsonify(res), status
                else:
                    return jsonify({ 'msg': 'Os dados nome, valor, comissao são obrigatorios', "status": 404 }), 404
            except Exception as erro:
                return jsonify({ "erro": erro })
        
        if request.method == 'DELETE':
            try:
                res = controller.deletar(id)
                return jsonify(res), res['status']                
            except Exception as erro:
                return jsonify({ "erro": erro })
        
        resposta, status = controller.lista_por_id(id)
        return jsonify(resposta), status
    
    @app.route('/vendas', methods=['GET', 'POST'])
    def venda_listar_inserir():
        """
            Metodo para inserir um vendas "POST", ou trazer todos os vendas "GET"
        """
        controller = VendaController()
        if request.method == 'POST':
            try:
                
                vendedor = request.json['vendedor']
                cliente = request.json['cliente']
                produtos = request.json['produtos']
                
                if vendedor and cliente and produtos:
                    res, status = controller.inserir(vendedor=vendedor, cliente=cliente, produtos=produtos)
                    return jsonify(res), status
                else:
                    return jsonify({ 'msg': 'Os dados vendedor, cliente, produtos são obrigatorios', "status": 404 }), 404
            except Exception as erro:
                print({ "Erro: ": erro })
        
        resposta, status = controller.listar_tudo()
        return jsonify(resposta), status

    @app.route('/vendas/<id>', methods=['GET', 'PUT', 'DELETE'])
    def venda_consultar_atualizar_deletar(id: int):
        """
            Metodo para consultar "GET", ou atualizar "PUT", ou deletar "DELETE" um produto pela id
        """
        controller = VendaController()
        if not id:
            return jsonify({ 'msg': 'Requer id', 'status': 404 }), 404

        if request.method == 'PUT':
            try:
                vendedor = request.json['vendedor']
                cliente = request.json['cliente']
                produtos = request.json['produtos']

                if vendedor and cliente and produtos:
                    res, status = controller.atualizar(id=id, vendedor=vendedor, cliente=cliente, produtos=produtos)
                    return jsonify(res), status
                else:
                    return jsonify({ 'msg': 'Os dados vendedor, cliente, produtos são obrigatorios', "status": 404 }), 404
            except Exception as erro:
                print(f'Erro [App - app.py - venda_consultar_atualizar_deletar - PUT]: {erro}')
        
        if request.method == 'DELETE':
            try:
                res = controller.deletar_venda(id)
                return jsonify(res), res['status']                
            except Exception as erro:
                print(f'Erro [App - app.py - venda_consultar_atualizar_deletar - DELETE]: {erro}')
        
        resposta, status = controller.lista_por_id(id)
        return jsonify(resposta), status
    
    @app.route('/vendas/<id_venda>/itens/<id_item>', methods=['GET', 'DELETE'])
    def remover_item_venda(id_venda: int, id_item: int):
        controller = VendaController()
        if request.method == 'DELETE':
            if not id_venda and not id_item:
                return jsonify({ 'msg': 'Requer id', 'status': 404 }), 404

            res, status = controller.deletar_item_carrinho(id_venda=id_venda, id_item=id_item)
            return jsonify(res), status
        
        resposta, status = controller.lista_item_por_id(id=id_item)
        return jsonify(resposta), status

    @app.route('/vendas/vendedor/<id>', methods=['GET'])
    def consutar_comissao_vendedor_por_periodo(id: int):
        controller = VendaController()
        
        if not id:
            return jsonify({ 'msg': 'Requer id', 'status': 404 }), 404
        
        try:
            inicial = request.json['inicial']
            final = request.json['final']

            if not inicial and not final:
                return jsonify({ 'msg': 'Requer data inicial e data final', 'status': 404 }), 404
            
            periodo = { 'inicial': inicial, 'final': final }
        except Exception as erro:
                print(f'Erro [App - app.py - venda_consultar_atualizar_deletar - GET]: {erro}')
                return jsonify({ 'msg': 'Não foi possivel calcular a comissao', 'status': 404 }), 404

        res, status = controller.calcular_comissao_vendedor_por_periodo(id=id, periodo=periodo)
        return jsonify(res), status

    return app


