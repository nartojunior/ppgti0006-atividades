class Turma:
    # Construtor
    def __init__(self):
        self.alunos = dict()
        self.size = 0
        pass
    pass

    # ToString
    def __str__(self):
        return str(self.alunos)

    def addAluno(self, nome, cpf):

        self.alunos[nome] = cpf
        self.size += 1
        pass

    def getCPF(self, nome):
        return self.alunos[nome]

    def count(self):
        return self.size

    def print(self):
        print("imprimindo alunos")
        print("nome - cpf")
        for nome in self.alunos:
            print( nome + " - " + str(self.alunos[nome]) )
            pass
        pass
    pass

print("Testando...")
minhaTurma = Turma()

minhaTurma.addAluno("narto", "123456")
print(minhaTurma.count())
minhaTurma.print()