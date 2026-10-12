# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 029 — Radar eletrônico
#
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa custa R$7,00 por cada Km acima do
# limite.
# === FIM DO ENUNCIADO ===

'''
Escreva um programa que leia a velocidade de um carro. 
se ele ultrapassar 80km/h, mostre que ele esta acima da velocidade permitida e pagara uma multa.
a multa vai custa 7 rais por cada km acima do limite
'''

v = int(input('Digite a velocidade do seu carro:'))

if v <= 0:
    print('Volocidade invalida.')
elif v > 80:
    c = (v-80)*7
    print('Você foi multado por estar acima da velocidade permitida. O valor\nda multa foi de R${}.'.format(c))
else:
    print('Vovê é um bom condutor e está dentro da velocidade permitida.')
