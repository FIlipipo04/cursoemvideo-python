'''escreva um programa qur faça o coputador pensar em um numero entre 0 e 5 e peça para p usuário tentar descobrir qual foi o numero escolhido pelo computador o programa deverá escrever se o usuario venceu ou perdeu '''

import random

a = random.randint(0, 5)
e = int(input('O computador pensou em um digito, será que você é capaz de adivinhar qual é? Escolha um número de 0 a 5'))

if e > 5:
    print('O valor digitado é invalido.')

elif a == e:
    print('Parabéns, você adivinhou o digito que o computador escolheu ')

else:
    print('Poxa, você não acertou, tente mais uma vez.')    
