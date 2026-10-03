'''escreva um algoritmo que pergunte o salário de um funcionario e calcule o valor do seu aumento. 
Para seu salaririos superiores a 1250 calcule um aumento de 10%
para salarios menores ou iguais calcule 15%
'''
x = float(input('Digite o seu salario: '))

if x >1250:
    x = x*1.10
    print('Parabens! Você recebeu um aumento de 10% e seu salario agora é {}'.format(x))

elif x <= 1250: 
    x = x*1.15
    print('Parabens! Você recebeu um aumeneto de 15% e o seu salario agora é de {}'.format(x)) 