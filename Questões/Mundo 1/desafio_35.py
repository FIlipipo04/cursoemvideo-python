'''leia tres retas e verifiqur se elas formam um triangulo'''

r1 = float(input('Diga o valor de uma reta: '))
r2 = float(input('DIgite outro valor para reta: '))
r3 = float(input('Mais um valor: '))


if (r1<r2+r3 and r2<r1+r3 and r3<r1+r2):
    if (r1==r2 and r2==r3):
        print('As retas informadas geram um triangulo equilatero')
    elif (r1==r2 or r1==r3 or r2==r3):
        print('As retas informadas geram um triangulo isosceles')
    else:
        print('As retas informadas geram um triangulo escaleno')
else:
    print('Não formam um triangulo')