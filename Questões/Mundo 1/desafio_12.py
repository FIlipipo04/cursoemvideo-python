'''algoritomo que da descontos de 5% par acompras
'''

x=float(input('Qual o valor do produto? R$'))
desconto = x * 0.05
valorfinal = x - desconto
print('O valor do produto com 5% de desconto é R${:.2f}'.format (valorfinal))   



