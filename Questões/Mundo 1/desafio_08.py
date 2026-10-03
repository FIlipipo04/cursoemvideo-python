'''programa pra trasformar medidas em metros para várias unidades'''

print('Está com dificuldades em fazer a conversão de medidas em metros? Este programa é para te ajudar!!', end=' ')
M = float(input('Diga quantos metros você quer converter: '))

# Conversões para cima (maiores)
KM = M / 1000
HM = M / 100
DAM = M / 10

# Conversões para baixo (menores)
DM = M * 10
CM = M * 100
MM = M * 1000

print(f'\nVocê colocou {M} metros, que equivale a:')
print(f'  • {KM} quilômetros (km)')
print(f'  • {HM} hectômetros (hm)')
print(f'  • {DAM} decâmetros (dam)')
print(f'  • {DM} decímetros (dm)')
print(f'  • {CM} centímetros (cm)')
print(f'  • {MM} milímetros (mm)')