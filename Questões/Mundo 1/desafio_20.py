#codigo para fazer sorteio de trabalhos
import random
a1=input(print('Primeiro aluno: '))
a2=input(print('Segundo aluno: '))
a3=input(print('Terceiro aluno'))
a4=input(print('Quarto aluno: '))
lista = [a1,a2,a3,a4]
sorteados = random.shuffle(lista) 
print ('A ordem será:')
print(lista)

