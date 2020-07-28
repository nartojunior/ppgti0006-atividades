numeros = list()

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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

media = 0

for num in numeros:
    media += num
    pass

media /= 10

print("A media foi de: " + str(media))

acimaMedia = list()

for num in numeros:
    if num > media:
        acimaMedia.append(num)
    pass

print("Numeros acima da media")
print(acimaMedia)