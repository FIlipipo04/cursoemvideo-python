# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 044 — Gerenciador de pagamentos
#
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e a condição de pagamento: à vista em dinheiro/cheque → 10% de desconto; à
# vista no cartão → 5% de desconto; em até 2x no cartão → preço normal; em 3x ou mais no
# cartão → 20% de juros.
# === FIM DO ENUNCIADO ===

'''
Elabore um programa que calcule o valor a ser pago por um produto,
cosiderando o seu preço e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

preco = input(float("Qual o valor do produto?"))
