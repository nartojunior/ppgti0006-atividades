print("Q1")

nomes = list()
nomes.append("narto")
nomes.append("aurelio")
nomes.append("thomas")
nomes.append("diego")
nomes.append("bjorn")

print(nomes)

nomeD = input("Digite um nome\n")

if nomeD in nomes:
    print(nomeD + " está na lista")
else:
    print(nomeD + " não está na lista")
    pass
#input = str.le