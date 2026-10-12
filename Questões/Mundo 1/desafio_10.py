# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 010 — Conversor de moedas
#
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar.
# === FIM DO ENUNCIADO ===

'''fazer um programa que converte valor em real para dolar.'''

#cotação dolar dia 29/11/2025 ta $5,32

print('Este progrma fará a conversão do seu dinho em reais para dolar.')
v = float(input('Quantos reais você quer convereter?'))
d = v/5.35
print('Você tinha R${}, isso dá ${:.2f}.'.format(v, d))
