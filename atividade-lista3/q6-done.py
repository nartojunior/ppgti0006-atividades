numeros = list()

test = [1, 2, 3, 4, 5, 6, 7, 8, 5, 10]

print("digite 10 numeros")

#"""
for i in range(10):
    numeros.append(int(input()))
    pass
print(numeros)
#"""

#para teste rapido.
#numeros = test
#print(numeros)

# verificando números 5.
for num in range(10):
    if numeros[num -1] == 5:
        numeros[num - 1] = "CINCO"
    pass

print(numeros)