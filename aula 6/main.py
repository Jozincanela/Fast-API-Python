from fastapi import FastAPI
from data import lista_clientes
from Api_tools import *
from fastapi import FastAPI, HTTPException, status, Path

app = FastAPI(   title='Api Restaurante',
   version='0.0.1',
   description="Api com nomes de clientes e seu prato favorito",)

@app.get('/clientes',
        status_code=status.HTTP_200_OK,
        description='Retorna todos os clientes ou uma lista vazia.',
        summary='Retorna todos os clientes'
        )
async def get_clientes():
    try:
        return lista_clientes
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clientes não encontrados'
    )


@app.get('/cliente/{id}', status_code=status.HTTP_200_OK,
        description='Retorna todos os clientes ou uma lista vazia.',
        summary='Retorna todos os clientes')
async def get_cliente_id(id: int = Path(
    title='ID do curso',
    description=f'Deve ser de 1 a {len(lista_clientes)}',
    gt=0,
    lt=len(lista_clientes) + 1)
    ):
    try:
        resposta = get_by_id(id, lista_clientes)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Cliente não encontrado'
    )
        
        
@app.post('/novo-cliente/', status_code=status.HTTP_201_CREATED,
        description='Retorna o novo cliente criado.',
        summary='Retorna o novo cliente')
async def Novo_cliente(
    nome:str, prato_fav,data:str,conta:float):
    try:
        resposta = new_cliente(nome,prato_fav, data, conta, lista_clientes)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail='Alguma condição não foi cumprida')

        
@app.put('/atualizar-prato-favorito/', status_code=status.HTTP_202_ACCEPTED,
        description='Retorna o novo cliente atualizado.',
        summary='Retorna o novo cliente atualizado')
async def Atualizar_prato_favorito(
    id:int, prato_fav:str):
    try:
        resposta = atualizar_prato_fav(id, prato_fav, lista_clientes)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail='Alguma condição não foi cumprida')
            
@app.put('/nova-venda/', status_code=status.HTTP_202_ACCEPTED,
        description='Retorna o cliente com uma nova vinda.',
        summary='Retorna o cliente com uma nova venda')
async def Nova_venda(
    id:int, data:str, conta:float):
    try:
        resposta = Venda(id, data, conta,lista_clientes)
        return resposta
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Alguma condição não foi cumprida')
        
@app.delete('/deletar-cliente/{id}', status_code=status.HTTP_202_ACCEPTED,
        description='Retorna a lista de clientes.',
        summary='Retorna a lista de clientes')
async def Nova_venda(
    id: int = Path(
    title='ID do curso',
    description=f'Deve ser de 1 a {len(lista_clientes)}',
    gt=0,
    lt=len(lista_clientes) + 1)
    ):
    try:
        resposta = Delete_id(id,lista_clientes)
        return resposta
    except:
                raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Alguma condição não foi cumprida')