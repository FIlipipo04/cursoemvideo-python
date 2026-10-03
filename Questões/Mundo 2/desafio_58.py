'''Melhore o programa 28. Só que agora o jogador vai tentar adivinhar ate acerta, mostrando no final o numero de tentativas.'''

import random

a = random.randint(0, 10)
e = int(input('O computador pensou em um digito, será que você é capaz de adivinhar qual é? Escolha um número de 0 a 10: '))
condicao = 0 #recebe 0 pq o jogador ainda não acertou o numero do bot
contador = 0
while condicao == 0:
    contador += 1
    if e > 10 or e < 0:
        e = int(input('Você adicionou um numero invalido, tente mais uma vez: '))
    elif a == e:
        print('Parabéns, você adivinhou o digito que o computador escolheu ')
        condicao = 1 #1 pq ele acertou
    elif e > a:
        e = int(input('Menos... Tente mais uma vez: '))
    elif e < a:
        e = int(input('Mais... Tente mais uma vez: '))
print(f'Você acetou em {contador} tentativs')
