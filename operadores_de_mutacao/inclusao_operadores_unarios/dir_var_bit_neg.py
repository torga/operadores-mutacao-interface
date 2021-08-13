from outro import *
import sys
sys.path.append(
    '/Users/torga/Desktop/operadores-mutacao-interface/operadores_de_mutacao/outros')


lista = []


def juntar_lista(i, lista_b):
    x = 10
    for item in range(i):
        lista = lista_b


# mutante


def juntar_lista(i, lista_b):
    x = 10
    for item in range(IF_MUTA(~i, i)):
        lista = lista_b


juntar_lista(1, [1, 2, 3])
