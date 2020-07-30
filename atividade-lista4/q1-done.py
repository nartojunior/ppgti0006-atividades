string = "esse texto serve"

def vogaisEmTexto(texto):

    vogais = dict()

    for c in texto:
        if c in ["a", "e", "i", "o", "u"]:

            if c in vogais:
                vogais[c] += 1
                pass
            else:
                vogais[c] = 1
                pass
        pass

    print(vogais)
    pass

vogaisEmTexto(string)

