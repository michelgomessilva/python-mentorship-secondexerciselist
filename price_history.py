"""
7. Histórico de Preços com Flutuação (List & Dict):
Mantenha um histórico de 4 preços. Ao adicionar um novo, remova o mais antigo.
Exiba o maior e o menor preço do histórico atual.
-------------------------------------------------------------------------------------------------------
"""

try:
    product_data = {"Smartphone": [1200.0, 1150.0, 1300.0, 1100.0]}
    
    new_price = float(input("Digite o novo preço: ").replace(",", "."))
    
    prices = product_data["Smartphone"]
    
    # Lógica de Fila (First In, First Out)
    prices.pop(0)  # Remove o índice 0 (mais antigo)
    prices.append(new_price)
    
    print(f"\nHistórico Atualizado: {prices}")
    print(f"Maior Preço: €{max(prices):.2f}")
    print(f"Menor Preço: €{min(prices):.2f}")

except ValueError:
    print("Erro: Entrada de preço inválida.")