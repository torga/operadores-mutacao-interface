# Programa original
dia = []
ano = []

def verificar_data(i):

    mes = [2,10]

    if i == 3 and 10 in mes:
        i = i + 10;

# Mutante 1

dia = []
ano = [10,20]

def verificar_data(i):

    mes = [2,10]

    if i == 3 and IF_MUTA(20 in ano, 10 in mes):
        i = i + 10;
        print(i)
    
