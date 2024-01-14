from flask import Flask,request,jsonify
from flask_pydantic_spec import FlaskPydanticSpec,Request,Response
from pydantic import BaseModel
from tinydb import TinyDB,Query

server_app = Flask(__name__)
spec = FlaskPydanticSpec('flask',title = 'Um pouco sobre apis')
spec.register(server_app)
database = TinyDB('database.json')

class Pessoa(BaseModel):
    id: int
    nome: str
    idade: int

@server_app.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoa))
def pegar_algo():
    """Retorna todas as pessoas da base de dados."""
    return jsonify(database.all())

@server_app.post('/pessoas')
@spec.validate(
    body=Request(Pessoa), resp=Response(HTTP_200=Pessoa)
)
def inserir_pessoa():
    """Insere uma Pessoa no banco de dados."""
    body = request.context.body.dict()
    database.insert(body)
    return body

server_app.run()