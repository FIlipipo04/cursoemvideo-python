# === ENUNCIADO (Curso em Vídeo) ===
# Desafio 073 — Tuplas com times de futebol
#
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre: a) os 5 primeiros colocados; b) os
# últimos 4 colocados; c) uma lista com os times em ordem alfabética; d) em que posição está
# o time da Chapecoense.
# === FIM DO ENUNCIADO ===

tupla = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'Coritiba', 'Red Bull Bragantino', 'São Paulo', 'Botafogo', 'Vitória', 'Corinthians', 'Mirassol', 'Vasco da Gama', 'Grêmio', 'Internacional','Remo', 'Chapecoense')
print('=-'*20)
print(f'Lista dos times do Brasileirão: {tupla}')
print('=-'*20)
print(f'Os cinco primeiros são: {tupla[0:5]}')
print('=-'*20)
print(f'Os ultimos 4 são: {tupla[-4:]}')
print('=-'*20)
print(f'Os times em ordem alfabeticação: {sorted(tupla)}')
print('=-'*20)
posicao = (tupla.index('Chapecoense')) + 1
print(f'O Chapecoense está na {posicao} posição')
