from abc import ABC, abstractmethod
import random

def jogar_dados(jogadas):
    atributo = 0
    for i in range(jogadas):
        atributo += random.randint(1, 6)
    return atributo

def lista_atributos():
    atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    return atributos

def mostra_nomes_atributos(lista, atributos):
    for i, (nome, valor) in enumerate(zip(lista, atributos), start=1):
        print(f"{i}.{nome}: {'Vazio' if valor is None else valor}")

def escolher_atributos(visualizar_valores, atributos, usados):
    lista = lista_atributos()
    for i in range(6):
        print("Você tem os seguintes valores:\n", *visualizar_valores)
        mostra_nomes_atributos(lista, atributos)
        while True:
            m = int(input(f"Para qual atributo vai o valor {visualizar_valores[i]}:\n")) - 1
            if m not in (usados):
                usados.append(m)
                break
            else:
                print("Escolha um novo atributo!")
        atributos[m] = visualizar_valores[i]
        visualizar_valores[i] = 0
    return atributos
