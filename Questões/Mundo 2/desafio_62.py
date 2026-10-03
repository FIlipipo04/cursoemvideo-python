termo = int(input('Qual o primeiro termo da dua PA? '))
razao = int(input('E qual a razão da sua PA: '))
contador = 0
num = 1

print(f'{termo}', end= ' ')
while contador < 9:
    termo += razao
    contador += 1
    print(termo, end= ' ')

print('\nVocê quer mostrar mais algum termo? se sim digite quantos termos a mais você quer, se quiser encerrar digite 0')
while contador != 0:
    contador = int(input())
    while num < contador + 1:
        termo += razao
        num += 1
        print(termo, end= ' ')
    if contador != 0:
        print('\nQuer continuar? digite mais quantos numeros voce quer ver ou 0 para parar')
    num = 1
print('Progrma encerrado')
