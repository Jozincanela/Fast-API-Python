#Quando o cliente chegar a 3 estrelas ele tem direito a 3% de desconto na conta
#get conta (id, data, valor da conta) => retorna valor da conta, c//s desconta e números de estrelas
#valor da conta com desconto 3 estrelas, quando Já tem 3 estrelas/ou não
lista_clientes = [
  {
    "id": 1,
    "nombre": "Pedro",
    "plato_favorito": 'arepa',
    "estrela": 1,
    "desconto_3_estrelas": 0, 
    "vindas":[
        {
          "data": "01/02/2023",
          "conta": 40,
        }
    ]
  },
  {
    "id": 2,
    "nombre": "Maria",
    "plato_favorito": 'tacos',
    "estrela": 2,
    "desconto_3_estrelas": 0,
    "vindas":[
      {
        "data": "01/02/2023",
        "conta": 40,
      },
      {
        "data": "07/02/2023",
        "conta": 100,
      }
    ]
  }
]