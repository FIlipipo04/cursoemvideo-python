# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 064 — Tratando vários valores v1.0
#
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# === FIM DO ENUNCIADO ===

num = contador = soma = 0
num = int(input('Digite um numero[999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um numero[999 para parar]: '))
print(f'Foram digitados {contador} e a soma de todos os numeros digitados é {soma}')
