'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passangem, cobrando R$0,50 por km para viagens até 200km e R$0,45 para 
viagens mais longas 
'''

km = float(input('Digite qual a distancia da sua viagem:'))

if km <= 0 :
    print('Digite um valor valido.')

elif km <= 200:
    print ('O valor da sua passagem é R${}. '.format(km * 0.5))

else:
    print ('Como sua viagem tem mais de 200km voce paga com 10% de desconto, tendo um proço final de R${' \
    '}'.format(km * 0.45))