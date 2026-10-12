# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 061 — Progressão aritmética v2.0
#
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.
# === FIM DO ENUNCIADO ===

termo = int(input('Qual o primeiro termo da dua PA? '))
razao = int(input('E qual a razão da sua PA: '))
contador = 1
print(f'{termo}', end= ' ')
while contador < 10:
    termo += razao
    contador += 1
    print(termo, end= ' ')
