# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 011 — Pintando parede
#
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
# uma área de 2m².
# === FIM DO ENUNCIADO ===

'''
fazer programa que calcule a area de uma parede. saiba que vamso pintar a parede
, cada 2m² da pared eprecisam de 1litro]
'''
print('Olá Sr(a) pintor(a)!\nEste programa serve para lhe auxuliar a calcular a área de uma parede\ne saber quantos litros de tinta são necessarios para pintar 1m²\nsabendo que 1l de tinta pinta 2m²')

L = float(input('Para começarmos, me informe qual é o comprimento em metros da sua parede:'))
C = float(input('Agora me informe a altura da sua parede tambem em metros:'))

A = L * C

T = A / 2

print('Bom, a sua parede tem {:.2f}m² e precisará de {:.2f} litros de tinta'.format(A, T))






