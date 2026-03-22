"""
DESAFIO: O Protocolo "Sentinela de Dados"
Cenário: Lógica de um cofre digital de altíssima segurança.
Objetivo: Validar acesso usando Sets, Tuplas, Dicionários e lógica booleana.
-------------------------------------------------------------------------------------------------------
"""

# 1. Preparação dos Dados (Contexto do Sistema)
usuarios_bloqueados = {"hackerman", "dr_evil", "py_robot"}
funcionarios_ativos = ("ana_gerente", "bruno_tech", "carla_diretora")
chaves_biometricas = {"setor_a": "digital_ok", "setor_b": "iris_ok"}

# Tentativa atual (Entrada de Dados)
usuario = input("Digite o nome de usuário: ").strip().lower()
cargo = input("Digite o cargo (gerente, tecnico, estagiario): ").strip().lower()
possui_cartao = True  # Simulação de sensor
senha_mestra = "Python2024"

# Entrada da senha para validação
tentativa_senha = input("Digite a senha mestra ou pressione Enter se usar o cartão: ")

# --- LÓGICA DE VALIDAÇÃO (Bloco Único IF/ELIF/ELSE) ---

# REGRA 4: Bloqueio de Estagiário (Prioridade de negação)
if cargo == "estagiario":
    print("\n⚠️  Acesso negado: Estagiários não possuem nível de acesso ao cofre.")

# REGRA 1: Segurança de Lista Negra
elif usuario in usuarios_bloqueados:
    print("\n🚫 ALARME ACIONADO: Usuário na lista de restrição!")

# REGRA 2, 3 e 5: Verificação de Hierarquia, Múltiplos Fatores e Integridade
elif (usuario in funcionarios_ativos and 
      (possui_cartao or tentativa_senha == senha_mestra) and 
      chaves_biometricas.get("setor_a") == "digital_ok"):
    
    # Se todas as condições acima forem True, o acesso é concedido
    print(f"\n🔓 ACESSO LIBERADO. Bem-vindo, {usuario.title()}!")

# REGRA 6: Qualquer outro erro (Credenciais inválidas ou erro de biometria)
else:
    print("\n❌ ACESSO NEGADO: Credenciais inválidas ou erro de biometria.")