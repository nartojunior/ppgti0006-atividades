n = int(input("Digite o numero \'n\' da familia: "))

for i in range(n):

    factorX = i + 1
    line = ""

    for f in range(i+1):
        line = line + " " + str(factorX * (f + 1))        
        pass

    print(line)
    pass