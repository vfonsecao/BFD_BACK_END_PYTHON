km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugado = int(input("Digite a quantidade de dias que o carro foi alugado: "))

preco_total = (dias_alugado * 60) + (km_percorridos * 0.15)

print(f"O preço a pagar é: R$ {preco_total:.2f}")
