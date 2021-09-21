from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
from Util.connections import *

app = FastAPI()

#rota raiz
@app.get("/")
def home():
    d = datetime.today() - timedelta(hours=3, minutes=00)

    data_hora_atual = d.strftime('%d/%m/%Y %H:%M:%S')

    return ("Todos Conectados!!! Bem vindo ao Fideliza !!! ", data_hora_atual)

class Usuario(BaseModel):
    id: int
    email: str
    senha: str

#base de dados para teste
base_de_dados = [
    Usuario(id=1, email='teste1@teste', senha='teste123'),
    Usuario(id=2, email='teste2@teste', senha='teste234')
]

#rota para buscar todos os dados no banco

@app.get('/all_users')
def all_users():
    conn = connection()
    con = conn.conect()
    cursor = conn.cursor(con)
    return conn.execute(cursor, """ select * from usuarios""")
# #rota para buscar por id os dados no banco

@app.get('/user')
def user(id_user:int):
    for user in base_de_dados:
        if (user.id == id_user):
            return user
    return {"Status": 404, "Mensagem": "Usuario não encontrado."}

@app.post('/user')
def insert_user(user:Usuario):
    #Regra de negocio com as restrições aqui

    base_de_dados.append(user)
    return user

@app.delete('/delete')
def delete_user(id_user:int):
    for user in base_de_dados:
        if(user.id == id_user):
            base_de_dados.remove(user)
            return {"Status": 200, "Mensagem": "Usuario deletado com sucesso."}

    return {"Status": 404, "Mensagem": "Usuario não encontrado."}

