# programa principal
lista = [1,2,3,4,5,6,7,8,9,10]

def somar_numeros(i, lista):
    
    global j 
    j = 3
    
    for a in lista:
        i = i + lista[j]   

# mutante 1

def somar_numeros(i, lista):
    
    global j 
    j = 3
    
    for a in lista:
        i = i + IF_MUTA(a,lista[j]) 

