'''
Microatividade 3: Descrever a utilização da
estrutura de repetição while em Python
'''
entrada_idade = ""

while str(entrada_idade) != "0":
    entrada_idade = input("Digite um número qualquer ou 0 para sair: ")
    print(f"Número digitado: {entrada_idade}")