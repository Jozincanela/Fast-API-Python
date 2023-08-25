from data import lista_clientes
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()
# leitura incrementação update e delete de produtos

def calculo_imc(altura: float, peso: float) -> float:
    imc = peso/(altura * altura)
    return imc

def classificacao_imc(imc: float) -> str:
    if imc <= 18.5 :
        classficacao = "baixo peso"
    elif imc>=18.5 and imc <= 24.9:
        classficacao = "peso normal"
    elif imc>=25.00 and imc <= 29.9:
        classficacao = "sobrepeso"
    elif imc>=30.00 and imc <= 34.9:
        classficacao = "obesidade grau 1"
    elif imc>=35.00 and imc <= 39.9:
        classficacao = "obesidade grau 2"
    elif imc>= 40.00:
        classficacao = "obesidade grau 3"
        
    return classficacao
    
    
@app.get('/get-todos-alunos-sem-dados/', status_code=status.HTTP_200_OK)
async def get():
    try:
        data_basic = []
        for clientes in lista_clientes:
            data_basic.append({'id': clientes['id'], 'nome': clientes['nome'] , })
        return data_basic
    except:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Alunos não encontrados')


@app.get('/get-todos-alunos/', status_code=status.HTTP_200_OK)
async def get():
    try:
        return lista_clientes
    except: 
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Alunos não encontrados')


@app.get('/get-ultimo-aluno/', status_code=status.HTTP_200_OK)
async def get():
    try:
        ultimo = len(lista_clientes)
        return lista_clientes[ultimo-1]
    except: 
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Aluno não encontrado')


@app.get('/get-ultimo-aluno/', status_code=status.HTTP_200_OK)
async def get():
    try:
        return lista_clientes[-1]
    except: 
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Aluno não encontrado')
    
@app.post('/post-aluno', status_code=status.HTTP_201_Created)
async def post(nome: str, peso:float, altura: float, data:str):
    try
        new_id = len(lista_clientes)
        imc = calculo_imc(altura, peso)
        lista_clientes.append({
            'id' : new_id+1,
            'nome': nome,
            'altura' : altura,
            'peso': peso,
            'avaliações' : [{'data' : data,
            'imc' : round(imc),
            'classificacao': classificacao_imc(imc)}]
        })
        return lista_clientes
    except:
        raise HTTPException(
        status_code=status.HTTP_406_Not_Acceptable,
        detail='Alguma condição não foi cumprida')


    
@app.put('/post-avaliação', status_code=status.HTTP_202_Accepted)
async def update(id:int, peso:float, data: str):
    try
        id_cliente =lista_clientes[id-1]
        altura = id_cliente['altura']
        id_cliente['avaliações'].append({
            'data' : data,
            'imc' : round(calculo_imc(altura, peso) , 2),
            'classificacao': classificacao_imc(round(calculo_imc(altura, peso), 2))
        })
        id_cliente['peso'] = peso
        return lista_clientes[id-1]
    except:
        raise HTTPException(
        status_code=status.HTTP_304_Not_Modified,
        detail='Não foi possivel modificar o aluno')

        
    
    
@app.delete ('/delete-produto/{id}', status_code=status.HTTP_200_OK)
async def delete(id : int):
    try:
        lista_clientes.pop(id-1)
        
        news_ids = 0
        for alunos in lista_clientes:
            news_ids += 1
            alunos['id'] = news_ids

        return lista_clientes
    except:
         raise HTTPException(   
        status_code=status.HTTP_404_Not_Found,
        detail='Não foi possivel modificar o aluno')