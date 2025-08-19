num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite o último número: "))

if num1 >= num2 and num1 >= num3:  # num1 é o maior número
    if num2 >= num3:
        print(num1, num2, num3)  # ordem: num1 > num2 > num3
    else:
        print(num1, num3, num2)  # ordem: num1 > num3 > num2

elif num2 >= num1 and num2 >= num3:  # num2 é o maior número
    if num1 >= num3:
        print(num2, num1, num3)  # ordem: num2 > num1 > num3
    else:
        print(num2, num3, num1)  # ordem: num2 > num3 > num1

else:  # num3 é o maior número
    if num1 >= num2:
        print(num3, num1, num2)  # ordem: num3 > num1 > num2
    else:
        print(num3, num2, num1)  # ordem: num3 > num2 > num1
