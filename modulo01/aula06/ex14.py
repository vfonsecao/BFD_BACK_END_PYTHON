senha =  "python123"
tentativa = input("Digite a sua senha:")

while tentativa != senha:
    print("Senha incorreta. Digite novamente.")
    tentativa = input("Digite novamente sua senha:")

    print("Senha correta! Acesso permitido.")


