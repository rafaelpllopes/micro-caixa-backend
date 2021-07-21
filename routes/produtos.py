from flask import jsonify, request
from config import app_config, app_active
config = app_config[app_active]

app = config.APP

@app.route('/')
def consultar():
    return jsonify({ 'status' : 'ok'})