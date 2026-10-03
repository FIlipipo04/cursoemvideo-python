'''escreva um programa para aprovar o emprestimo bancario para
a compra de uma casa. O programa vai perguntar o valor da casa, o 
salario do comprador e em quantos anos ele vai pagar 

calcule o valor da prestação mensal, sabendo que ela não pode 
exceder 30% do salario ou então o emprestimo será negado
'''

print ('Olá, este programa vai verificar se você consegue fazer um emprestimo bancario, para isso informe:')

casa = float(input('O valor da casa que deseja comprar: '))   
salario = float(input('O seu salario: '))
anos = float(input('E em quantos anos quer pagar: '))

nsalario = salario /100 * 30 #pra saber quanto é % do salario da pessoa
anos = anos  * 12 # vezes 12 pq ele quer saber quantos meses vai demorar pra pagar
mensal = casa / anos # pra saber a parcela mensal 
'''
teste:
print(casa)
print(salario)
print(anos)
print(mensal)
print(nsalario)
deu certo 
'''

print('Você deseja comprar uma casa no valor de R${:.2f} em {:.0f} anos tendo o salario R${:.2f}.'.format(casa, anos/12, salario))
if (nsalario >= mensal):
    print('Você pode comprar a casa desejada!! a parecla da casa ficou R${:.2f} em {:.1f} meses.'.format(mensal, anos))
else:
    print('Infelizmente você não pode comprar a casa pois a parecla mensal seria de R${:.2f}\ne ela excede o maximo permitido de 30% em relação ao seu salario que é R${:.2f}.'.format(mensal, nsalario))

