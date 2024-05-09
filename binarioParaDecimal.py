def binarioParaDecimal(n):
    binario = str(n)[::-1]
    decimal = 0
    index = 0 
    for bit in binario:
        decimal = decimal + ((2**index) * int(bit))
        index = index + 1
    print(decimal)
binarioParaDecimal(10)



def conversaoPreguicosa():
    while True: 
    n = int(input('Digite um número: '))
    print('- - - - '* 5)
    print('[1] Binário')
    print('[2] Octal')
    print('[3] Hexadecimal')
    print('[x] Sair')


    perguntanum = str(input('Digite a opção que deseja converter: '))
    if perguntanum == 'x'or perguntanum == 'X':
        break
    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3':
        if perguntanum == '1':
            rio = str(bin(n))
            print(rio)
        elif perguntanum == '2':
            cta = str(oct(n))
            print(cta)

        elif perguntanum == '3':
            exa = str(hex(n))
            print(exa)

    else:
        print('Opção invalida!')