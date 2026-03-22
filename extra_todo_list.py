"""
Exercício 1: Gerenciador de Lista de Tarefas (List + IF)
Objetivo: Praticar busca e existência em listas.
Crie uma lista chamada tarefas com: "Estudar Python", "Limpar quarto", "Fazer exercícios".
Peça para o usuário digitar uma nova tarefa.
Lógica: Se a tarefa já estiver na lista (use o operador in), exiba "Essa tarefa já existe!".
Caso contrário, adicione-a à lista com .append() e exiba a lista atualizada.
-------------------------------------------------------------------------------------------------------
"""

try:
    tasks = ["Estudar Python", "Limpar quarto", "Fazer exercícios"]

    user_input = input("Digite uma nova tarefa: ").strip()

    # Robust validations (edge cases)
    if not user_input:
        print("Erro: A tarefa não pode ser vazia.")
    elif not isinstance(user_input, str):
        print("Erro: Entrada inválida.")
    else:
        # Normalize to avoid duplicates caused by case or spaces
        normalized_tasks = list(map(lambda t: t.lower().strip(), tasks))
        normalized_input = user_input.lower()

        if normalized_input in normalized_tasks:
            print("Essa tarefa já existe!")
        else:
            tasks.append(user_input.strip())
            print(f"\nLista atualizada: {tasks}")

except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as e:
    print(f"Erro inesperado: {e}")