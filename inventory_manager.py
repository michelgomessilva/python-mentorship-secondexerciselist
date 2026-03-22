"""
1. Sistema de Inventário Único (Set & List):
Peça ao usuário nomes de produtos (separados por vírgula). 
Converta em List, remova duplicados com Set e exiba a lista ordenada 
alfabeticamente, informando quantos itens repetidos foram removidos.
-------------------------------------------------------------------------------------------------------
"""

try:
    raw_input = input("Digite os produtos (ex: maçã, banana, maçã): ").strip()

    if not raw_input:
        print("Erro: A entrada não pode estar vazia.")
    else:
        # Criamos a lista inicial e limpamos espaços extras de cada item
        # Usamos replace para garantir consistência antes do split
        initial_list = raw_input.replace(", ", ",").split(",")
        
        # O Set remove automaticamente as duplicatas
        unique_items = set(initial_list)
        
        # Cálculo de duplicados
        duplicates_removed = len(initial_list) - len(unique_items)
        
        # Ordenação alfabética
        sorted_inventory = sorted(list(unique_items))

        print(f"\nInventário Atualizado: {sorted_inventory}")
        print(f"Itens duplicados removidos: {duplicates_removed}")

except Exception as e:
    print(f"Erro inesperado: {e}")