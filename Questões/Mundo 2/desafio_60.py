'''entrada = int(input())
fatorial = 1
for c in range(1, entrada + 1):
    fatorial *= c
print(fatorial)'''
#fiz no automatico e nao vi que era pra fazer com while, vou refazer
 
entrada = int(input('Digite um numero para calcular o seu faotrial: '))
contador = 1
fatorial = 1

print(f'calculando {entrada}! = ', end='')
while contador < entrada + 1:
    print(f'{contador}', end='')
    print(' X ' if contador < entrada else ' = ', end='')
    contador += 1
    fatorial *= contador
print(f'{fatorial}')
