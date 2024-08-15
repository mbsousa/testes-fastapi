""" atributos: origem, destino, distancia(km), valor(R$6,65 + R$ 2/km),
    estado('Requisitada','Em Andamento', 'Finalizado') """

""" Post - Criar corrida """
""" Get - Listar corrida  """
""" Delete - Remover corrida """
""" Post - Iniciar corrida """
""" Post - Finalizar corrida """

from fastapi import FastAPI, HTTPException, Response, Request
from pydantic import BaseModel
from ulid import ULID

app = FastAPI()

class Corrida(BaseModel):
    """ na criação da corrida o id não existe, então será None inicialmente; 
     depois que o objeto de corrida é criado e armazenado, o ID será gerado automaticamente """
    id: str 
    origem: str
    destino: str
    distancia: int
    valor: float 
    estado: str 

""" O estado('Requisitada','Em Andamento', 'Finalizado') será referenciado pelo ID 
para verificar o status da corrida. """

def calculo_valor(distancia: int) -> float:
    tarifa = 6.65
    km = 2.00
    total = tarifa + (km * distancia) 
    return total

corridas: list[Corrida] = [
  Corrida(
        id=str(ULID()), 
        origem='Tancredo', 
        destino='Centro', 
        distancia=8, 
        valor=calculo_valor(8), 
        estado='Requisitada'),
    Corrida(
        id=str(ULID()), 
        origem='Renascença', 
        destino='Pedra Mole', 
        distancia=15, 
        valor=calculo_valor(8), 
        estado='Em andamento'),
    Corrida(
        id=str(ULID()), 
        origem='Lourival Parente', 
        destino='Dirceu', 
        distancia=10, 
        valor=calculo_valor(8), 
        estado='Finalizada'),
]
  
@app.get('/corridas')
def corrida_lista() -> list[Corrida]:
    return corridas

""" Filtra a lista pelo estado """
@app.get('/corridas/{estado}')
def lista_estado(estado:str) -> list[Corrida]:
    if estado:
        return [c for c in corridas if c.estado.lower() == estado.lower()]
    return corridas

""" Detalha a corrida específica pelo ID """
@app.get('/corridas/{id}')
def corrida_detalhes(id: str) -> Corrida:
    for c in corridas: 
        if c.id == id: 
            return c
    raise HTTPException(status_code=404, detail='Corrida não localizada!')

""" Cria uma nova corrida """
@app.post('/corridas')
def corrida_criar(corrida: Corrida):
    corrida.id = str(ULID())
    corrida.valor = calculo_valor(corrida.distancia)
    corrida.estado = 'Requisitada'
    corridas.append(corrida)
    return corrida

""" Atualiza a corrida """
@app.put('/corridas/{id}')
def corrida_atualizar(id:str, corrida_atualizar: Corrida):
    for c in corridas:
        if c.id == id:
            if c.estado in ['Requisitada', 'Em andamento']:
                c.origem = corrida_atualizar.origem
                c.destino = corrida_atualizar.destino
                c.distancia = corrida_atualizar.distancia
                c.valor = calculo_valor(corrida_atualizar.distancia) 
                return c
            raise HTTPException(status_code=400, detail='A corrida não pode ser alterada.')
    raise HTTPException(status_code=404, detail='Corrida não localizada!')


@app.post('/corridas/{id}/iniciar' )
def iniciar(id:str) -> Corrida:
    for c in corridas:
        if c.id == id:
            if c.estado == 'Requisitada':
                c.estado = 'Em andamento'
                return c 
            raise HTTPException(status_code=400, detail='A corrida só pode iniciar se estiver requisitada')
    raise HTTPException(status_code=404, detail='Corrida não localizada!')

@app.post('/corridas/{id}/finalizar')
def finalizar(id:str) -> Corrida:
    for c in corridas:
        if c.id == id:
            if c.estado == 'Em andamento':
                c.estado = 'Finalizada'
                return c
            raise HTTPException(status_code=400, detail='A corrida só pode ser finalizada se estiver em andamento.')
    raise HTTPException(status_code=404, detail='Corrida não localizada!')

""" Remove a corrida retornando 204 """
@app.delete('/corridas/{id}')
def corrida_remover(id: str):
    for c in corridas:
        if c.id == id: 
            corridas.remove(c)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail='Corrida não localizada!')
