# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 054 — Grupo da maioridade
#
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.
# === FIM DO ENUNCIADO ===

from datetime import datetime
a = datetime.now().year
im = 0
i = 0

for c in range(1, 8):
    x = int(input(f'Em que ano a {c}° pessoa nasceu?'))
    idade = a - x
    if idade >= 21:
        im += 1
    else: 
        i += 1
print(f'Ao todo tivemos {im} pessoas maiores de idade\nE tambem tivemos {i} pessoas menores de idade')
