from pymongo import MongoClient
client = MongoClient('localhost:27017')

db = client.desafio

matricula = db.aeronave.find_one({'matricula':"PTNQX"})
print(matricula)


