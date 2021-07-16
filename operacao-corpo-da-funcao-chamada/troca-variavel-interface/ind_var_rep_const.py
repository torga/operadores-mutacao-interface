# Programa original
def my_function_f(a):
    i = a
    while i <= 5:
        i += 1
    print(i)

# Exemplo de mutante
def my_function_mutant_f(a):
# Este operador troca as variaveis de interface por constantes utilizadas na funcao 
    i = 5
    while i <= 5:
        i += 1
    print(i)
    
my_function_f(10)
my_function_mutant_f(10)