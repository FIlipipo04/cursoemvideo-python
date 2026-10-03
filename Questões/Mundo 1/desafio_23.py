'''Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
ex: 
digito 8963
unidade:3
dezana :6
centena:9
milhar:8
'''
num  = int(input('Digite um numero de quatro digitos:'))
# sempre declarar o tipo da str

u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10 
print('Fazendo a deconposiçãoa do seu número {} obtemos: \nunidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'.format(num, u, d, c, m))

