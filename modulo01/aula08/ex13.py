usuarios = [{'nome': 'Carlos', 'idade': 30}, {'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno', 'idade': 40}]

usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario['nome'])

print(usuarios_ordenados)