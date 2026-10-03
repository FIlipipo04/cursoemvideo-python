'''Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o ultimo nome separadamente'''

nome = input('Qual o seu nome?')
nome0 = nome.title()
nome1 = nome0.split()
print('O seu primeiro nome é {}'.format(nome1[0]))
print('O seu ultimo nome é {}'.format(nome1[-1]))