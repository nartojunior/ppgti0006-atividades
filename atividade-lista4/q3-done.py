### AGENDA
import os

class Agenda:
    # Construtor
    def __init__(self):
        self.contatos = dict()
        self.size = 0

        pass
    pass

    # ToString
    def __str__(self):
        return str(self.contatos)

    def addContato(self, nome, numero):

        if nome in self.contatos:
            self.contatos[nome].append(numero)
            pass
        else:
            initList = list()
            initList.append(numero)
            self.contatos[nome] = initList
            pass

        self.size += 1
        pass

    def count(self):
        return self.size
    pass


novaAgenda = Agenda()

"""
novaAgenda.AddContato("narto", "123456")
novaAgenda.AddContato("narto", "654321")
novaAgenda.AddContato("narto", "024680")
novaAgenda.AddContato("junior", "654321")
novaAgenda.AddContato("junior", "024680")
"""

#print(novaAgenda)

canExit = False
canPrintAgenda = False

os.system("cls")

while not canExit:
    print()
    print("AGENDA")
    print("1 - Adicionar contato.")
    print("2 - Listar contatos.")
    print("Qualquer outro valor para sair.")

    

    if canPrintAgenda:
        print()
        print("Imprimindo Contatos")

        if novaAgenda.count() > 0:
            print(novaAgenda)
            pass
        else:
            print("Nao há contatos registrados.")
            pass
        canPrintAgenda = False
        pass

    print()
    op = int(input("Digite sua opção: "))

    if op == 1:
        os.system("cls")
        print()
        print("Adicionando contato")
        nome = input("Digite o nome do contato: ")
        numero = input("Digite um numero: ")
        novaAgenda.addContato(nome, numero)
        
        pass
    elif op == 2:
        canPrintAgenda = True
        pass
    else:
        canExit = True

    os.system("cls")
    
    pass

