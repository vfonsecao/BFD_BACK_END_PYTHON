def calcular_media(*args):
    media = (sum(args) / len(args))
    return round(media, 2)

print(calcular_media(8.5, 9.0, 7.5))