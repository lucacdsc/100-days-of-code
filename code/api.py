from itertools import count
from typing import Optional
from flask import Flask,request,jsonify
from flask_pydantic_spec import FlaskPydanticSpec,Request,Response
from pydantic import BaseModel,Field
from tinydb import TinyDB,Query

server_app = Flask(__name__)
spec = FlaskPydanticSpec('flask',title = 'Um pouco sobre apis')
spec.register(server_app)
database = TinyDB('database.json')
c = count()

class Pessoa(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    nome: str
    idade: int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int


@server_app.get('/pessoas/<int:id>')
@spec.validate(resp=Response(HTTP_200=Pessoa))
def buscar_pessoa(id):
    """Retorna todas as pessoas da base de dados."""
    try:
        pessoa = database.search(Query().id == id)[0]
    except IndexError:
        return {'message': 'Pessoa não encontrada'}
    return jsonify(pessoa)

@server_app.post('/pessoas')
@spec.validate(
    body=Request(Pessoa), resp=Response(HTTP_200=Pessoa)
)
def inserir_pessoa():
    """Insere uma Pessoa no banco de dados."""
    body = request.context.body.dict()
    database.insert(body)
    return body

@server_app.put('/pessoas/<int:id>')
@spec.validate(
    body=Request(Pessoa), resp=Response(HTTP_200=Pessoa)
)
def altera_pessoa(id):
    """Altera uma pessoa do banco de dados."""
    Pessoa = Query()
    body = request.context.body.dict()
    database.update(body, Pessoa.id == id)
    return jsonify(body)

@server_app.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deleta_pessoa(id):
    """Deleta uma pessoa do banco de dados."""
    Pessoa = Query()
    database.remove(Pessoa.id == id)
    return jsonify({})

server_app.run()