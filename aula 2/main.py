from fastapi import FastAPI
from data import lista_alunos
app = FastAPI()

id = 3


@app.get('/get-alunos')
async def get():
    return lista_alunos

@app.get('/get-alunos/{id}')
async def get_by_id(id:int):
    return lista_alunos[id-1]


@app.post('/post-aluno')
async def post(nome:str):
        new_id = len(lista_alunos) + 1
        lista_alunos.append({'id' : new_id ,'nome':nome })
        return lista_alunos

@app.put('/update-aluno/{id}')
async def update(id:int, nome:str):
    id_int = int(id) -1
    aluno_update = lista_alunos[id_int]
    aluno_update ['nome'] = nome
    return lista_alunos

@app.delete('/delete-aluno/{id}')
async def delete (id:int):
    int_id = int(id)-1
    lista_alunos.pop(int_id)
    
    
    new_id  = 0
    for aluno in lista_alunos:
        new_id +=1
        aluno['id'] = new_id
        
    return lista_alunos
    
