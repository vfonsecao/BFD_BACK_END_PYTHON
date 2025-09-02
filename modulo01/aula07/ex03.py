vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]

total = sum(vendas_semana)
menor_venda = min(vendas_semana)

semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

indice = vendas_semana.index(menor_venda)

print(f"O total de vendas na semana:  {total}")
print(f"O dia com menos vendas foi:  {semana[indice]} com {menor_venda}")