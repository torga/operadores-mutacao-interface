# programa
def aumentarVetor(lista):
    item = 1
    for item in range(len(lista)):
        lista.append(100)

# mutante


def aumentarVetor(lista):
    item = 1
    for item in range(len(lista)):
        IF_MUTA(lista.append(5), lista.append(100))


# teste
lista = [1, 3, 4, 5]
aumentarVetor(lista)

print(lista)

# saída
# [1, 3, 4, 5, 100, 100, 100, 100] programa
# [1, 3, 4, 5, 1, 100, 1, 100, 1, 100, 1, 100] mutação
# erro de keyword argument repeated linha 11
