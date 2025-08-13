idade = int(input("Digite sua idade: "))
IDADE_MINIMA = 18
idade_categoria = ["O usuário é menor de idade", "O usuário é maior de idade"]
print(idade_categoria[idade >= IDADE_MINIMA])