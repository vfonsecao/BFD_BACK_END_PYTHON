arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')

pdf = sum(1 for arquivo in arquivos if arquivo.endswith('.pdf'))
print(f"A extensão .pdf aparece {pdf} vez(es) na tupla.")