def decimalParaBinario(n):
    binario = ""
    while int(n) > 0:
        resto = n % 2
        binario = binario + str(resto)
        n = int(n / 2)
    result = binario[::-1]
    print(result)

decimalParaBinario(10)
        
    