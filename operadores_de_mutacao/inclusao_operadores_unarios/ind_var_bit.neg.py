from outro import *
import sys
sys.path.append(
    '/Users/torga/Desktop/operadores-mutacao-interface/operadores_de_mutacao/outros')


lista = []


def juntar_lista(i, lista_b):
    x = 10
    for item in range(x):
        lista = lista_b


# mutante


def juntar_lista(i, lista_b):
    x = 10
    for item in range(IF_MUTA(~x, x)):
        lista = lista_b
