# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 013 — Reajuste salarial
#
# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com
# 15% de aumento.
# === FIM DO ENUNCIADO ===

'''fazer programa que da 15% de aumneto no salario'''

salario = float(input('Digite o salario do funcionario: R$ '))
aumento = salario * 0.15
novo_salario = salario + aumento
print('O salario com 15% de aumento sera de R$ {:.2f}'.format(novo_salario))    
