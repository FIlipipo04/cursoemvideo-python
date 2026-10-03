'''programa para ver se é par ou impar'''

num = int(input('Digite um numero:'))

if num <= 0:
    print('Valor invalido.')
elif num > 0:
    if (num%2 == 1 ):
        print('O seu numero é ímpar.')
    elif (num%2 == 0 ):
        print('O seu número é par.')
    