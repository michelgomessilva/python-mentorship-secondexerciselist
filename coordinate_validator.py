"""
9. Validador de Tuplas em Conjuntos (Set & Tuple):
Peça coordenadas (x, y). Use tuplas para armazenar e um Set para 
garantir que não existam coordenadas duplicadas.
-------------------------------------------------------------------------------------------------------
"""

try:
    points_set = set()

    # Ponto 1
    x1 = int(input("Ponto 1 X: "))
    y1 = int(input("Ponto 1 Y: "))
    points_set.add((x1, y1))

    # Ponto 2
    x2 = int(input("Ponto 2 X: "))
    y2 = int(input("Ponto 2 Y: "))
    
    # Verificação de duplicado manual (sem loop)
    if (x2, y2) in points_set:
        print(f"Aviso: A coordenada ({x2}, {y2}) já existe e foi ignorada.")
    else:
        points_set.add((x2, y2))

    print(f"\nPontos Únicos Registrados: {points_set}")

except ValueError:
    print("Erro: As coordenadas devem ser números inteiros.")