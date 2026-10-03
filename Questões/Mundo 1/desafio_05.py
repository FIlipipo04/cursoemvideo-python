'''fazer programa que mostre o sucessor e anterior de um numero'''

print('Olá!!! vamos ver o sucessor e o antecessor de um numero?', end= ' ')
b = int(input ('Escreva o numero que quiser:'))

print('Você escolheu o numero {}, o seu sucessor é {} e o seu antecessor é {}.' .format(b, b+1, b-1))