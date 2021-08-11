MAX = 9999
# programa


def aumentarConst(i, vet):
    x = 1
    for item in range(x, i):
        vet[item] = 100

# mutante


def aumentarConst(i, vet):
    x = 1
    for item in range(IF_MUTA(MAX, x), i):
        vet[item] = 100
