def cadastrar_usuario(nome, email, **kwargs):
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")

cadastrar_usuario(nome = "Victor Fonsêca", email = "vfonseca132@gmail.com", cidade = "Recife")
