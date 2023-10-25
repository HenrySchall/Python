# install.packages("radian")

vendedores = ['Vendedor 1', 'Vendedor 2', 'Vendedor 3', 'Vendedor 4', 'Vendedor 5']
vendas_por_vendedor = {}

for vendedor in vendedores:
    vendas = []
    for dia in range(1, 8):
        venda_dia = float(input(f"Digite a venda do {vendedor} no dia {dia}: R$ "))
        vendas.append(venda_dia)
    vendas_por_vendedor[vendedor] = vendas

# Exiba as vendas por vendedor
for vendedor, vendas in vendas_por_vendedor.items():
    print(f"Vendas de {vendedor}: {vendas}")

# Calcule e exiba as vendas totais por vendedor
for vendedor, vendas in vendas_por_vendedor.items():
    total_vendas = sum(vendas)
    print(f"Total de vendas de {vendedor}: R$ {total_vendas:.2f}")



