lista_alunos = [
    {
        'id': 1,
        'nome': 'André'
    },
    {
        'id':2,
        'nome': 'Renato'
    },
]
def post(id: int, nome: str) -> dict:
    pessoa = {'id': id, 'nome': nome}
    return pessoa


id = 3
escolha = 100
while escolha != 0:
    #CRUD
    escolha = int(input("bem vindo ao sistema \n adicionar nova pessoa -1 \n ler -2 \n atualizar um aluno -3 \n deletar um aluno do sistema-4\n Sair-0 \n"))

    if escolha == 1:
            #Post
            #Criar uma função que coloca a aluna Joana na lista
        nome = input("qual o nome do aluno")
        print(post(id, nome))
        lista_alunos.append(post(id, nome))
        id +=1
    elif escolha ==2:
            #read/get
            #criar uma função que leia
        decisao = int(input("Deseja ver todos os alunos (1) \n Ou somente um aluno(2)"))
        if decisao == 1:
            print(lista_alunos)
        elif decisao ==2:
            ler_id = int(input("qual o id do aluno que voçê deseja ler?"))
            print(lista_alunos[ler_id -1 ])
    elif escolha ==3:
            #Update
        id = int(input("qual o id do aluno? "))
        new_name = input("qual será o novo nome do aluno? ")   
        lista_alunos[id-1] = {'id': id, 'nome': new_name}
    elif escolha == 4: 
            #delete
        id_delete = int(input("qual o id do aluno que será deletado?"))
        id_delete -=1
        lista_alunos.pop(id_delete)
                
    else : 
        print("escolha invalida")









