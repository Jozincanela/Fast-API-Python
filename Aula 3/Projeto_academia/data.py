'''
get todos clientes sem os dados/keys: peso, altura e as avaliações (For e HOF)
get cliente todas avaliações
get cliente última avaliação
post: com primeira avaliação (nome, peso, altura, data)
update: mudando peso, coloca nova avaliação no []
delete: simples
'''


lista_clientes = [
    {
        'id': 1,
        'nome': 'Renato',
        'altura': 1.75,
        'peso': 85.5,
        'avaliações': [
            {
                'data': '01/07/2023',
                'imc': 28.5,
                'classificação': 'sobrepeso'
            },
        ]
    },
    {
        'id': 2,
        'nome': 'André',
        'altura': 1.66,
        'peso': 90.5,
        'avaliações': [
            {
                'data': 'teste',
                'imc': 28.5,
                'classificação': 'teste'
            },
            {
                'data': 'final',
                'imc': 28.5,
                'classificação': 'final'
            },
        ]
    },
]


# Exemplo de uso da função
nome = 'teste'
peso = 85.5
altura = 1.75
data = '08/07/2023'
