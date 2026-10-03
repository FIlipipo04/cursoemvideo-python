import time
e = 0
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
while e != 5:
    e = int(input('[1] soma\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa\n>>>Qual é a sua opção?'))
    if e == 1:
        print(f'A soma de {a} mais {b} é {a+b}')
    elif e == 2:
        print(f'A multiplicação de {a} e {b} é {a*b}')
    elif e == 3:
        if a > b:
            print(f'Entre os numeros {a} e {b} o maior é {a}')
        else:
            print(f'Entre os numeros {a} e {b} o maior é {b}')
    elif e == 4:
        print('Informe os numeros novamente:')
        a = int(input('Primeiro valor:'))
        b = int(input('Segundo valor:'))
    elif e == 5:
        print('Saindo do programa...')
    else:
        print('Informe uma opção valida')
    print('-_'*10)
    time.sleep(2)
print('Fim do programa, volte sempre!')