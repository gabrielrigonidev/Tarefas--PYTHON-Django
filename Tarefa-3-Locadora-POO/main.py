from Locadora import Locadora
from Filme import Filme
from Cliente import Cliente

locadora = Locadora()
while True:
    print("--------------------------------")
    print("\nLocadora Fatec - MENU:")
    print("1. Adicionar filme")
    print("2. Adicionar cliente")
    print("3. Alugar filme")
    print("4. Listar filmes disponíveis")
    print("5. Listar filmes alugados")
    print("6. Listar clientes")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("--------------------------------")
        titulo = input("Título do filme: ")
        ano = input("Ano de lançamento: ")
        genero = input("Gênero: ")
        filme = Filme(titulo, ano, genero)
        locadora.adicionar_filme(filme)

    elif opcao == '2':
        print("--------------------------------")
        id_cliente = input("ID do cliente: ")
        nome = input("Nome do cliente: ")
        cliente = Cliente(id_cliente, nome)
        locadora.adicionar_cliente(cliente)

    elif opcao == '3':
        print("--------------------------------")
        titulo_filme = input("Título do filme: ")
        id_cliente = input("ID do cliente: ")
        locadora.alugar_filme(titulo_filme, id_cliente)

    elif opcao == '4':
        print("--------------------------------")
        locadora.listar_filmes_disponiveis()

    elif opcao == '5':
        print("--------------------------------")
        locadora.listar_filmes_alugados()

    elif opcao == '6':
        print("--------------------------------")
        locadora.listar_clientes()

    elif opcao == '7':
        print("Saiu")
        break

    else:
        print("Opção inválida. Tente novamente.")