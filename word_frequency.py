"""
2. Dicionário de Frequência de Palavras (Dict):
Peça uma frase ao usuário. Crie um dicionário que conte a frequência 
de palavras específicas fornecidas pelo usuário sem usar loops.
-------------------------------------------------------------------------------------------------------
"""

raw_phrase = input("Digite uma frase: ").strip().lower()

if not raw_phrase: # raw_phrase is empty, ou raw_phrase is None
    print("Erro: A frase não pode estar vazia.")
else:
    words = raw_phrase.split()

    # Como não usamos loops, pedimos as palavras alvo para análise
    target = input("Qual palavra deseja contar na frase? ").strip().lower()
    
    # Criamos o dicionário usando o método .count() da lista
    frequency = {target: words.count(target)}
    
    print(f"\nResultado da análise: {frequency}")