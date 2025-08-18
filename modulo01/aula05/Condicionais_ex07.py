num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
num3 = int(input("Digite o último número:"))

if num1 >= num2 and num2 >= num3:
    print(num3, num2, num1)
elif num1 <= num2 and num1 >= num3:
    print(num3, num1, num2)


elif num1 >= num2 and num2 <= num3:
    print(num2, num3, num1)
elif num1 >= num2 and num3 >= num1:
    print(num2, num1, num3)


elif (num1 <= num3) and (num2) and (num3 >= num2):
    print(num1, num3, num2)
elif (num1 <= num3) and (num2) and (num3 <= num2):
    print(num1, num2, num3)
