# PROGRAMA ORIGINAL
'''
num_aleatorio = 10 #VARIAVEL GLOBAL

def correr_numero(a): #VARIAVEL DE INTERFACE
    numero = a #VARIAVEL LOCAL RECEBENDO VARIAVEL DE INTERFACE
    for numero in range(a,num_aleatorio,2): #TEMOS CONSTANTES UTILIZADAS NA FUNCAO
        print(retornar_numero(a)) #COMUNICACAO COM OUTRA FUNCAO

def retornar_numero(a):
    return a+1

correr_numero(0)
'''
__flg = False


def PREPARE_MUTA(x):
    _flg = True
    return x


def IF_MUTA(x, y):
    if __flg:
        return x
    return y


# MUTANTE 1
num_aleatorio = 10  # VARIAVEL GLOBAL


def correr_numero(a):

    numero = 0

    for numero in range(IF_MUTA(numero, a), num_aleatorio, 2):
        retornar_numero(numero)


def retornar_numero(a):
    return a+1

# PROGRAMA


num_aleatorio = 10


def correr_numero(a):

    numero = 0

    for numero in range(a, num_aleatorio, 2):
        retornar_numero(numero)


def retornar_numero(a):
    return a+1
