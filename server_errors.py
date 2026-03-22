"""
5. Tradutor de Códigos de Erro (Dict):
Dicionário fixo com códigos de erro. Se o usuário digitar um código 
inexistente, permita que ele adicione a descrição ao sistema.
-------------------------------------------------------------------------------------------------------
"""

error_log = {
    "404": "Not Found",
    "500": "Internal Server Error",
    "403": "Forbidden"
}

search_code = input("Digite o código de erro (ex: 404): ").strip()

# Guard Clause usando .get()
error_message = error_log.get(search_code)

if error_message:
    print(f"Descrição: {error_message}")
else:
    print("Código não encontrado no sistema.")
    new_description = input(f"Defina a mensagem para o código {search_code}: ").strip()
    error_log[search_code] = new_description
    print(f"Sucesso: Erro {search_code} registrado como '{new_description}'.")