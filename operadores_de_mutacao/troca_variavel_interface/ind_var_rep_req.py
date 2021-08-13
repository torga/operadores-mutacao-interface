# PROGRAMA ORIGINAL

import sys


def contar(i):

    x, y = 0

    for (x == 1) in range(i):

        y = i + 100


# MUTANT

max = sys.maxsize


def contar(i):

    x, y = 0

    for (x == 1) in range(i):

        IF_MUTA(y=max + 30, y=i + 30)


# MUTANTE 3
def merge(i, vet):
    x = 0
# ALTERAR FOR PARA for(x=1; 0 <=i; x++)
    for (x == 1) in range(i):
        vet[x] = 100

# MUTANTE 4


def merge(i, vet):
    x = 0
    for (x == 1)in range(i):
        vet[x] = 100

# MUTANTE 5


def merge(i, vet):
    x = 0
# for(x=1; IF_MUTA(-1<=i, x<=i) ;x++)
    for (x == 1)in range(i):
        vet[x] = 100
