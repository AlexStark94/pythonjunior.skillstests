import unittest
from words import test

class tester (unittest.TestCase):
    def test_1(self):
        self.assertEqual(['Hello', 'happy', 'nothing', 'dollar', 'unity', 'freelance', 'Android'], test('Texto.txt'))
    def test_2(self):
        self.assertEqual(['arbol', 'materia', 'papel'], test('lineas.txt'))
    def test_3(self):
        self.assertEqual(['nunca', 'jamas', 'hasta', 'felicidad', 'porque'], test('palabras.txt'))


if __name__ == "__main__":
    unittest.main()
