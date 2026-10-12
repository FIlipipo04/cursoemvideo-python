# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 025 — Procurando uma string dentro de outra
#
# Crie um programa que leia o nome completo de uma pessoa e mostre se ela tem "Silva" no
# nome.
# === FIM DO ENUNCIADO ===

'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome
'''

nome = str(input('Qual o  seu nome completo? '))
nome1 = (nome.title())
lista = (nome1.split())
print('Seu nome tem Silva?', 'Silva' in lista)
