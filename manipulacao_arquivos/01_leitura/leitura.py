nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print("\n--- Conteúdo do arquivo --- ")
        print(conteudo)
        
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
except Exception as e:
    print("Ocorreu um erro ao tentar ler o arquivo: ", e)
