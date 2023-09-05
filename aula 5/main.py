from fastapi import FastAPI
from apiTools import *
from data import lista_cliente
from fastapi import FastAPI, Depends, HTTPException, status
app = FastAPI()

@app.get('/cliente', status_code=status.HTTP_200_OK)
async def get_clientes():
    try:
        fake_db()
        return lista_cliente
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clientes não encontrados')

@app.get('/cliente/{id}', status_code=status.HTTP_200_OK)
async def get_clientes_id(id: int):
    try:
        fake_db()
        return lista_cliente[id-1]
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clientes não encontrados')

@app.post('/post-cliente/', status_code=status.HTTP_200_OK)
async def get_clientes_id(Nome:str, prato_favorito: str):
    try:
        fake_db()
        novo_id = len(lista_cliente)
        novo_cadastro ={
            "id": novo_id,
            "nome": Nome,
            "prato_favorito": prato_favorito
        }
        lista_cliente.append(novo_cadastro)
        return lista_cliente[novo_id]
    except:
        raise HTTPException(
        status_code=status.HTTP_406_Not_Acceptable,
        detail='não foi possivel criar novo cliente')

@app.put('/atualizar-cliente/{id}', status_code=status.HTTP_200_OK)
async def get_clientes_id(id:int, Nome:str, prato_favorito: str):
    try:
        fake_db()
        lista_cliente[id-1] = {
            "id": id,
            "nome": Nome,
            "prato_favorito": prato_favorito
        }
        return lista_cliente[id-1]
    except:
        raise HTTPException(
        status_code=status.HTTP_406_Not_Acceptable,
        detail='Não foi possivel atulalizar cliente')
        
@app.delete('/deletar-cliente/{id}', status_code=status.HTTP_200_OK)
async def get_clientes_id(id: int):
    try:
        fake_db()
        lista_cliente.pop(id-1)
        news_ids = 0
        for clientes in lista_cliente:
            news_ids+=1
            clientes['id'] = news_ids
            
        return lista_cliente
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clientes não encontrados')