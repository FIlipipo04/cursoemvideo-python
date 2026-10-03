'''Desenvolva um prograram que leia o primeiro termo e a razão de uma PA. No 
final mostre os 10 primeiros termos dessa progresão'''

n1 = int(input('Diga o primeiro termo da PA: '))
r = int(input('Diga a razão: '))

print(n1, end=" ")

for c in range(1,10):
    print(f'{n1+r}', end=" ")
    n1 += r