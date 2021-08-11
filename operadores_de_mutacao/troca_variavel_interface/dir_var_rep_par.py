__flg = False

def PREPARE_MUTA(x):
    _flg = True
    return x
    

def IF_MUTA(x,y):
    if __flg: return x 
    return y

'''
# Programa Original
a = 0

def merge(i, vet):

    for x in range(i):
        a += vet[x]

    return a
'''
# Mutante 1

a = 0

def merge(i, vet):

    for x in range(i):

        IF_MUTA(a = a + i, a = a + vet[x])

        return a

merge(1,3)

'''
# Mutante 2
def merge(i, vet):
    x = 0
    for (x == 1) in range(i):
        vet[x] = 100

# Mutante 3
def merge(i, vet):
    x = 0
    for (x == 1) in range(i):
        vet[i] = 100

# Mutante 4
def merge(i, vet):
    x = 0
#    for (*vet = 1) in range(i):
#       vet[x] = 100

# Mutante 5
def merge(i, vet):
    x = 0
# olhar na linguagem
#   for *vet in range(i):
#       vet[x] = 100

# Mutante 6

def merge(i, vet):
    x = 0
    for (x == 1) in range(i):
#       vet[*vet] = 100


   '''