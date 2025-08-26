status = input("Digite um dos seguintes status atual do seu pedido: recebido - em preparação - em entrega - entregue ")

match status:
    case "recebido":
        print("Obrigado pela confiança, enviaremos um e-mail com os detalhes da sua compra")
    case "em preparação":
        print("Aguarde mais alguns minuto, em breve enviaremos o código de rastreamento")
    case "em entrega":
        print("O seu produto está chegando. Fique atento")
    case "entregue":
        print("Obrigado, conte conosco sempre.")
    case _:
        print("Erro. Digite um status válido.")