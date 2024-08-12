import random

def listaRandom():
    return random.sample(range(1, 100), 5)

listaNumeros = listaRandom()
# print(f"Lista: {listaNumeros}")

while True:
    escolha = input("Digite um número ou digite 'Desistir' para sair: ")

    if escolha.lower() == 'desistir':
        print("Você desistiu.")
        break
    numero = int(escolha)

    if numero in listaNumeros:
        print("Número encontrado!")
        break
    else:
        perto = False
        for n in listaNumeros:
            if abs(numero - n) <= 5:
                perto = True
                break

        if perto:
            print("Você está perto de um dos números da lista. Tente denovo.")
        else:
            print("Número não encontrado. Tente denovo.")