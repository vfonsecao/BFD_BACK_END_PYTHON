nomes = ['Teclado', 'Mouse']
precos = [250, 120]
estoques = [10, 25]

for (nomes, precos, estoques) in zip(nomes, precos, estoques):
    print(f"Nome: {nomes}, Preço: R$ {precos}, Estoque: {estoques}")