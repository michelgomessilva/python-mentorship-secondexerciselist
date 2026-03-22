"""
6. Gestão de Candidatos (Set):
Compare dois conjuntos de candidatos (Python vs Analista). 
Exiba quem está em ambos, o total de inscritos únicos e quem é exclusivo de Python.
-------------------------------------------------------------------------------------------------------
"""

vaga_python = {"Ana", "Bruno", "Caio", "Felipe"}
vaga_analista = {"Caio", "Duda", "Elena", "Ana"}

# Operações de Conjunto (Álgebra de Boole)
both_jobs = vaga_python.intersection(vaga_analista)
all_candidates = vaga_python.union(vaga_analista)
only_python = vaga_python.difference(vaga_analista)

print(f"Candidatos em ambas as vagas: {both_jobs}")
print(f"Total de candidatos únicos: {len(all_candidates)}")
print(f"Exclusivos para Python: {only_python}")