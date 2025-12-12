nome_arquivo = input("Digite o nome do arquivo: ") # Aqui a gente cria a variável nome_arquivo que salva através do input o que for digitado pelo usuário.

try: # o try serve para iniciar blocos de exceções. É como que tudo que tiver abaixo dele será executado normalmente. Mas se tiver algo diferente fora do esperado é chamado o bloco de except.
    with open(nome_arquivo, "r") as arquivo: # aqui gerenciamos através do with que o arquivo seja aberto no modo de leitura "r" e salva o file object no arquivo!
        conteudo = arquivo.read() # aqui é onde a gente passa a instrução de leitura do arquivo.. e retorna uma string com tudo que está dentro dele.
        print("\n--- Conteúdo do arquivo --- ") # Então printamos na tela esse título com espaçamento através do \n .. é algo exclusivamente visual pra ficar mais bonito e performático, ou não kkk
        print(conteudo) # por fim, printamos abaixo o conteúdo do arquivo.
        
except FileNotFoundError: # Aqui é o primeiro bloco de exceção para caso seja digitado um arquivo inexistente pelo usuário.
    print("Erro: arquivo não encontrado!") # Logo, é printado na tela a mensage de erro.
except Exception as e: # E por fim, esse bloco captura qualquer exceção que não tenha sido tratada nos passos anteriores. o Exception é uma classe padrão para exceções e através do as e a gente vincula a exceção na variável "e" para inspeção!
    print("Ocorreu um erro ao tentar ler o arquivo: ", e) # printamos a mensagem de erro dessa exceção e mostra o conteúdo que foi salvo na variável.
