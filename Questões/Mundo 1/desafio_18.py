'''Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse angulo.
'''
import math 
angulo = float(input('Digite um ângulo qualquer: '))    
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {:.2f} tem seno de {:.3f}\ncosseno de {:.3f} e tangente de {:.3f}.'.format(angulo,seno, cosseno, tangente))