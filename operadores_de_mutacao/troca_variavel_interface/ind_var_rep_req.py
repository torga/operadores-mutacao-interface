# PROGRAMA ORIGINAL
import sys

def merge(i,vet):
    x = 0
    for (x == 1) in range(i):
        vet[x] = 100

# MUTANTE 1
#int merge(int i; int vet[]) {
#int x;
#for(x=1; IF_MUTA(MAXINT<=i, x<=i) ;x++)
#vet[x] = 100;
#}

# MUTANTE 2
#int merge(int i; int vet[]) {
#int x;
#for(x=1; IF_MUTA(MININT<=i, x<=i) ;x++)
#vet[x] = 100;
#}

# MUTANTE 3
def merge(i,vet):
    x = 0
# ALTERAR FOR PARA for(x=1; 0 <=i; x++)
    for (x == 1) in range(i):
        vet[x] = 100

# MUTANTE 4
def merge(i,vet):
    x = 0
    for (x == 1)in range(i):
        vet[x] = 100

# MUTANTE 5
def merge(i,vet):
    x = 0
# for(x=1; IF_MUTA(-1<=i, x<=i) ;x++)
    for (x == 1)in range(i):
        vet[x] = 100

    