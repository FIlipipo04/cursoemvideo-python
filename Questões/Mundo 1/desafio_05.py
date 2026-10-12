# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 005 — Antecessor e sucessor
#
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu
# antecessor.
# === FIM DO ENUNCIADO ===

'''fazer programa que mostre o sucessor e anterior de um numero'''

print('Olá!!! vamos ver o sucessor e o antecessor de um numero?', end= ' ')
b = int(input ('Escreva o numero que quiser:'))

print('Você escolheu o numero {}, o seu sucessor é {} e o seu antecessor é {}.' .format(b, b+1, b-1))
