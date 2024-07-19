import unittest
import math
from geometria import area_circulo, area_retangulo

## adicionando erro ao cod para reproduzir cenário 2 (erro de build)
class TesteGeometria(unittest.TestCasa):
    def teste_area_circulo(self):
        self.assertAlmostEqual(area_circulo(1), math.pi, places=2)
        self.assertAlmostEqual(area_circulo(0), 0, places=2)
        self.assertRaises(ValueError, area_circulo, -1)

    def teste_area_retangulo(self):
        self.assertEqual(area_retangulo(2, 3), 6)
        self.assertEqual(area_retangulo(0, 5), 0)
        self.assertRaises(ValueError, area_retangulo, -2, 3)
        self.assertRaises(ValueError, area_retangulo, 2, -3)

if __name__ == '__main__':
    unittest.main()
