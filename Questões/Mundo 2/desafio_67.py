# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 067 — Tabuada v3.0
#
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for
# negativo.
# === FIM DO ENUNCIADO ===

while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if num > 0:
        for c in range(1, 11):
            print(f'{num} X {c} = {num * c}')
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
