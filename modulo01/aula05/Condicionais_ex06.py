NOTA_MINIMA = 7.0
nota_final = float(input("Digite a sua nota final:"))

if nota_final >= NOTA_MINIMA:
    print("Aprovado!")
elif (nota_final < NOTA_MINIMA) and (
    nota_final >= 5.0
):  # as notas 5 a 6.99 ainda podem se recuperar
    print("Você não foi muito bem, mas ainda pode se recuperar.")
else:
    print("Reprovado!")
