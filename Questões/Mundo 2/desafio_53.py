# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 053 — Detector de palíndromo
#
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
# === FIM DO ENUNCIADO ===

a = str(input('Digite uma frase: '))
x = a.replace(" ", "")
x = x.lower()
y = x[::-1]
print(f'O inverso de {a.upper()} é {y.upper()}')
if (x == y):
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palínfromo')
