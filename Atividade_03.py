def IMC(p, a ):
    t = p / (a**2)
    return t


qtp = int(input("quantidade de pessoas :"))

for i in range(qtp):
    print(f"\npessoa{i+1}")
    peso = float(input("Informe o peso: "))
    altura = float(input("Informe a altura: "))




a = IMC(peso, altura)

match a:
    case a if a < 17:
        classificacao = ' Muito Abaixo'
    case a if a < 18.5:
        classificacao = 'Abaixo do peso'
    case a if a < 25:
        classificacao = 'Peso normal'
    case a if a < 30:
        classificacao = 'Acima do peso'
    case a if a < 35:
        classificacao = "Obesidade grau | "
    case a if a < 40:
        classificacao = 'Obesidade Grau ||'
    case _:
        classificacao = 'Obesidade grau |||'

# Saída 
print(30 * "-")
print("Resultado")

print(f"IMC {a:.2f}")
print(f"Classficação {classificacao}")
    