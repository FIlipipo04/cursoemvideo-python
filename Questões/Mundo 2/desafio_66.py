# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 066 — Vários números com flag
#
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# === FIM DO ENUNCIADO ===

c = soma = 0
while True:
    entrada = int(input('Digite um numero[999 para sair]: '))
    if entrada == 999:
        break
    soma += entrada
    c += 1
print(f'Foram digitaos {c} numeros e a soma deles é {soma}')
