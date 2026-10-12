# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 060 — Cálculo do fatorial
#
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 × 4
# × 3 × 2 × 1 = 120.
# === FIM DO ENUNCIADO ===

'''entrada = int(input())
fatorial = 1
for c in range(1, entrada + 1):
    fatorial *= c
print(fatorial)'''
#fiz no automatico e nao vi que era pra fazer com while, vou refazer
 
entrada = int(input('Digite um numero para calcular o seu faotrial: '))
contador = 1
fatorial = 1

print(f'calculando {entrada}! = ', end='')
while contador < entrada + 1:
    print(f'{contador}', end='')
    print(' X ' if contador < entrada else ' = ', end='')
    contador += 1
    fatorial *= contador
print(f'{fatorial}')
