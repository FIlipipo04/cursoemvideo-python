a = 0
b = 1
num = 1

entrada = int(input('Quantos termos da sequencia de Fibonacci você quer ver? '))
if entrada == 0:
    print('Você nao quer nem um numero da sequencia')
elif entrada >= 1:
    while num < entrada:
        print(a, end='->')
        a, b = b, a + b
        num += 1
    print(a)
else:
    print('Numero invalido')
