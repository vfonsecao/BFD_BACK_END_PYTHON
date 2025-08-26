num = int(input("Digite um número de 1 a 5: "))

match num:
    case 1:
        print("Péssimo")
    case 2:
        print("Ruim")
    case 3:
        print("Regular")
    case 4:
        print("Bom")
    case 5:
        print("Ótimo")
    case _:
        print("Erro. Digite um número de 1 a 5.")