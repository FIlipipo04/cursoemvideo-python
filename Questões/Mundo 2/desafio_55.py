# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 055 — Maior e menor da sequência
#
# Faça um programa que leia o peso de cinco pessoas e, no final, mostre qual foi o maior e o
# menor peso lidos.
# === FIM DO ENUNCIADO ===

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Diga o peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.1f}kg')
print(f'O menor peso lido foi de {menor:.1f}kg')
