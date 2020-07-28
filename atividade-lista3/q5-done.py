meses = list()

meses.append("janeiro")
meses.append("fevereiro")
meses.append("marco")
meses.append("abril")
meses.append("maio")
meses.append("junho")
meses.append("julho")
meses.append("agosto")
meses.append("setembro")
meses.append("outubro")
meses.append("novembro")
meses.append("dezembro")

mesInput = input("Digite um mês de 1 a 12\n")
# considerando que seja digitado um valor válido.

print(mesInput + " é " + meses[int(mesInput) - 1])