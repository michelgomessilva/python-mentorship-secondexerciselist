"""
8. Agrupamento por Categoria (Dict & List):
Crie um dicionário onde as chaves são prioridades e os valores são listas de tarefas.
Adicione uma tarefa à categoria correta.
-------------------------------------------------------------------------------------------------------
"""

tasks_by_priority = {
    "Alta": ["Ficheiro Main", "Backup"],
    "Média": ["Reunião"],
    "Baixa": ["Limpar Emails"]
}

new_task = input("Nome da nova tarefa: ").strip()
priority = input("Prioridade (Alta/Média/Baixa): ").strip().capitalize()

# Guard Clause para verificar validade da chave
if priority in tasks_by_priority:
    tasks_by_priority[priority].append(new_task)
    print(f"\nTarefa '{new_task}' adicionada com sucesso!")
    print(f"Estado atual: {tasks_by_priority}")
else:
    print("Erro: Prioridade inválida. Escolha entre Alta, Média ou Baixa.")