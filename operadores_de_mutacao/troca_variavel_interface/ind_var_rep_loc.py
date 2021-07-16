# Programa original
def contador(i):
    x = y = z = 0

    for x in range(i):
        y = y + 30
        z = z / y 
#        print(z)

    return z

# contador(5)

# Mutante 1
def contador_mutant(i):
    x = y = z = 0

    for x in range(x):
        y = y + 30
        z = z / y 
#        print(z)

    return z

# Mutante 2
def contador_mutant(i):
    x = y = z = 0

    for x in range(y):
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


        