# test_math_operations.py

import unittest
from src.math_operations import addition, soustraction, multiplication, division

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)
        self.assertEqual(soustraction(3, 5), -2)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(6, 2), 3)
        self.assertEqual(division(7, 2), 3.5)
        with self.assertRaises(ValueError):
            division(7, 0)

if __name__ == "__main__":
    unittest.main()
