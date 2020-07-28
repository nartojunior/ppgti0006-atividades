alunos = dict()

def resultadoFinal(nota):

    if nota >= 5.0:
        return "Aprovado"
    else:
        return "Reprovado"
    pass

print("Registrando notas:")

#"""
alunos = { "João": 8.0, "Maria": 5.5, "José": 4.5, "Narto": 10.0 }
#"""

"""
for i in range(3):

    nome = input("Digite o Nome do aluno: ")
    nota = int( input("Digite a nota de " + nome + ", por favor: ") )

    alunos[nome] = nota


    pass
"""

for key in sorted(alunos):
    line = key + ", nota " + str(float(alunos[key])) + ", " + resultadoFinal(alunos[key])
    print(line)
    pass
