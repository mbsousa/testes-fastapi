""" sempre ao referenciar um nome depois de from, isso significa que está sendo chamando
uma biblioteca que possui uma classe em específico que será utilizada. """

from fastapi import FastAPI

""" BaseModel do módulo pydantic é uma biblioteca pra validação de dados e criação de 
modelos de dados baseados em Python. """
from pydantic import BaseModel 

""" a classe ULID da biblioteca ulid, é usada para gerar identificadores únicos. """
from ulid import ULID


#instância
app = FastAPI()

esportes = [
    {
        'id': str(ULID()),
        'nome': 'Vôlei',
        'tipo': 'Feminino',
        'coletivo': True
    },
    {
        'id': str(ULID()),
        'nome': 'Skate', 
        'tipo': 'Masculino',
        'coletivo': False
    },    
    {
        'id': str(ULID()),
        'nome': 'Salto em distância', 
        'tipo': 'Feminino',
        'coletivo': False
    },
    {
        'id': str(ULID()),
        'nome': 'Lançamento de disco', 
        'tipo': 'Feminino',
        'coletivo': False
    },
    {
        'id': str(ULID()),
        'nome': 'Taekwondo', 
        'tipo': 'Masculino',
        'coletivo': False
    },
    {
        'id': str(ULID()),
        'nome': 'Tênis de mesa', 
        'tipo': 'Masculino',
        'coletivo': False
    },
    {
        'id': str(ULID()),
        'nome': 'Escalada Esportiva', 
        'tipo': 'Feminino',
        'coletivo': False
    },
    {
        'id': str(ULID()),
        'nome': 'Judô', 
        'tipo': 'Feminino',
        'coletivo': False
    },
        {
        'id': str(ULID()),
        'nome': 'Corrida', 
        'tipo': 'Feminino',
        'coletivo': False
    },
]

""" Classe usada pra ser referenciada no método post """
class Esporte(BaseModel):
    nome: str
    tipo: str
    coletivo: bool

""" Retorna a lista de esportes """
@app.get("/esportes")
def esportes_lista():
    return esportes

""" Isola a lista de esportes com endpoint do id específico """
@app.get("/esportes/{id}")
def esporte_detalhes(id:str):
    for esporte in esportes:
        if esporte['id'] == id:
            return esporte
    return {}

""" Cria uma nova lista de esportes """
@app.post('/esportes')
def esporte_criar(esporte: Esporte):
    esportes.append({
        'id': str(ULID()),
        'nome': esporte.nome,
        'tipo': esporte.tipo,
        'coletivo': esporte.coletivo,
    })
    return {}

""" Deleta uma lista de esportes """
@app.delete('/esportes')
def esporte_delete(esporte: Esporte):
    for elemento in esportes:
        if elemento['id'] == id:
            esportes.remove(elemento)
            return {}
    return {}

""" Atualiza lista de esportes """
@app.put('/esportes/{id}')
def esporte_atualizar(id:str, esporte_atualizado: Esporte):
    for elemento in esportes:
        if elemento['id'] == id:
            elemento['nome'] = esporte_atualizado.nome
            elemento['tipo'] = esporte_atualizado.tipo
            elemento['coletivo'] = esporte_atualizado.coletivo
            return elemento
    return {}

""" Home da page """
@app.get("/home")
def home():
    return "Bem vindos aos Jogos Olímpicos 2024"

