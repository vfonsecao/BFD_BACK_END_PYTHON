def contador_vogais(texto):
    vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛ'
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

print(contador_vogais("Victor Fonsêca"))