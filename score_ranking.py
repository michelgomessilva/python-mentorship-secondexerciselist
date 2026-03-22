"""
10. Ranking de Pontuação (Dict & List):
Converta um dicionário de jogadores e pontos numa lista de tuplas ordenada. 
Exiba o Top 3 (ou o ranking atual disponível).
-------------------------------------------------------------------------------------------------------
"""

# Dados iniciais
scores = {
    "Michel": 980,
    "Junior": 1050,
    "Ana": 890,
    "Bruno": 1100
}

# Converter dicionário em lista de tuplas [(chave, valor)]
scores_list = list(scores.items())

# Ordenar a lista pelo valor (índice 1 da tupla) de forma decrescente
ranking = sorted(scores_list, key=lambda x: x[1], reverse=True)

print("\n--- RANKING GERAL ---")
# Acesso direto (sem loops)
print(f"1º Lugar: {ranking[0][0]} - {ranking[0][1]} pts")
print(f"2º Lugar: {ranking[1][0]} - {ranking[1][1]} pts")
print(f"3º Lugar: {ranking[2][0]} - {ranking[2][1]} pts")