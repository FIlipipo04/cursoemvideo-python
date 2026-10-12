# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 043 — Índice de Massa Corporal
#
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre
# o seu status: abaixo de 18,5 → abaixo do peso; entre 18,5 e 25 → peso ideal; 25 a 30 →
# sobrepeso; 30 a 40 → obesidade; acima de 40 → obesidade mórbida.
# === FIM DO ENUNCIADO ===

'''
Desenvolva um programa que leia o peso e a altura de uma pessoa e determine o seu imc. 
depois verifique em qual faixa ela se encontra
abaixo de 18.5 = abaixo do peso
18.5 - 25 = peso ideal 
25 - 30 =   sobrepeso 
30 - 40 = obesidade 
+40 = obesidade morbida 
'''

peso = float(input('Entre com o seu peso: '))
altura = float(input('Entre com a sua altura em mestros: '))
imc = peso / (altura * altura)

if (imc < 18.5):
    print('Você se encontra abaixo do peso.')
elif (imc < 25):
    print('Você está no peso ideal!')
elif (imc < 30):
    print('Você está em sobrepeso!')
else:
    print('Você está obeso.')
