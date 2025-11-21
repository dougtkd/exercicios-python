import unittest # Sinceramente não sei se é o ideal mas foi a forma mais eficiente que eu achei pesquisando na documentação e principalmente no youtube como fazer testes em python, que é importando essa biblioteca.
from exercicio_01 import verifica # aqui a gente importa a função que eu criei no arquivo principal

class TestVerifica(unittest.TestCase): # Essa classe serve pra definir o grupo de teste abaixo chamando o módulo unittest que foi importado.
    
    def test_numeros_pares(self): # um erro comum que eu estava comentando aqui era escolher o nome do método com o "test" no final causando erro, descobri na marra que é preciso colocar o "test" no começo do nome do método.
        resultado = verifica(4) # aqui chama a função verifica e atribui o 4 nela
        self.assertEqual(resultado, "Par!") # essa verificação que é o pulo do gato, o assert obriga que o resultado precisa ser igual à intring que foi passada como parâmetro ali dentro. Diferente disso vai dar FAIL

    def test_numeros_impares(self): # aqui segue o padrão do primeiro teste só que retorna Ímpar
        self.assertEqual(verifica(7), "Ímpar!") # O que mudou nessa linha para o teste acima foi simplificado com a função sendo chamada diretamente dentro da asserção. Eu pesquisei a respeito e as duas formas estão corretas
# No vídeo que eu assisti explicando o uso da biblioteca unittest o cara não especifica o pq, mas pelo pouco que li na internet é uma questão de boas práticas.        

    def test_entrada_invalida(self): # Terceiro teste que trata a exceção da função!
        with self.assertRaises(TypeError): # Nesse caso o teste deve chamar o TypeError quando for verificado ser um texto.
            verifica("texto") 

if __name__ == '__main__':
    unittest.main()

# O segundo e o terceiro testes estavam retornando FAIL no terminal e era somente porque estava faltando a exclamação no parâmetro dos testes kkk
