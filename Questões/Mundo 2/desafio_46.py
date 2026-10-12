# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 046 — Contagem regressiva
#
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# === FIM DO ENUNCIADO ===

'''Faça um program que mostre na tela uma contagem regressiva para o estouro de
 fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
import time

for c in range(10,-1,-1):
    print(c)
    time.sleep(1)
print('BUM! BUM! POOOOOOW!')
