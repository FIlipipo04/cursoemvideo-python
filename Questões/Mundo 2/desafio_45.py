'''
crie um programa que faça o computador 
jogar jokenpo com você

usar random de lista 
pedra peedra empate
pedra tesoura ganha 
pedra folha perde
'''
import random

lista = ['Pedra', 'Papel', 'Tesoura']
m = random.choice(lista)

print('Este é jogo de jokenpô, selecione sua opção e tente ganhar da maquina')
p = int(input('[ 1 ] para Pedra\n[ 2 ] para Papel\n[ 3 ] para Tesoura\n\n'))

if (p == 1):
    p = 'Pedra'
elif (p == 2):
    p = 'Papel'
elif (p == 3):
    p = 'Tesoura'
else:
    print('Coloque uma opção valida!')

print('Máquina jogou:', m)
print('Você jogou:', p)

if (m == 'Pedra'):
    if (p == 'Pedra'):
        print('Empate!')
    elif (p == 'Papel'):
        print('Você ganhou!')
    else:
        print('Você perdeu 😭')

elif (m == 'Papel'):
    if (p == 'Pedra'):
        print('Você perdeu!')
    elif (p == 'Papel'):
        print('Empate!')
    else:
        print('Você ganhou!')

else:
    if (p == 'Pedra'):
        print('Você perdeu!')
    elif (p == 'Papel'):
        print('Você ganhou!')
    else:
        print('Empate!')