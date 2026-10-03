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