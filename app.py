# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from config import app_active, app_config

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return jsonify({ 'status' : 'API está rodando'}), 200

    return app

