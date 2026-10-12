# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 063 — Sequência de Fibonacci v1.0
#
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma sequência de Fibonacci. Ex: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
# === FIM DO ENUNCIADO ===

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
