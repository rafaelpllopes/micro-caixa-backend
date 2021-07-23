# -*- coding: utf-8 -*-
from json.encoder import JSONEncoder
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from config import app_active, app_config
from controllers.Cliente import ClienteController

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route('/')
    def index():
        return jsonify({ 'status' : 'API está rodando' }), 200

    @app.route('/clientes', methods=['GET', 'POST'])
    def clientes_listar_inserir():
        cliente_controller = ClienteController()
        if request.method == 'POST':
            try:
                resposta = request.json
                if resposta:
                    cliente_controller.inserir(resposta)
                    return jsonify({ 'msg': 'Cliente inserido com sucesso', 'status': 201}), 201
            except Exception as erro:
                return jsonify({ "erro": erro })
        
        resposta = cliente_controller.listar_tudo()
        return jsonify(resposta), 200

    @app.route('/clientes/<id>', methods=['GET', 'PUT'])
    def cliente_consultar_atualizar_deletar(id: int):
        cliente_controller = ClienteController()
        if not id:
            return jsonify({ 'msg': 'Requer id', 'status': 404 }), 404

        # if request.method == 'PUT':
        #     try:
        #         resposta = request.json
        #         if resposta:
        #             cliente_controller.inserir(resposta)
        #             return jsonify({ 'msg': 'Cliente alterado com sucesso', 'status': 201 }), 201
        #     except Exception as erro:
        #         return jsonify({ "erro": erro })
        
        resposta = cliente_controller.lista_por_id(id)
        return jsonify(resposta), 200

    return app

