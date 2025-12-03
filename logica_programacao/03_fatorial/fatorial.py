def fatorial(n): # definida a função que recebe o número
    if n < 0: # nessa linha a gente determina se o número for menor que zero vai retornar um erro!
        return "Erro!"

    resultado = 1 # determinamos o valor base do resultado que precisa ser 1
    for i in range(1, n + 1): # aqui a gente gera nossa sequência, para cada vez que o i for chamado ele recebe o valor de 1 até n
        resultado = resultado * i # aqui o resultado recebe ele mesmo multiplicado por i

    return resultado # sendo assim retorna o resultado final

if __name__ == "__main__": # padrão do python pra chamar a função quando a gente roda diretamente no terminal
    numero = int(input("Digite um número para calcular o fatorial: ")) # input com mensagem para o usuário digitar um número
    print(f"O fatorial de {numero} é {fatorial(numero)}") # Por fim printado na tela o fatorial já multiplicado
