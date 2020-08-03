"""
Desenvolva um sistema de banco em python. Você deve exibir 6 menus:

Criar nova conta. Uma nova conta deve conter ID, NOME e SALDO
Adicionar dinheiro a conta. Adiciona uma quantia (dita pelo usuário) a conta de um ID especifico, mostra quando ficou o saldo final.
Remover dinheiro da conta. Remove uma quantia (dita pelo usuário) a conta de um ID especifico, mostra quanto ficou o saldo final. Emitir um alerta caso o saldo tenha ficado negativo.
Mostrar saldo de um nome dado
Apagar uma conta (apaga todos os dados de um determinado ID)
Apagar todas as contas
ps: lembre-se de tratar exceções, caso o menu selecionado, ID ou nome sugerido não exista imprimir uma alerta avisando que não existe.
"""
import os
import time

class Banco:
    def __init__(self):
        self.idCounter = 1
        self.ids = list()
        self.contas = dict()

        pass

    def criarConta(self, nome, saldo=float):
        
        self.ids.append(self.idCounter)
        self.contas[self.idCounter] = [nome, saldo]        

        print("Nova conta criada!")
        print("ID: " + str(self.idCounter) + ", NOME: " + nome + ", SALDO: $" + str(saldo) + ".")

        self.idCounter += 1
        pass

    def adicionarSaldo(self, id, valor=float):
        if id not in self.ids:
            print("ID [" + str(id) + "] não existe...")
            pass
        else:
            self.contas[id][1] += valor
            print("ID: " + str(id) + ", NOME: " + self.contas[id][0] + ", SALDO: $" + str(self.contas[id][1]) + ".")
            pass

    def removerSaldo(self, id, valor=float):
        if id not in self.ids:
            print("ID [" + str(id) + "] não existe...")
            pass
        else:
            self.contas[id][1] -= valor
            print("ID: " + str(id) + ", NOME: " + self.contas[id][0] + ", SALDO: $" + str(self.contas[id][1]) + ".")

            if self.contas[id][1] < 0:
                print("ESTA CONTA ESTÁ COM SALDO NEGATIVO!")
            pass

        pass

    def mostrarSaldo(self, nome):

        temNome = False

        for key, value in self.contas.items():
            if value[0] == nome:
                #print(nome)
                print("ID: " + str(key) + ", NOME: " + value[0] + ", SALDO: $" + str(value[1]) + ".")
                temNome = True
                pass
        
        if not temNome:
            print("Nome [" + nome + "] não existe...")
            pass

        pass

    def apagarConta(self, cId=int):
        if cId not in self.ids:
            print("ID [" + str(id) + "] não existe...")
            pass
        else:
            #print(self.ids)
            #print(self.contas)
             
            print("ID: " + str(cId) + ", NOME: " + self.contas[cId][0] + ", SALDO: $" + str(self.contas[cId][1]) + ".")
            del self.contas[cId]
            self.ids.remove(cId)
            print("Conta Removida")           

            #print(self.ids)
            #print(self.contas)
            pass
        pass

    def apagarTodasAsContas(self):
        
        #print(self.ids)
        #print(self.contas)

        self.ids.clear()
        self.contas.clear()

        #print(self.ids)
        #print(self.contas)
        pass

    def Mockup(self):
        self.criarConta("narto", 2000.0)
        self.criarConta("marcel", 2000.0)
        pass

    pass

def StartBanco():

    meuBanco = Banco()
    timeToSleep = 3
    meuBanco.Mockup()
    canExit = False
    ##canPrintAgenda = False

    os.system("cls")

    
    while not canExit:
        print("Bem vindo ao Banco N.")

        print("1 - Criar nova Conta.")
        print("2 - Adicionar dinheiro na Conta.")
        print("3 - Remover dinheiro na Conta.")
        print("4 - Mostrar Saldo")
        print("5 - Apagar Conta")
        print("6 - Apagar todas as Contas.")
        print("Qualquer outro valor para sair.")
    
        """
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
        """

        print()
        op = int(input("Escolha uma das opções acima: "))

        if op == 1:
            #os.system("cls")
            print()
            print("Criando nova conta")
            nome = input("Digite o nome do cliente: ")
            saldo = float(input("Digite o saldo inicial: "))
            meuBanco.criarConta(nome, saldo)
            
            pass
        elif op == 2:            
            print()
            print("Adicionando saldo em conta.")
            cId = int(input("Digite o ID do cliente: "))
            saldo = float(input("Digite o saldo a acrescentar: "))
            meuBanco.adicionarSaldo(cId, saldo)
            #canPrintAgenda = True
            pass
        elif op == 3:
            print()
            print("Removendo saldo em conta.")
            cId = int(input("Digite o ID do cliente: "))
            saldo = float(input("Digite o saldo a diminuir: "))
            meuBanco.removerSaldo(cId, saldo)
            pass
        elif op == 4:
            print()
            print("Mostrando Saldo.")
            nome = input("Digite o Nome do cliente: ")
            meuBanco.mostrarSaldo(nome)
            pass
        elif op == 5:
            print()
            print("Apagando Conta.")
            ciD = int(input("Digite o id da conta: "))
            meuBanco.apagarConta(ciD)
            pass
        elif op == 6:
            print()
            print("Apagando todas as contas.")
            meuBanco.apagarTodasAsContas()
            pass
        else:
            print("A OPÇÃO DIGITADA NÃO EXISTE. FECHANDO O SISTEMA EM " + str(timeToSleep) + " segundos...")
            canExit = True
            break

        time.sleep(timeToSleep)
        os.system("cls")
        pass

    pass

StartBanco()