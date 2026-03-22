"""
3. Registro de Notas Imutável (Tuple & Dict):
Armazene o nome de 2 alunos e 2 notas para cada um. As notas devem ser 
guardadas em uma Tuple (imutável) dentro de um Dicionário.
Calcule a média e exiba o status (Média >= 7).
-------------------------------------------------------------------------------------------------------
"""

try:
    # Aluno 1
    name1 = input("Nome do Aluno 1: ").strip()
    grade1_a = float(input(f"Nota A de {name1}: ").replace(",", "."))
    grade1_b = float(input(f"Nota B de {name1}: ").replace(",", "."))

    # Aluno 2
    name2 = input("Nome do Aluno 2: ").strip()
    grade2_a = float(input(f"Nota A de {name2}: ").replace(",", "."))
    grade2_b = float(input(f"Nota B de {name2}: ").replace(",", "."))

    # Estrutura: Chave (String) -> Valor (Tuple)
    school_records = {
        name1: (grade1_a, grade1_b),
        name2: (grade2_a, grade2_b)
    }

    # Processamento manual (sem loops)
    avg1 = sum(school_records[name1]) / 2
    avg2 = sum(school_records[name2]) / 2

    print(f"\n{name1} | Média: {avg1:.2f} | {'Aprovado' if avg1 >= 7 else 'Reprovado'}")
    print(f"{name2} | Média: {avg2:.2f} | {'Aprovado' if avg2 >= 7 else 'Reprovado'}")

except ValueError:
    print("Erro: Insira valores numéricos válidos para as notas.")