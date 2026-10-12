# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 012 — Calculando descontos
#
# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de
# desconto.
# === FIM DO ENUNCIADO ===

'''algoritomo que da descontos de 5% par acompras
'''

x=float(input('Qual o valor do produto? R$'))
desconto = x * 0.05
valorfinal = x - desconto
print('O valor do produto com 5% de desconto é R${:.2f}'.format (valorfinal))   



