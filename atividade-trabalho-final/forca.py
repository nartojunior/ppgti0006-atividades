import os
import random


#agora = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#elemento = random.choice(agora)
#print(elemento)

print("ola")

def StartGameForca(palavras=list()):

    size = len(palavras)

    if size < 1:
        print("É preciso uma lista de palavras.")
        return
        

    palavra = random.choice(palavras)

    tentativas = 6
    
    letrasDescobertas = list()

    while tentativas > 0:
        letra = input("Digite uma letra: ")

        if letra in palavra:

            if letra not in letrasDescobertas:
                letrasDescobertas.append(letra)
                pass

            #print(letrasDescobertas)
            mascara = ""

            acertos = 0
            for i in range( len(palavra) ):
                if palavra[i] in letrasDescobertas:
                    mascara += str(palavra[i]) + " "
                    acertos+=1
                    pass
                else:
                    mascara += "_ "
                    pass
                pass

            print(mascara)

            if acertos == len(palavra):
                print("Parabens!")
                break
            
            pass
        else:
            tentativas -= 1
            print("Você errou pela " + str( 6 - tentativas ) + "ª vez. Tente de novo!")
            if tentativas == 0:
                print("Enforcado! A palavra secreta é: " + palavra)
                pass
            pass
        pass

    print
    pass
    #

#StartGameForca(["mamao", "acucar"])