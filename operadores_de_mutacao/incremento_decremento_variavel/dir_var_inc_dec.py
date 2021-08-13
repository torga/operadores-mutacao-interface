
# programa


def verificar_numero(i, y):
    x = 10
    if(y == 10):
        y = 1000

# mutante incremento


def verificar_numero(i, y):
    x = 10
    if(y == x):
        IF_MUTA(DEVOLVE_VAR(y=+10), y=1000)

# mutante decremento


def verificar_numero(i, y):
    x = 10
    if(y == x):
        IF_MUTA(DEVOLVE_VAR(y=+10), y=1000)


verificar_numero(1, 10)
