# Programa original
def contar_valor(i):

    x = y = z = 0

    for x in range(i):

        y = y + 30
        z = z / y

    return z


# Mutante 1
def contador_mutant(i):
    x = y = z = 0

    for x in range(IF_MUTA(x,i)):
        y = y + 30
        z = z / y 
        print(z)

    return z

# Mutante 2
def contador_mutant(i):
    x = y = z = 0

    for x in range(IF_MUTA(x,i)):
        y = y + 30
        z = z / y 
#        print(z)

    return z

# Mutante 3
def contador_mutant(i):
    x = y = z = 0

    for x in range(z):
        y = y + 30
        z = z / y 
#        print(z)

    return z
