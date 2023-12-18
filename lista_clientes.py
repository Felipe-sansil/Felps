clientes = [
    {'id_cliente': 1, 'nome_cliente': 'Ruth Gama', 'endereco': 'Rua cidade de Fagundes',
     'telefone': '(83)99114-6634','data_nascimento': '21/09/1999'}
]

def exibir_lista_clientes(lista_clientes):
    print("\nLista de Clientes: ")
    print("ID | Nome | Endereço | Telefone | Data de Nascimento ")
    print("-" *30)

    for cliente in lista_clientes:
        print(f"{cliente['id_cliente']} | {cliente[ 'nome_cliente']} | {cliente[ 'endereco']} | {cliente[ 'telefone']}"  )

        print("-" * 30)

exibir_lista_clientes(clientes)