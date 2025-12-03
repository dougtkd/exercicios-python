import unittest # importando a biblioteca de teste do python
from fatorial import fatorial # importando as funções do programa fatorial

class TestFatorial(unittest.TestCase): # classe de teste que chama o método unittest onde qualquer função que comece com test_ será executada como teste automaticamente.

    def test_fatorial_zero(self): # essa e todas as funções asbaixo representam os testes unitários que vamos fazer onde o self e obrigatório para o funcionanemto do código
        self.assertEqual(fatorial(0), 1) # aqui é onde a comparação acontece como argumento e o processo se repete em todos os testes

    def test_fatorial_um(self):
        self.assertEqual(fatorial(1), 1)

    def test_fatorial_positivo(self):
        self.assertEqual(fatorial(5), 120)

    def test_fatorial_negativo(self):
        self.assertEqual(fatorial(-3), "Erro!")

    def test_fatorial_numero_grande(self):
        self.assertEqual(fatorial(6), 720)

if __name__ == "__main__": # Esse bloco faz a checagem de execução do programa, que caso for executado diratamente no terminal o teste ele rodará automaticamente.
    unittest.main()        # Chama o runner automáticamente do uittest!
