def lerVendas(arquivo):
    vendas = []
    with open('vendas.txt','r',encoding='utf-8') as arquivo:
        for linha in arquivo:
            data, produto, quantidade, precoUnitario = linha.split(',')
            quantidade = int(quantidade)
            precoUnitario = float(precoUnitario)
            vendas.append((data, produto, quantidade, precoUnitario))
    return vendas

def calcularTotal(vendas):
    total_por_produto = {}
    total_por_dia = {}
    total_geral = 0.0

    for data, produto, quantidade, preco_unitario in vendas:
        total_venda = quantidade * preco_unitario
        total_por_produto[produto] = total_por_produto.get(produto, 0) + total_venda
        total_por_dia[data] = total_por_dia.get(data, 0) + total_venda
        total_geral += total_venda
    
    return total_por_produto, total_por_dia, total_geral

def relatorio(total_por_produto, total_por_dia, total_geral):
    relatorio = [
        "Relatório de Vendas",
        "--------------------",
        "\nTotal de Vendas por Produto:",
        *[f"{produto}: R$ {total:.2f}" for produto, total in total_por_produto.items()],
        "\nTotal de Vendas por Dia:",
        *[f"{data}: R$ {total:.2f}" for data, total in total_por_dia.items()],
        f"\nTotal Geral de Vendas: R$ {total_geral:.2f}"
    ]
    
    with open("relatorio.txt", 'w', encoding='utf-8') as arquivo:
        arquivo.write("\n".join(relatorio))

arquivo = 'vendas.txt'
vendas = lerVendas(arquivo)
totalProduto, totalDia, totalGeral = calcularTotal(vendas)
relatorio(totalProduto, totalDia, totalGeral)    
with open('relatorio.txt','r',encoding='utf-8') as arquivo:
    print(arquivo.read())