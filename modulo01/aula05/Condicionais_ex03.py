IDADE_MINIMA = 18
idade_usuario = int(input("Digite a sua idade:"))

if idade_usuario >= IDADE_MINIMA:
    print("O usuário é maior de idade.")
elif (idade_usuario < IDADE_MINIMA) and (idade_usuario >= 16):
    print("O usuário é menor e tem 16 ou 17 anos")
