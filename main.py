import os
import sys
import subprocess

# Cores ANSI para o terminal
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"

def clear_screen():
    """
        Funcao para limpar o ecrã
    """
    # Limpa o ecrã
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Caminho do interpretador python atual para garantir que funciona em qualquer PC
    python_cmd = sys.executable

    while True:
        clear_screen()
        print(f"{YELLOW}{'='*50}{RESET}")
        print(f"{BOLD}{CYAN}{' MAIN HUB - SecondExerciseList ' : ^50}{RESET}")
        print(f"{BOLD}{CYAN}{' Menu de Exercícios ' : ^50}{RESET}")
        print(f"{YELLOW}{'='*50}{RESET}")
        
        # Lista de opções coloridas
        print(f"{GREEN}1.  {RESET}Desafio: Sentinela de Dados")
        print(f"{GREEN}2.  {RESET}Sistema de Candidatos (Sets)")
        print(f"{GREEN}3.  {RESET}Validador de Coordenadas")
        print(f"{GREEN}4.  {RESET}Otimizador de Entregas")
        print(f"{GREEN}5.  {RESET}Verificador de Acesso ao Clube")
        print(f"{GREEN}6.  {RESET}Classificador de Notas")
        print(f"{GREEN}7.  {RESET}Sistema de Login (Tuplas)")
        print(f"{GREEN}8.  {RESET}Lista de Tarefas")
        print(f"{GREEN}9.  {RESET}Gestor de Inventário")
        print(f"{GREEN}10. {RESET}Histórico de Preços")
        print(f"{GREEN}11. {RESET}Ranking de Scores")
        print(f"{GREEN}12. {RESET}Analisador de Erros de Servidor")
        print(f"{GREEN}13. {RESET}Registos de Alunos")
        print(f"{GREEN}14. {RESET}Agrupamento de Tarefas")
        print(f"{GREEN}15. {RESET}Contador de Frequência de Palavras")
        
        print(f"{YELLOW}{'-' * 50}{RESET}")
        print(f"{RED}{BOLD}0.  SAIR{RESET}")
        print(f"{YELLOW}{'-' * 50}{RESET}")

        choice = input(f"{BOLD}Escolha uma opção para executar: {RESET}").strip()

        # Dicionário que mapeia a escolha ao nome do ficheiro real na tua pasta
        scripts = {
            "1": "1. challenge.py",
            "2": "candidate_sets.py",
            "3": "coordinate_validator.py",
            "4": "delivery_optimizer.py",
            "5": "extra_club_verificator.py",
            "6": "extra_grade_classifier.py",
            "7": "extra_login_tuple.py",
            "8": "extra_todo_list.py",
            "9": "inventory_manager.py",
            "10": "price_history.py",
            "11": "score_ranking.py",
            "12": "server_errors.py",
            "13": "student_records.py",
            "14": "task_grouping.py",
            "15": "word_frequency.py"
        }

        if choice == "0":
            print(f"\n{BOLD}{GREEN}A encerrar o programa... Até à próxima!{RESET}")
            break
        
        elif choice in scripts:
            script_path = scripts[choice]
            print(f"\n{MAGENTA}--- A EXECUTAR: {script_path} ---{RESET}\n")
            
            # Executa o ficheiro como um processo separado usando subprocess para evitar erros com espaços nos caminhos
            try:
                subprocess.run([python_cmd, script_path], check=True)
            except subprocess.CalledProcessError:
                print(f"\n{RED}Ocorreu um erro ao executar o script.{RESET}")
            except Exception as e:
                print(f"\n{RED}Erro inesperado: {e}{RESET}")

            print(f"\n{YELLOW}{'-'*50}{RESET}")
            input(f"\n{BOLD}Exercício terminado. Pressione ENTER para voltar ao menu...{RESET}")
        
        else:
            print(f"\n{RED}Opção inválida! Tente novamente.{RESET}")
            input(f"\n{BOLD}Pressione ENTER...{RESET}")

if __name__ == "__main__":
    main()
