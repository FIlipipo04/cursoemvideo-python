'''
Escreva um algoritimo que leia um ano qualquer e diga se ele é bissexto
'''
ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print('Seu ano é bissexto')

else:
    print('Ele não é bissexto')

    
