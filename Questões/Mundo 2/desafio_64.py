num = contador = soma = 0
num = int(input('Digite um numero[999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um numero[999 para parar]: '))
print(f'Foram digitados {contador} e a soma de todos os numeros digitados é {soma}')