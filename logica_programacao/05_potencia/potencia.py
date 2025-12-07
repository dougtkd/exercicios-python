def calcular_potencia(base, expoente): # Aqui declaro a função calcular_potencia que recebe coma parâmetro base e expoente!
    return base ** expoente # retorna o cálculo da potência com o operador ** chamando assim, o resultado.

if __name__ == "__main__": # Aqui a variável __name__ recebe main, isso permite que o código seja executado diretamente no terminal.
    base = float(input("Digite a base da potência: ")) # Pede para o usuário digitar retornando uma string que vai ser convertida em um número float.
    expoente = float(input("Digite o expoente: ")) # Mesma lógica da linha de cima!

    resultado = calcular_potencia(base, expoente) # Chamamos a função calcular_potencia passando as variaveis e salvando o resultado.

    print(f"{base} elevado a {expoente} é = {resultado}") # retorna o resultado do cálculo de potência com f-string visando interpolar as variáveis.
