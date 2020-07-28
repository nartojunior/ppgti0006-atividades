# Em busca do número perfeito!

def perfeito(a, b):
    perfeitos = list()

    for i in range(a, b+1):
        #print(i)
        divs = divisores(i)
        soma = 0
        for div in divs:
            soma += div
            pass

        if soma == i and i != 0:
            perfeitos.append(i)
            pass

        #print(divs)
        pass
    
    line = ""
    length = len(perfeitos)
    if (length > 0):
        for i in range(length):
            if (i < length - 1):
                line += str(perfeitos[i]) + ", " 
                pass
            else:
                line += str(perfeitos[i]) + "."
                pass
        pass
    else:
        line += "nenhum número encontrado..."

    print("Os números perfeitos no intervalo de " + str(a) +  " até "+ str(b) + " são: " + line)    
    pass

def divisores(num):
    tempList = list()
    #print("NUMERO: " + str(num))
    for i in range(num):        
        if num % (i+1) == 0 and i < num - 1:
            tempList.append(i+1)
            pass
        pass
    #print(tempList)
    return tempList

#poderia fazer um 
print("Vamos encontrar os números perfeitos!")
a = int(input("Digite o início do intervalo: "))
b = int(input("Digite o final do intervalo: "))
perfeito(a, b)

#perfeito(0, 30)
