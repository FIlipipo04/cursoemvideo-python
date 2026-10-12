# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 020 — Sorteando uma ordem na lista
#
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# === FIM DO ENUNCIADO ===

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

