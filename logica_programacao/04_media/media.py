numeros = input("Digite números separados por espaço para calcular a média: ") # salva na variável numeros o que o usuário vai digitar, que no caso são números separados por espaço!

lista = numeros.split() # Aqui o .spĺit tem como funcionalidade quebrar a string dos números digitados acima e transforma em uma lista.
lista = [float(num) for num in lista] # Através do float convertemos cada item dessa lista recém criada de string para número float.

media = sum(lista) / len(lista) # Soma recebe a lista e soma todos números que estiverem dentro e em seguida divide pela quatidade de itens dentro da lista.

print(f"A média dos números é: {media}") # Por fim, printa na tela a média calculada.
