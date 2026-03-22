"""
4. Otimizador de Rotas de Entrega (List & Tuple):
Receba 3 destinos e suas distâncias. Armazene cada par em uma Tuple 
dentro de uma List. Exiba o roteiro ordenado da menor para a maior distância.
-------------------------------------------------------------------------------------------------------
"""

try:
    # Captura de 3 destinos
    dest1 = (input("Destino 1: ").strip(), float(input("Distância 1 (km): ").replace(",", ".")))
    dest2 = (input("Destino 2: ").strip(), float(input("Distância 2 (km): ").replace(",", ".")))
    dest3 = (input("Destino 3: ").strip(), float(input("Distância 3 (km): ").replace(",", ".")))

    route_list = [dest1, dest2, dest3]

    # Ordenação por distância (o segundo elemento da tupla - índice 1)
    optimized_routes = sorted(route_list, key=lambda x: x[1])

    print("\n--- Roteiro de Entrega Otimizado ---")
    print(f"1º Paragem: {optimized_routes[0][0]} ({optimized_routes[0][1]}km)")
    print(f"2º Paragem: {optimized_routes[1][0]} ({optimized_routes[1][1]}km)")
    print(f"3º Paragem: {optimized_routes[2][0]} ({optimized_routes[2][1]}km)")

except ValueError:
    print("Erro: Valor de distância inválido.")