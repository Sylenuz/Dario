vendas={"janeiro": 1000, "fevereiro": 1500, "março": 1200}

total_vendas=0
for mes, valor in vendas.items():
    total_vendas += valor

print(f"Total de vendas: {total_vendas}")