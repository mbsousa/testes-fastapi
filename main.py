""" sempre quando utilizo um nome depois de from, isso significa que estou chamando
uma biblioteca que possui uma classe em específico que quero utilizar. """

from fastapi import FastAPI

""" BaseModel do módulo pydantic é uma biblioteca pra validação de dados e criação de 
modelos de dados baseados em Python. """
from pydantic import BaseModel 

""" a classe ULID da biblioteca ulid, é usada para gerar identificadores únicos. """
from ulid import ULID


#instância
app = FastAPI()

@app.get("/home")
def home():
    return "Bem vindos aos Jogos Olímpicos 2024"

