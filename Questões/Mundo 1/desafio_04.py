'''fazer programa que leia pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ele'''

print('Olá! Vamos fazer um teste? Escreva qualquer coisa, seja letras, numeros ou apenas simbolos e este programa classificará.')

A=input()
print('O tipo primitivo desse valor é', type(A))
print('Só tem espaços?', A.isspace())
print("Só tem numeros?", A.isnumeric())
print('Só tem letras?', A.isalpha())
print('Só tem letras maiusculas?', A.isupper())


'''
isalpha() → só letras.
isdigit() → só números (0–9).
isalnum() → letras e/ou números.
islower() → tudo minúsculo.
isupper() → tudo maiúsculo.
istitle() → cada palavra começa com maiúscula.
isspace() → só espaços (ou tab, quebra de linha).
isdecimal() → só números decimais puros.
isnumeric() → qualquer símbolo numérico (frações, romano etc).
isidentifier() → pode ser nome de variável.
isprintable() → só caracteres imprimíveis.
'''