saldo_bancario = 1000.00
deposito = float(input("Digite um  valor de depósito:"))
saque = float(("Digite um valor de saque:"))
juros = float(input("Digite um fator de juros:"))

saldo_bancario += deposito
saldo_bancario -= saque
saldo_bancario *= juros

print(f"O saldo bancário final é: {saldo_bancario}")