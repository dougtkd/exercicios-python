import unittest
from potencia import calcular_potencia

class TestCalcularPotencia(unittest.TestCase):

    def test_potencia_positiva(self):
        self.assertEqual(calcular_potencia(2, 3), 8)

    def test_potencia_zero(self):
        self.assertEqual(calcular_potencia(5, 0), 1)

    def test_potencia_base_zero(self):
        self.assertEqual(calcular_potencia(0, 5), 0)

    def test_potencia_float(self):
        self.assertAlmostEqual(calcular_potencia(2.5, 2), 6.25)

if __name__ == "__main__":
    unittest.main()
