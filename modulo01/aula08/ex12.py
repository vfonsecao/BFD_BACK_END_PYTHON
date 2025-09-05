precos = [85, 120, 50, 250, 99]

produtos_filtrados = list(filter(lambda x: x > 100, precos))

print(produtos_filtrados)