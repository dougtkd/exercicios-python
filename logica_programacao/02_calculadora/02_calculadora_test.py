import unittest # aqui importamos essa biblioteca de testes do python que nos garante vários recursos legais para testes unitários
from calculadora import soma, subtracao, multiplicacao, divisao, calcular # Já aqui a gente importa as funcoes que vão ser testada do programa

class TestCalculo(unittest.TestCase): # de acordo com o documento do unittest a gente tem que chamar o Testcase numa calsse de teste, se não vai dar ruim!

    def test_soma(self): # Estamos definindo o teste aqui e em todos que comecem com "test" vai funcionar por padrão e rodar o teste, por conta do unittest que importamos na primeira linha
        self.assertEqual(soma(2, 8), 10) # Chamando a soma e testando, se estiver errado retorna erro!

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 4), 6) # Chamando a soma e testando.

    def test_multiplicaco(self):
        self.assertEqual(multiplicacao(2, 5), 10) # Chamando a multiplicação e testando.

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2) # Chamando a divisão e testando.

    def test_divisao_zero(self): # Aqui fazemos o teste em caso de divisão por zero!
        self.assertEqual(divisao(10, 0), "Erro: divisão por zero!")

if __name__ == "__main__": # Essa linha faz uma verificação no arquivo executado para depois iniciar os testes
    unittest.main()
