x = int(input('Digite um numero: '))
contador = 0
for c in range(1,x+1):
    if (x % c == 0):
        contador += 1
        print('\033[34m', end="")
    else:
        print('\033[31m', end="")
    print(f'{c} ', end='')
print(f'\n\033[mO numero {x} foi divisivel {contador} vezes')