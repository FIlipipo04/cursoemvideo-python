# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 032 — Ano bissexto
#
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# === FIM DO ENUNCIADO ===

'''
Escreva um algoritimo que leia um ano qualquer e diga se ele é bissexto
'''
ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print('Seu ano é bissexto')

else:
    print('Ele não é bissexto')

    
