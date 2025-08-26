cor_semaforo = input("Digite uma cor: verde - amarelo - vermelho ")

match cor_semaforo:
    case "verde":
        print("Pode passar")
    case "amarelo":
        print("Atenção")
    case "vermelho":
        print("Pare")
    case _:
        print("Erro. Digite uma cor válida. E se dirigir não beba.")