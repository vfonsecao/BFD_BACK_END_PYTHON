clientes = ['João', 'Maria', 'José' ]
saldos = [1500, 2500, 800]

for i, (cliente, saldo) in enumerate(zip(clientes, saldos), start = 1):
    print(f"{i}º Cliente: {cliente}, Saldo: R${saldo}")