NOTA_MINIMA = 7.0
nota_final = float(input("Digite a sua nota final: "))

if nota_final >= NOTA_MINIMA:
    print("Aprovado!")
elif nota_final in (5 , 6):
    print("Você não foi muito bem. Mas ainda consegue recuperar.")
else:
    print("Reprovado!")    