"""
Exercício 2: Sistema de Login com Tupla (Tuple + IF/ELSE)
Objetivo: Usar a imutabilidade para segurança básica.
Crie uma tupla chamada admin_acesso que contém: ("admin", "12345").
Peça para o usuário digitar o usuario e a senha.

Lógica:
Se o usuario for igual ao primeiro item da tupla E a senha for igual ao segundo item, 
exiba "Acesso concedido!". Caso contrário, exiba "Login ou senha incorretos".
-------------------------------------------------------------------------------------------------------
"""

# Definição da tupla imutável (Credenciais de Sistema)
admin_acesso = ("admin", "12345")

# Captura de dados
# Nota: Não usamos .strip() ou .lower() na senha para manter a integridade exata do caractere
user_input = input("Usuário: ").strip().lower()
pass_input = input("Senha: ")

# Lógica de Acesso (Acesso direto aos índices da tupla)
if user_input == admin_acesso[0] and pass_input == admin_acesso[1]:
    print("\n[SUCESSO] Acesso concedido! Bem-vindo ao sistema.")
else:
    # Por segurança, não especificamos se o erro foi no usuário ou na senha
    print("\n[ERRO] Login ou senha incorretos.")