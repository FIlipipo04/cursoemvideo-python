import random

tupla = random.choices(range(0, 11), k = 5)
maior = menor = tupla[0]

for c in tupla:
    if maior < c:
        maior = c
    if menor > c:
        menor = c
pos_maior = tupla.index(maior)
pos_menor = tupla.index(menor)
print(f'Os valores sorteados foram:', *tupla)
print(f'O maior numero sorteado foi: {maior} na posição {pos_maior+1}')
print(f'O menor numero sortedo foi: {menor} na posição {pos_menor+1}')