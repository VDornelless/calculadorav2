'''
Trabalho Prático calculadora_v2
'''

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Não foi possível realizar a divisão por 0"
    return n1 / n2

def calculadora(n1, n2, sinal):
    if sinal in ["adicao", "adição", "mais", "+"]:
        return adicao(n1, n2)
    elif sinal in ["subtracao", "subtração", "menos", "-"]:
        return subtracao(n1, n2)
    elif sinal in ["multiplicacao", "multiplicação", "x", "*", "."]:
        return multiplicacao(n1, n2)
    elif sinal in ["divisao", "divisão", "/"]:
        return divisao(n1, n2)
    else:
        return "Operação inválida"

# Laço principal
saida = ""
while saida != "n":
    try:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
        sinal = input("Operação matemática: ").lower()
        resultado = calculadora(n1, n2, sinal)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")
    saida = input("Quer continuar? [S/N] ").lower()