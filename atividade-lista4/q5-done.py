def imprimePorIdade(pDIct = dict()):
    
    sortedDict = sorted(pDIct.items(), key = lambda x: x[1], reverse=False)

    for i in sortedDict:
        print(i[0], i[1])
        pass

    pass

testDict = { "narto": 29, "leo": 13, "antonia": 45, "mimosa": 27, }

imprimePorIdade(testDict)