"""
Exercício 3: Verificador de Clube (Set + IF/ELIF)
Objetivo: Usar conjuntos para verificar permissões únicas.
Crie um Set chamado convidados_vip com 4 nomes de sua escolha.
Peça para o usuário digitar o seu nome.

Lógica:
Se o nome estiver no Set, exiba "Bem-vindo à área VIP!".
Se o nome for "Dono", exiba "Bem-vindo, chefe!".
Para qualquer outro nome, exiba "Acesso apenas com convite".
-------------------------------------------------------------------------------------------------------
"""

# Definição do conjunto de convidados (Set - garante unicidade e busca rápida)
convidados_vip = {"Michel", "Junior", "Ana", "Beatriz"}

# Captura e normalização do nome (Remoção de espaços e capitalização padrão)
nome_usuario = input("Digite seu nome para verificação: ").strip().title()

# Lógica de Permissões (Hierarquia de Acesso)
if nome_usuario == "Dono":
    print(f"\n[MASTER] Bem-vindo, chefe!")

elif nome_usuario in convidados_vip:
    print(f"\n[VIP] Bem-vindo à área VIP, {nome_usuario}!")

else:
    print("\n[NEGADO] Acesso apenas com convite. Por favor, dirija-se à bilheteria.")