from Cliente import Cliente
from Filme import Filme

class Locadora:
    def __init__(self):
        self.estoque_filmes = []
        self.lista_clientes = []
        self.filmes_alugados = []

    def adicionar_filme(self, filme):
        self.estoque_filmes.append(filme)
        print(f"Filme '{filme.titulo}' adicionado!.")

    def adicionar_cliente(self, cliente):
        self.lista_clientes.append(cliente)
        print(f"Cliente '{cliente.nome}' adicionado!")

    def alugar_filme(self, titulo, id_cliente):
        for f in self.estoque_filmes:
            if f.titulo == titulo and f.disponibilidade:
                filme = f
                break
        else:
            print("Filme não disponível ou não encontrado")
            return
        
        for c in self.lista_clientes:
            if c.id_cliente == id_cliente:
                cliente = c
                break
        else:
            print("Cliente não cadastrado")
            return
        
        filme.disponibilidade = False
        self.filmes_alugados.append(filme)
        print(f"Filme '{filme.titulo}' alugado por '{cliente.nome}'")

    def listar_filmes_disponiveis(self):
        filmes_disponiveis = []

        for f in self.estoque_filmes:
            if f.disponibilidade:
                filmes_disponiveis.append(f)

        if filmes_disponiveis:
            print("Filmes disponíveis:")
            for filme in filmes_disponiveis:
                print(f"Título '{filme.titulo}'")
        else:
            print("Nenhum filme disponível")

    def listar_filmes_alugados(self):
        filmes_alugados = []

        for f in self.estoque_filmes:
            if f.disponibilidade == False:
                filmes_alugados.append(f)
        if filmes_alugados:
            print("Filmes alugados:")
            for filme in filmes_alugados:
                print(f"Título '{filme.titulo}'")
        else:
            print("Nenhum filme alugado")

    def listar_clientes(self):
        clientes_cadastrados = []

        for f in self.lista_clientes:
                clientes_cadastrados.append(f)
        if clientes_cadastrados:
            print("Clientes cadastrados:")
            for cliente in clientes_cadastrados:
                print(f"Nome '{cliente.nome}'")
        else:
            print("Nenhum cliente cadastrado")