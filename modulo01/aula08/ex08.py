def atualizar_perfil(perfil, **kwargs):
    for chave, valor in kwargs.items():
        perfil[chave] = valor
    return perfil

perfil = {'nome': 'João', 'idade': 30}
print(perfil)

atualizar_perfil(perfil, idade=31, cidade="Rio de Janeiro")
print(perfil)