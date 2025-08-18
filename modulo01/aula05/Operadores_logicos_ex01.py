tem_wifi = False
tem_dados_moveis = True

pode_se_conectar = not tem_wifi or tem_dados_moveis
print(f"O celular pode se conectar a internet? {pode_se_conectar}")
