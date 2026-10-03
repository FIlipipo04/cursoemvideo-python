tupla = ()
cont = 0
pos = 0
cont = ()
for _ in range(4):
    num = int(input('Digite um numero: '))
    tupla += (num,)
    if num % 2 == 0:
        cont += (num,)
for indice, conteudo in enumerate(tupla):
    if pos > 1:
        if conteudo == 3:
            pos = indice + 1
            break
rep = tupla.count(9)
print(f'Você digitou os valores ', *tupla)
if pos == 0:
    print('O valor 3 não foi digitado em nem uma posição')
else:
    print(f'O valor 3 aparece na posição {pos}')
print(f'O numero 9 aparece {rep} vezes')
print(f'Os pares digitados foram', *cont)

