def idadeDaCamila(a, b, c): 
    idades = [a,b,c]
    idades.remove(min(idades))
    idades.remove(max(idades))
    if idades[0] <= 5 or idades[0] >= 100:
        print("Idade invalida! ")
    else:
        print("A idade da Camila é: {}".format(idades[0]))

idadeDaCamila(150,130,5)