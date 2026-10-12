# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 048 — Soma ímpares múltiplos de três
#
# Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de três
# (3) e que se encontram no intervalo de 1 até 500.
# === FIM DO ENUNCIADO ===

'''Faça um programa que calcule a soma entre 
todos os numeros impares que sao multiplos de 
tres e que estao no intervalo 1 ate 500'''

s = 0
cont = 0
for c in range(3, 500, 3):
    if (c % 2 != 0):
        s += c
        cont +=1
print(s)
print(cont)
