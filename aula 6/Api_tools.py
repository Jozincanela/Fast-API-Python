def get_by_id(id,lista_cliente):
    """seleciona um usuario da base de dados

    Args:
        id (int): id do usuario
        lista_cliente (list): lista de todos os clientes da base de dados

    Returns:
        list: todos os dados do cliente
    """
    return lista_cliente[id-1]

def new_cliente(nome, prato_fav, data, conta, lista_cliente):
    """
    Cria um novo cliente na lista de clientes

    Args:
        nome (str): Nome do novo cliente
        prato_fav (str): O prato favorito deste cliente
        data (str): a data da primeira vez deste cliente no restaurante
        conta (float): o valor que o cliente pagou na primeira vez que o mesmo foi no restaurante
        lista_cliente (list): lista de todos os clientes da base de dados

    Returns:
        list: todos os dados do novo cliente
    """
    new_id = len(lista_cliente)+1
    dados =   {  "id": new_id,
    "nombre": nome,
    "plato_favorito": prato_fav,
    "estrela": 1,
    "desconto_3_estrelas": 0, 
    "vindas":[
        {
          "data": data,
          "conta": conta,
        }
    ]
    }
    
    lista_cliente.append(dados)
    return lista_cliente[new_id-1]
    
def atualizar_prato_fav(id, prato_fav, lista_cliente):
    """Atualiza o prato favorito do cliente escolhido pelo id

    Args:
        id (int): id do cliente desejado
        prato_fav (str): O novo prato favorito do cliente
        lista_cliente (list): lista de todos os clientes da base de dados

    Returns:
        list: todos os dados do cliente escolhido
    """
    dados = lista_cliente[id-1]
    dados["plato_favorito"] = prato_fav
    return lista_cliente[id-1]

def Venda(id, data, conta, lista_cliente):
    """Atualiza a data base adicionando uma nova venda ao usuario escolhido pelo id, se o usuario tiver mais de 3 estrelas que são 3 visitas
    o mesmo terá um desconto fornecido pelo propio restaurante de 3%.

    Args:
        id (int): id do usuario
        data (str): data da compra do usuario
        conta (float): valor pago pelo usuario pela compra
        lista_cliente (list): lista de todos os clientes da base de dados

    Returns:
        list: todos os dados do cliente escolhido atualizado
    """
    
    dados =  lista_cliente[id-1]
    if  dados['estrela'] >= 3:
        desconto = conta
        conta -=0.03 * conta  
        dados['desconto_3_estrelas'] += round(desconto - conta, 4)
    dados['estrela'] += 1
    nova_vinda =       {
        "data": data,
        "conta": conta,
    }
    dados['vindas'].append(nova_vinda)
        
    return dados

def Delete_id(id, lista_cliente):
    """Deleta um usuario escolhido pelo usuario pelo id

    Args:
        id (int): id do usuario
        lista_cliente (list): lista de todos os clientes da base de dados

    Returns:
        list: lista de clientes atualizadas
    """
    lista_cliente.pop(id-1)
    new_id =0
    for cliente in lista_cliente:
        new_id  +=1
        cliente['id'] =  new_id

    return lista_cliente