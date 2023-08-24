from fastapi import FastAPI
import random
from data import lista_produtos
from data import lista_vendas
        
app = FastAPI()
# leitura incrementação update e delete de produtos
@app.get('/get-produtos/')
async def get(id: str):
    if id == '0':
        return lista_produtos
    elif id != '0':
        return lista_produtos[id]
    
@app.post('/post-produto')
async def post(nome: str, qnt: int, valor: float):
    new_id = str(len(lista_produtos) + 1)
    novo_produto = {
        'nome': nome,
        'quantidade': qnt,
        'valor': valor,
    }
    lista_produtos[new_id] = novo_produto
    return lista_produtos
    
@app.put ('/update-produto/{id}')
async def update(id: str, qnt: int, valor: float):
    produto_update = lista_produtos[id]
    produto_update['valor'] = valor
    produto_update['quantidade'] = qnt
    return lista_produtos
    
@app.delete ('/delete-produto/{id}')
async def delete(id : str):

    lista_produtos.pop(id)
    
    news_ids = 0
    for produtos in lista_produtos:
        lista_produtos[produtos] : lista_produtos[str(news_ids)]
        
    return lista_produtos
        
@app.put('/venda-produto/{id}')
async def venda(id:str, qnt:int):
    produto_update =  lista_produtos[id]
    if produto_update['quantidade'] == 0:
        clausula_final = "Fora de estoque"
    else:
        produto_update['quantidade'] -= qnt
        valor_a_ser_pago = qnt * produto_update['valor']
        pagar = f"deverá ser pago {valor_a_ser_pago}$ RS"

        new_id = str(len(lista_vendas) + 1)
        produto = lista_produtos[id]
        nova_venda = {
        'nome': produto_update['nome'],
        'quantidade': qnt,
        'valor_venda': valor_a_ser_pago,
        }
        lista_vendas[new_id] = nova_venda
        clausula_final = f"{pagar}  " ,lista_vendas[new_id] ,"lista de produtos atualizada", lista_produtos

    return clausula_final

    

