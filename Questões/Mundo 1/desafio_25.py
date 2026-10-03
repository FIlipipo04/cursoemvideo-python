'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome
'''

nome = str(input('Qual o  seu nome completo? '))
nome1 = (nome.title())
lista = (nome1.split())
print('Seu nome tem Silva?', 'Silva' in lista)