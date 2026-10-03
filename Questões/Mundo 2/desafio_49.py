'''Refaça o dasafio 009, mostrando a tabuada de um numero que o usuario
escolher, so que agora utilizando um laço for'''

x = int(input('Escolha um numero: '))
print('-----------------')
for c in range(1, 11):
    print(f'{x:2} X {c:2} = {x*c:2}')
print('-----------------')