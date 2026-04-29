# lim 100 mult 4 

def mult(m ):
    f = m * 4
    return f


kg = int(input("Quantos kl de peixe : kg"))

if kg > 100:
   p = kg - 100
   resultado = mult(p) 
   print(f"O resultado da multa foi R${resultado}")
   print(f"R${kg}; sem multas")
else:
    print(f"R${kg}; sem multas")



