import random
import os
controle = "s"

while controle == "s":
    dados = []
    cont = 0
    resultado = 0
    os.system('cls')
    ndados = int(input("Digite quantos dados você deseja jogar: "))
    lados = int(input("Digite o número de lados do dado: "))

    while cont < ndados:
        dados.append(random.randrange(1,(lados + 1)))
        cont+=1
    cont = 1

    for x in dados:
        print("{}° dado -> {}" .format(cont, x))
        cont+=1
        resultado += x

    print("A soma de todos os dados foi ->", resultado)
    controle = input("Deseja jogar outra vez? [s ou n] ")
os.system('cls'); print("Finalizando...")