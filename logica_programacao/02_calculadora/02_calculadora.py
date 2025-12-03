def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calcular(operacao, a, b):
    if operacao == "soma":
        return soma(a, b)
    elif operacao == "subtracao":
        return subtracao(a, b)
    elif operacao == "multiplicacao":
        return multiplicacao(a, b)
    elif operacao == "divisao":
        return divisao(a, b)
    else:
        return "Operação inválida"

print(calcular("soma", 2, 52))
