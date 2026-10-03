'''from math import trunc #importei apenas a funcao trunc que era a que me interessava

x=float(input("Digite um número: "))
print('O numero {} tem a sua paret inteira {}'.format(x, trunc(x)))'''

#tambem podemos fazer usando o int
'''x = float(input('Digiote um numero: '))
print('O numero {} tem a sua parte inteira {}'.format(x, int(x)))'''

#e eu acho que tambem tem essa forma:
x=float(input('Escolha um numero: '))

print('O numero {} tem a sua parte inteira {:.0f}'.format(x, x))
