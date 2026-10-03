'''
crie um program que leia o nome completo de uma pessoa e mostre :
o nome com todas as letras maisculas
o nome com todas as letras minusculas
quastas letras ao todo sem condsiderar os espaços
quasntas letras tem o primeiro nome 
'''
'''nome = input('Qual o seu nome?')
print(nome.upper())
print(nome.lower())
nome2 = (nome.replace(' ', ''))
print(('Seu nome tem {} letras').format(len(nome2)))
nome3 = nome.split()
#print(nome3)
print(('Seu primeiro nome tem {} letras.').format(len(nome3[0])))
'''
# essa foi a forma que eu fiz, o guanabara fez diferente e eu vou colocar a baixo:

nome = str(input('Qual o seu nome completo?')).strip()
# ele deixou explicito que é str e adicionou a função stipe pra tirar os espaços das laterais
print('O seu nome maiusculo é {}'.format(nome.upper()))
# aqui ele fez tudo numa linnha só e usou o format pra deixar mais organizado
print('O seu nome em minusculo é {}'.format(nome.lower()))
# aqui a mesma coisa
print('O seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# aqui ele fez usando manipulação de str, já eu fiz removendo separadamente os espaços
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
# aqui foi genial, ele fez usando find, ou seja, ele proucurou o primeiro espaço e perguntou onde ele tava, como o python conta começando do 0 da cetinho a coontagem
   




