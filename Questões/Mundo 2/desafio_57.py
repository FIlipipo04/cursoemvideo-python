'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto'''
sexo = ''
condicao = 'S'
while condicao == 'S':
    sexo = str(input('Digite o seu sexo: [F/M]')).upper().strip()[0]
    if sexo in 'FM':
        condicao = 'N'
    else:
        print('Digite um valor validoS')
print(f'Sexo {sexo} registrado com sucesso')