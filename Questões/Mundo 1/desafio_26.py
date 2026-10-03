'''Faça um programa qur leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em que possição ela aparece a primeira vez
Em qual posição ela aparece a ultima  vez
'''

frase0 = str(input('Digite uma frase:')).strip()
frase = frase0.upper()
print(frase.count('A'))
print(frase.find('A')+1)
print(frase.rfind('A')+1)



