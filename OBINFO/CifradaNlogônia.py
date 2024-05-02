alfabeto = "abcdefghijklmnopqrstuvxz"
vogaisProximas = "aaaeeeeiiiiioooooouuuuuu"
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvxzz"

palavra = input("Digite uma palavra para ser cifrada: ")
cifra = ""
for letra in palavra: 
    if not (letra in vogais): 
        # Consoante inicial permanece 
        cifra = cifra + letra
        # Consoante vira vogal proxima 
        posicaoAlfabeto = alfabeto.find(letra)
        cifra = cifra + vogaisProximas[posicaoAlfabeto]
        # Consoante vira cosoante seguinte
        posicaoConsoante = consoantes.find(letra) + 1
        cifra = cifra + consoantes[posicaoConsoante]
    else: 
        cifra = cifra + letra
    print(cifra)