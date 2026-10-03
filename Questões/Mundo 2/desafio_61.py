termo = int(input('Qual o primeiro termo da dua PA? '))
razao = int(input('E qual a razão da sua PA: '))
contador = 1
print(f'{termo}', end= ' ')
while contador < 10:
    termo += razao
    contador += 1
    print(termo, end= ' ')