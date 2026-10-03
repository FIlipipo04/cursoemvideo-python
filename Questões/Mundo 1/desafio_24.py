'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com santo'''

nome = str(input('Digite o nome da sua cidade:'))
nome1 = nome.title()
lista = (nome1.split())
print('Rio' == lista[0])
