c = soma = 0
while True:
    entrada = int(input('Digite um numero[999 para sair]: '))
    if entrada == 999:
        break
    soma += entrada
    c += 1
print(f'Foram digitaos {c} numeros e a soma deles é {soma}')
