# -*- coding: utf-8 -*-
import os

class Config(object):
    """
        Classe pai com atributos comuns para as classes filhas
            CSRF: Habilita o uso de criptografia
            SECRET: Utilizada para criar chaves e valores criptografados
            APP: recebe a propriedade do app, de acordo com o tipo do ambiente
            SQLALCHEMY_DATABASE_URI: variavel que contém o acesso a url do banco de dados
    """
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET_FLASK') # carregar a variavel de ambiente SECRET_FLASK com a chave
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    APP = None

class DevConfig(Config):
    """
        Classe com as configurações para ambiente de desenvolvimento
            TESTING: habilita o ambiente de test com recursos especificos
            DEBUB: habilita no exibição no console do debug
            IP_HOST: host onde ficara disponivel a pagina
            PORT_HOST: porta disponivel do app
    """
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000 
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

class TesteConfig(Config):
    """
        Classe com as configurações para ambiente de teste
            TESTING: habilita o ambiente de test com recursos especificos
            DEBUB: habilita no exibição no console do debug
            IP_HOST: host onde ficara disponivel a pagina
            PORT_HOST: porta disponivel do app
    """
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5001 
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

class ProducaoConfig(Config):
    """
        Classe com as configurações para ambiente de producao
            TESTING: habilita o ambiente de test com recursos especificos
            DEBUB: habilita no exibição no console do debug
            IP_HOST: host onde ficara disponivel a pagina
            PORT_HOST: porta disponivel do app
    """
    TESTING = False
    DEBUG = False
    IP_HOST = '0.0.0.0' # disponivel para toda a rede
    PORT_HOST = 8000 
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

"""
    Dicionario que devolve o ambiente de acordo com a classe informada
        app_config['dev'], para utilizar como desenvolvedor
"""
app_config = {
    'development': DevConfig(),
    'production': ProducaoConfig(),
    'testing': TesteConfig()
}

"""
    Variavel que carrega a variavel de ambiente com o ambiente que deve ser utilizado
"""
app_active = os.getenv('FLASK_ENV') # carregar a variavel de ambiente FLASK_ENV

"""
export FLASK_ENV=development && export SECRET_FLASK=*djjuqWEGJ3355@3fdf && export DATABASE_URL=postgresql+psycopg2://postgres:123@localhost:5432/micro_caixa
"""