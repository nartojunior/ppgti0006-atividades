numeros = list()

numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)

def pares(lista):
    nPares = 0

    for num in lista:
        if num % 2 == 0:
            nPares +=1
        
    return nPares

def impares(lista):
    nImpares = 0

    for num in lista:
        if num % 2 != 0:
            nImpares +=1

    return nImpares

print("a lista tem " + str(pares(numeros)) + " numeros pares e " + str(impares(numeros)) + " numeros impares")
