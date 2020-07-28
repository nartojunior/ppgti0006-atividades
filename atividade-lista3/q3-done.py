nomes = list()
nomes.append("narto")
nomes.append("aurelio")
nomes.append("thomas")
nomes.append("diego")
nomes.append("bjorn")

print(nomes)

nomeD = input("Digite um nome\n")

if nomeD in nomes:
    nomes.remove(nomeD)


print(nomes)