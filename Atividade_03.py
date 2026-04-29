def IMC(p, a ):
    t = p / (a*a)
    return t


mp = float(input("Qual é seu peso : "))

ma = float(input("Qual é sua altura : "))

i = IMC(mp, ma)

if i > 18.5:
    print('Abaixo do peso.')
elif 18.6 > i > 24.9:
    print('Peso ideal ( parabéns).')
elif 25 > i > 29.9:
    print('Levemente acima do peso.')
elif 30 > i > 34.9 :
    print('Obesidade grau l.')
elif 35 > i > 39.9:
    print('Obesidade grau ll (severa).')
else:
    print('Obesidade grau lll (mórbida).')
