import unittest # Importa a biblioteca Unittest que é padrão do Python
from media import calcular_media # Aqui importamos a função calcular_media do arquivo media.py que está salvo no mesmo diretório do arquivo de teste!

class TestCalcularMedia(unittest.TestCase): # Aqui a gente cria a calsse de teste que recebe o testcase do unittest, que nos fornece todos os métodos dessa biblioteca pra gente brincar.

    def test_media_numeros(self): # Aqui a gente faz o primeiro teste, que simplesmente vai testar a média de números positivos inteiros. Vale reforçar que todo método criado dentro do TestCase que comece com "test" automaticamente executa o unittest!
        self.assertEqual(calcular_media([10, 20, 30]), 20) # Verifica que se os parâmetros passados não forem iguais o teste falha. sendo A a lista passada e B = 20.. a média de A tem q ser igual a 20 pra dar true.

    def test_media_numeros_decimais(self): # Já aqui a gente faz o teste de números decimais (float)
        self.assertAlmostEqual(calcular_media([1.5, 2.5, 3.0]), 7/3) # Na verificação de A e B nesse teste existe uma tolerância que nesse exemplo é de 7. E diferente dos outros, quando se trata de float tem q usar o Almost por conta da diferença na precisão dos números flutuantes

    def test_media_lista_um_elemento(self): # Teste o limite da lista com somente um elemento!
        self.assertEqual(calcular_media([42]), 42) # Verifica que na lista com o elemento X a média seja X. Rápido, simples e prático.

    def test_media_lista_vazia(self): # Aqui já testamos a lista vazia.
        with self.assertRaises(ValueError): # todo código dentro do with se não apresentar o ValueError vai falhar. Pra dar true ele tem que apresentar o ValueError! Uma questão de validação do comportamento da lista evitando dividir por zero!
            calcular_media([]) # Se calcular a média aprensentar ValueError o contexto salva e o teste da true. Qualquer comportamento diferente vai de F

if __name__ == "__main__": # Novamente, essa linha funciona somente quando o arquivo de teste é executando diretamente no terminal.
    unittest.main() # Chama o unittest que por sua vez procura automaticamente e roda todos métodos de testes herdado do TestCase.. e rezar pra dar certo, amém.
