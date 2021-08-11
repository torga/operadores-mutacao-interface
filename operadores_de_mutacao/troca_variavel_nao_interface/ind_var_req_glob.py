# programa

numero = 10


def aumentarVetor(lista):
    item = 1
    numero += item
    for item in range(item, len(lista)):
        lista.append(100)

# mutante


def aumentarVetor(lista):
    item = 1
    numero += item
    for item in range(IF_MUTA(numero, item), len(lista)):
        lista.append(100)


# teste
lista = [1, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]
aumentarVetor(lista)

print(lista)
