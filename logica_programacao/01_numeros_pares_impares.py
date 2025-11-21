def verifica(numero): # Depois de conversar com Christian e Maria algumas vezes durante a semana resolvi tentar fazer o código sem imputs, passando o parâmetro já dentro da variável!
    if not isinstance(numero, int): # Aqui vai ser onde vamos evitar possíveis erros garantindo o que for digitado pelo usuário seja um número!
        raise TypeError("Digite um número inteiro, por gentileza!") # o raise vai servir pra sinalizar uma exceção quando não for um int digitado retornando uma mensagem de TypeError. Desse jeito o programa não finaliza automático no terminal!
    if numero % 2 == 0: # aqui ta declarado a variável que vai salvar a informação digitada pelo usuário. O % serve pra dividir e retornar o resto.
# Exemplo prático, se 10/2 = 5 resta 0, e como == 0 vai validar como true .. se fosse 7/2 = 3 restando 1, nesse caso é false
        return "Par!"
    else:
        return "Ímpar!"
# Tudo daqui pra cima é lógica de cálculo!
# Daqui pra baixo tá responsável pela interação com o usuário!   
if __name__ == "__main__": #Aqui foi algo que eu custei pra entender, mas parece que em Python eu tenho que passar que a variável é main pra executar o programa como principal se não da erro no terminal e os prints e inputs são ignorados
# é como se eu tivesse fazendo uma consulta dessa variável "dunder" que é diferente de uma variável criada. E aparentemente é essa variável que permite os testes serem possíveis!
    try: # o try trata os possíveis erros de digitação do usuário
        entrada_usuario = int(input("Digite um número: ")) # Aqui pedimos a entrada do usuário já convertendo ela para inteiro
        resultado = verifica(entrada_usuario) #Aqui a gente pega o que o usuário digitou e chama a função verifica que eu criei com a lógica imbutida
        print(f"O número {entrada_usuario} é: {resultado}") # E aqui a gente printa na tela o resultado com ajuda do "f" que faz possível a gente colocar a variável dentro da string nessa resposta
    except ValueError: # Aqui nessa exceção se o usuário digitar letras vai retornar a mensagem abaixo
        print("Por favor, digite um número inteiro!") # mensagem de erro solicitando pra digitar núme
    except TypeError as e: # já nessa exceção caso o usuário digite um número flutuante 5.1 , 4.3 etc.. ele não aceita e pede o inteiro.
        print(f"Erro: {e}") 

