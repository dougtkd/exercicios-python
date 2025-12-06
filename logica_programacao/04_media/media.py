def calcular_media(lista): # Pensando nos testes unitários atualizamos o código  declarando a função calcular_media que recebe a lista.
    if len(lista) == 0: # Esse if faz a verificação se a lista está vazia retornando a quantidade dos elementos dentro da mesma.
        raise ValueError("A lista não pode estar vazia.") # Logo, se a lista estiver vazia chamamos a exceção ValueError recebendo uma mensagem para o usuário explicando que a lista precisa receber números.
    return sum(lista) / len(lista) # retorna a soma dos itens da lista e divide pela quantidade de itens dentro da mesma!

if __name__ == "__main__": # Essa linha é um pouco confusa pra mim, mas eu li que é uma boa prática fazer essa verificação do arquivo se está sendo executado diretamente no terminal e não importado por algu módulo. Resumindo,todo código dentro desse if só vai rodar se o arquivo for o script principal do rolê, possibilitando a gente fazer testes unitários.
    numeros = input("Digite números separados por espaço para calcular a média: ") # Através do imput pede pro usuário digite uma linha de texto separada por espaços, e seu valor é salvo na variavel numeros.
    
    lista = numeros.split() # Aqui o .spĺit tem como funcionalidade quebrar a string dos números digitados acima e transforma em uma lista.
    lista = [float(num) for num in lista] # Através do float convertemos cada item dessa lista recém criada de string para número float.

    media = sum(lista) / len(lista) # Soma recebe a lista e soma todos números que estiverem dentro e em seguida divide pela quatidade de itens dentro da lista.

    print(f"A média dos números é: {media}") # Por fim, printa na tela a média calculada.
