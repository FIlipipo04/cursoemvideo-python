'''Fazer programa qaue lêm o cateto oposto e adjacente e calcule a hipotenusa'''

'''import math

co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Agora digite o valor do cateto adjacente: '))
hi=math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

metodo usando a biblioteca
'''
#metodo usando a matematica mesmo
co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Digite o valor do cateto adjacente: '))
aux = (ca**2 + co**2)
hi = aux**(1/2)

print('O valor dos catetos eram {} e {}, sabendo disso a hipotenussa é {}.'.format(co,ca, hi))