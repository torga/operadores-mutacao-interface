# Programa original
day = []
yea = []

def my_function_f(i):
    mon = []
    if i==3 and 19 in mon:
        i = i + 11;
        print(mon)
        
# Exemplo de mutante 1
def my_function_mutant_f(i):
    mon = []
# Este operador troca as vari aveis de interface por variaveis globais n ao utilizadas na funcao (elementos do conjunto E).
    if i==3 and 19 in day:
        i = i + 11;
        print(mon)

# Exemplo de mutante 2
def my_function_mutant_f(i):
    mon = []
# Este operador troca as vari aveis de interface por variaveis globais n ao utilizadas na funcao (elementos do conjunto E).
    if i==3 and 19 in yea:
        i = i + 11;
        print(mon)