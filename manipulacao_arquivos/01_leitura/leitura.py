def ler_arquivo(nome_arquivo): # Definimos a função ler_arquivo que recebe como parâmetro nome_arquivo
    try: # Aqui damos início ao bloco de exceções.. qualquer coisa que retornar diferente do que está sendo passado dentro do try, chama o bloco except
        with open(nome_arquivo, "r") as arquivo: # li a respeito e o with garante que o arquivo vai ser fechado automaticamente quando sair do bloco. e o open abre o arquivo em modo de leitura  "r", e o as guarda o objeto file dentro de arquivo
            return arquivo.read() # aqui retorna o arquivo que vai ser todo lido 
            
    except FileNotFoundError: # aqui capturamos a exceção saindo do bloco try, quando o usuário digita algum arquivo que não existe.
        return "Erro: Arquivo inexistente!" # retornamos a mensagem que o arquivo não existe!
    except Exception as e:  # Segunda exceção: aqui é para casos não previstos. Onde Exception é uma classe padrão para exceções e o as salva essa exceção não prevista no "e".
        return f"Erro desconhecido: {e}" # retorna uma string que contém a exceção salva no "e".

if __name__ == "__main__": # esse if é padrão quando queremos rodar o código diretamente no terminal, ou seja.. main "importante quando queremos fazer testes unitários"
    nome_arquivo = input("Digite o nome do arquivo: ") # salva na variável nome_arquivo o input do usuário
    resultado = ler_arquivo(nome_arquivo) # chamamos a função ler_arquivo que recebe o input do usuário e guardamos dentro de resultado

    print("\n--- Conteúdo do arquivo ---") # meramente estético, \n faz o espaçamento quebrando a linha.
    print(resultado) # Por fim, imprimos na tela o resultado!
