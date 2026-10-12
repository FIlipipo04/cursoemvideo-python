# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 006 — Dobro, triplo e raiz quadrada
#
# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a sua raiz
# quadrada.
# === FIM DO ENUNCIADO ===

'''fazer codigo que mostre o dobro, triplo e raiz qudrada de um numero'''

num= int(input('escreva um numero:'))

print('o dobro do seu numero é {}, o seu triplo é {}, já a raiz quadrada é {:.2f}'.format(num*2, num*3, num**(1/2)))
