'''
Faça um programa que leia três números e diga qual é o maior e qual o menor
'''
a = int(input('Digite um número: '))

maior = a
menor = a 

b = int(input('Diga outro número: '))

if b > maior:
    maior = b

elif b < menor:
    menor = b

c = int(input('Diga mais um número: '))

if c > maior:
    maior = c

elif c < menor:
    menor = c

print('Dentre os três números o maior é {} e o menor é {}.'.format(maior, menor))
