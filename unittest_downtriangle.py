import unittest
from downtriangle import downtriangle

class tester (unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, downtriangle(0))
    def test_2(self):
        self.assertEqual(0, downtriangle(1))
    def test_3(self):
        self.assertEqual(0, downtriangle(2))
        self.assertEqual(0, downtriangle(3))
        self.assertEqual(0, downtriangle(4))
        self.assertEqual(0, downtriangle(5))
        self.assertEqual(0, downtriangle(6))
        self.assertEqual(0, downtriangle(7))
    def test_4(self):
        self.assertEqual(0, downtriangle(8))
        self.assertEqual(0, downtriangle(9))
        self.assertEqual(0, downtriangle(10))

if __name__ == "__main__":
    unittest.main()
