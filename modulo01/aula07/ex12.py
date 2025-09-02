import re
import string

frase = input("Digite aqui a sua frase: ")

# Substitui pontuações por espaço para não juntar palavras compostas
removedor_pontuacao = re.sub(f"[{re.escape(string.punctuation)}]", " ", frase)

# Cria lista de palavras em minúsculas para evitar duplicidade entre maiúsculas e minúsculas
palavras = [palavra.lower() for palavra in removedor_pontuacao.split() if palavra.strip()]


palavras_unicas = set(palavras)
quantidade = len(palavras_unicas)


print(f"Palavras únicas na frase: {palavras_unicas}")
print(f"Quantidade de palavras únicas: {quantidade}")