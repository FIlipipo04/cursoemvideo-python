num = int(input('Digite um numero: '))
maior = num
menor = num
contador = 1
soma = num
condicao = input('Deseja continuar? [S/N]').upper()
while condicao != 'N':
    num = int(input('Digite um numero: '))
    contador += 1
    soma += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    condicao = str(input('Deseja continuar? [S/N]').upper()).strip()[0]
print(f'Foram digitados {contador} numeros, a media deles é {soma/contador:.2f}. O maior foi {maior} e o menor foi {menor}')