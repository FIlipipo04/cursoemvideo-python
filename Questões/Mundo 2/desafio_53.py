a = str(input('Digite uma frase: '))
x = a.replace(" ", "")
x = x.lower()
y = x[::-1]
print(f'O inverso de {a.upper()} é {y.upper()}')
if (x == y):
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palínfromo')