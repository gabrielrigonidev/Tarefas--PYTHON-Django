agenda = {}
def criarContato():
    nome = input("Digite seu Nome: ")
    telefone = input("Digite seu Tel: ")
    agenda[nome] = telefone
def exibirContatos():
    for n,t in agenda.items():
        print(f'\nNome: {n}')
        print(f'Telefone: {t}') 
def buscarContato():
    nomeBusca = input("Procurar seu contatinho: ")
    if nomeBusca in agenda:
        print("Contato encontrado: " + nomeBusca)
    else:
        print("Contato não encontrado")
        
while True:
    print("Bem vindo a Agenda DSM: ")
    print("1 - Criar contato")
    print("2 - Exibir contatos")
    print("3 - Buscar contato")
    print("4 - Sair")
    print('------------------------')
    opcao = input("Digite uma opção: ")
    if opcao == '1':
        criarContato()
        print('------------------------')
    elif opcao == '2':
        exibirContatos()
        print('------------------------')
    elif opcao == '3':
        buscarContato()
        print('------------------------')
    elif opcao == '4':
        print('Tchau')
        break;