"""
Exercício 4: Classificador de Notas (Dict + ELIF)
Objetivo: Mapear dados e aplicar lógica de classificação sobre os valores.
Crie um dicionário chamado boletim com 3 matérias e suas respectivas notas.
Peça para o usuário digitar o nome de uma matéria.

Lógica:
Se a matéria existir no dicionário:
    Se a nota for >= 7: exiba "Aprovado em [Matéria]".
    Se a nota for entre 5 e 6.9: exiba "Recuperação em [Matéria]".
    Se for menor que 5: exiba "Reprovado em [Matéria]".
Se a matéria não existir, exiba "Matéria não encontrada".
-------------------------------------------------------------------------------------------------------
"""

# Definição do Dicionário (Mapeamento de Chave e Valor)
student_grades = {
    "Matematica": 8.5,
    "Portugues": 6.0,
    "Historia": 4.5
}

# Captura e normalização (Title Case para bater com as chaves do Dict)
subject = input("Qual matéria deseja consultar? ").strip().title()

# Guard Clause: Verificamos primeiro se a matéria existe
subject_grade = student_grades.get(subject)

if subject_grade is None:
    print(f"\n[ERRO] Matéria '{subject}' não encontrada no sistema.")

else:
    # Lógica de Classificação sobre o valor encontrado
    status = ""
    
    if subject_grade >= 7.0:
        status = "Aprovado"
    elif subject_grade >= 5.0:
        status = "Recuperação"
    else:
        status = "Reprovado"

    print(f"\n--- Resultado Final ---")
    print(f"Matéria: {subject}")
    print(f"Nota: {subject_grade}")
    print(f"Status: {status}")