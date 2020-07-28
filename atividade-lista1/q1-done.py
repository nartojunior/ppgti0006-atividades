## Gerador de tabuada.
canGenerateTabuada = False
#print("Tabuada de: ")
vInput = int(input("Tabuada de: "))

canGenerateTabuada = vInput >= 1 and vInput <= 10

while not canGenerateTabuada:
    print("Digite um valor de 1 a 10.")
    vInput = int(input("Tabuada de: "))
    canGenerateTabuada = vInput >= 1 and vInput <= 10
    pass

## Gerando tabuada

for i in range(10):
    print(str(vInput) + " x " + str((i+1)) + " = " + str(vInput*(i+1)))
    pass
