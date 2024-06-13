# test_meu_codigo.py
import unittest
from meu import soma, subtracao, multiplicacao


class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(3, 5), 8)

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 2), 8)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(4, 5), 20)


if __name__ == "__main__":
    unittest.main()
