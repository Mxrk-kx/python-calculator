import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(3, 2), 5)

    # Add the following test methods to the TestCalculator class:
    def test_substract(self):
        self.assertEqual(self.calc.subtract(2,1), 1)
    def test_substract2(self):
        self.assertEqual(self.calc.subtract(5,3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,5), 10)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(5,5), 25)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2), 5)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(12,2), 6)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5,7), 5)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10,3), 1)
    
    
    

if __name__ == '__main__':
    unittest.main()