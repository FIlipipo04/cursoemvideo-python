# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 007 — Média aritmética
#
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# === FIM DO ENUNCIADO ===

'''programa pra mostra media de duas notas de aluno'''

N1 = float(input('Qual é a sua primeira nota?'))
N2 = float(input('E a segunda?'))
N = (N1 + N2) / 2

print('As suas notas foram {} e {}, a media delas é {}'.format(N1, N2, N))
