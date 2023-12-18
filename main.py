print("Bem vindo ao seu sistema Felps!")

print("Qual operação deseja realizar?")

print("Menu de Opções:")
print("1- Cadastrar cliente")
print("2- Cadastrar produto")
print("3- Ver lista de clientes")
print("4- Ver lista de produtos")
print("5. Sair")

escolha = int(input("Digite uma opção: "))

lista_clientes = []
lista_produtos = []

if escolha == 1:
    while True:
        id_cliente = int(input("Digite o código do cliente: "))
        nome_completo = str(input("Digite o nome da cliente: "))
        idade = input("Digite a idade da cliente: ")
        endereco = str(input("Digite o endereço da cliente: ") )
        telefone = input("Digite o telefone para contato: ")
        data_nasc = input("Qual a data de nascimento da cliente? Digite no formarto dd/mm/aaaa ")

        #dicionario para clientes
        clientes = {
            id_cliente: 'id_cliente',
            nome_completo: 'nome_completo',
            idade: 'idade',
            endereco: 'endereco',
            telefone: 'telefone',
            data_nasc: 'data_nasc'
        }
        lista_clientes.append(clientes)

        print ("Cliente cadastrado com sucesso!")
        novo_cliente = str(input("Deseja cadastrar um novo cliente?\nDigite 1 para sim \nDigite 2 para não\n"))
        if novo_cliente != '1':
            break
    print("Fim do cadastro de clientes.")
    for clientes in lista_clientes:
        print(clientes)
    
elif escolha == 2:
    while True:
        #inputs dos produtos
        cod_produto = int(input("Insira o código do produto: "))
        nome_produto = str(input("Digite o nome do produto: "))
        quantidade_produto = int(input("Digite a quantidade do produto a ser cadastrada: "))
        valor_compra = float(input("Qual o valor de custo do produto? "))
        valor_venda = float(input("Digite o valor de venda do produto: "))

        #dicionario para representar o produto
        produto = {
        'cod_produto': cod_produto,
        'nome_produto': nome_produto,
        'quantidade_produto': quantidade_produto,
        'valor_compra': valor_compra,
        'valor_venda': valor_venda
    }
        #adição do produto a lista_produtos
        lista_produtos.append(produto)

        print("Produto cadastrado com sucesso!")
        novo_produto =  input("Deseja cadastrar um novo produto?\nDigite 1 para sim\nDigite 2 para não.\n")
        if novo_produto != '1':
            break
    print("Fim do cadastro de produtos.")
    for produto in lista_produtos:
        print(produto)
        

    
elif escolha == 3:

    
    def exibir_lista_clientes(lista_clientes):
            print("\nLista de Clientes: ")
            print("ID | Nome | Endereço | Telefone | Data de Nascimento ")
            print("-" *30)

            for cliente in lista_clientes:
             print(f"{cliente['id_cliente']} | {cliente[ 'nome_cliente']} | {cliente[ 'endereco']} | {cliente[ 'telefone']}"  )

            print("-" * 30)

    exibir_lista_clientes(lista_clientes)

elif escolha == 4:

    def exibir_lista_produtos(lista_produtos):
        print("\nLista de Produtos:")
        print("Cód.Produto | NomeProduto | Qtd.Produto | Valor compra | Valor venda")
        print("-" * 30)
        
        for produto in lista_produtos:
            print(f"{produto['cod_produto']} | {produto['nome_produto']} | {produto['quantidade_produto']} | {produto['valor_compra']} | {produto['valor_venda']}")

        print("-" * 30)

    exibir_lista_produtos(lista_produtos)
