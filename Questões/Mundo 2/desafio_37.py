'''escreva um programa que leia um numero e peça para o usuario usuario qual 
sera a base de conversão:
1 para binario 
2 para octal 
3 para hexadecimal

oct(x)
hex(x)
bin(x)
'''

print('Esse programa trasformará um numero de base 10 para a uma base da sua escolha')
x = int(input('Diga um numero inteiro: '))
b = int (input('Diga 1 base escolher base binaria, 2 para octal e 3 para hexadecimal: '))
if (b==1):
    x1 = bin(x)
elif (b==2):
    x1 = oct(x)
else:
    x1 = hex(x)

print ('Você escolheu o numero {} tendo como resultado o numero {}'.format(x, x1[2:]))



