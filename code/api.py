from flask import Flask,request
from flask_pydantic_spec import FlaskPydanticSpec,Request

server_app = Flask(__name__)
spec = FlaskPydanticSpec('flask',title = 'Um pouco sobre apis')
spec.register(server_app)

@server_app.get('/recurso')
def pegar_algo():
    return 'Estou pegando'

@server_app.post('/pessoas')
@spec.validate(
    body=Request(Pessoa), resp=Response(HTTP_200=Pessoa)
)
def inserir_pessoa():
    """Insere uma Pessoa no banco de dados."""
    body = request.context.body.dict()
    return body

server_app.run()