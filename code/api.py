from flask import Flask

server_app = Flask(__name__)

@server_app.get('/recurso')
def pegar_algo():
    return 'Estou pegando'

server_app.run()