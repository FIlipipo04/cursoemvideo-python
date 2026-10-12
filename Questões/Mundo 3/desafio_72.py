# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 072 — Número por extenso
#
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.
# === FIM DO ENUNCIADO ===

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num <= -1 or num > 20:
        num = int(input('Tente outra vez. digite um numero: '))
    else:
        print(f'Você digitou o numero {tupla[num]}')
        break
