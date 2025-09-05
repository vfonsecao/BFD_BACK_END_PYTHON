def buscar_livro(autor, **kwargs):
    livro = {"autor" : autor}
    for chave, valor in kwargs.items():
        livro[chave] = valor
        return livro

print(buscar_livro(autor = "Machado de Assis", ano = 1899))
