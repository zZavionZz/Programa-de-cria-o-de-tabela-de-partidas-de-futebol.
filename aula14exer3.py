'''
    1 - tenho que obter valores de nomes de time, e colocar num vetor
    2 - fazer uma tabela com time vs outro time(não pode ser igual!)

'''
from os import system

def titulo():
    print('-' * 20)
    print(' CAMPEONATO FUTEBOL')
    print('-' * 20)

def nomes_de_times(lista):
    for i in range(1, 4):
        nome = input(f'o nome do {i}° time: ')
        lista.append(nome)
    return lista

def tabela(lista):
    largura_fixa = max([len(i) for i in lista]) + 3
    system('cls')
    print('---------------------\n'
          ' TABELA DE PARTIDAS  \n'
          '---------------------')
    for i in lista:
        for j in lista:
            if i != j:
                print(f'{i:{largura_fixa}} X {j:{largura_fixa}}')
            else:
                continue

lista = []
titulo()
lista = nomes_de_times(lista)
tabela(lista)