# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 050 — Soma dos pares
#
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.
# === FIM DO ENUNCIADO ===

s = 0
for c in range (1, 7):
    x = int(input('Digite um numero: '))
    if (x % 2 == 0):
        s += x
print(s)
