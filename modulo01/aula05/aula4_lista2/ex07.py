idade_motorista = int(input("Qual a sua idade? "))
tem_carteira = input("Você tem carteira de motorista? (s/n) ") == "s" or input("Você tem carteira de motorista? (s/n) ") == "s"

pode_dirigir = idade_motorista >= 18 and tem_carteira
print(f"Pode dirigir? {pode_dirigir}")
