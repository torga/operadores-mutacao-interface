import time
from outro import *
import sys

sys.path.append(
    '/Users/torga/Desktop/operadores-mutacao-interface/operadores_de_mutacao/outros')


# programa

lista = []


def juntar_lista(i, lista_b):
    x = 10
    for item in range(i):
        lista = lista_b


# mutante


def juntar_lista(i, lista_b):
    x = 10
    for item in range(IF_MUTA(-i, i)):
        lista = lista_b


def juntar_lista(a, b):
    return a+b


inicio = time.time()
if juntar_lista(1, 2) == 3:
    print(True)
fim = time.time()
print(fim - inicio)
