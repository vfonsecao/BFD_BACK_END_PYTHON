num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

operadores_aritmeticos = input(
    " Escolha um dos operadores aritméticos: + , - , *, / , // , %"
)

if operadores_aritmeticos == "+":
    print(num1 + num2)
elif operadores_aritmeticos == "-":
    print(num1 - num2)
elif operadores_aritmeticos == "*":
    print(num1 * num2)
elif operadores_aritmeticos == "/":
    print(num1 / num2)
elif operadores_aritmeticos == "//":
    print(num1 // num2)
elif operadores_aritmeticos == "%":
    print(num1 % num2)
else:
    print("Operador inválido!")