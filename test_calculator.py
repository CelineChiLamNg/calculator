import unittest
from calculator import Calculator

# only TestCase is used but unittest framework has other classes
# my class "TestCalculator" is a child class of TestCase
# which allows me to have access to methods like self.assertEqual...
class TestCalculator(unittest.TestCase):
    def test_memory(self):
        calc = Calculator()    # creating a new calc instance in every test
        calc.memory = 10
        self.assertEqual(calc.memory, 10)    # compare calc.memory is the correct value

    def test_addition(self):
        calc = Calculator()
        calc.addition(5)
        self.assertEqual(calc.memory, 5)

    def test_subtraction(self):
        calc = Calculator()
        calc.memory = 4
        calc.subtraction(2)
        self.assertEqual(calc.memory, 2)

    def test_multiplication(self):
        calc = Calculator()
        calc.memory = 1.5
        calc.multiplication(2)
        self.assertEqual(calc.memory, 3)

    def test_division(self):
        calc = Calculator()
        calc.memory = 20
        calc.division(2)
        self.assertEqual(calc.memory, 10)
        self.assertEqual(calc.division(0), "Error: Division by zero")    # comment is a returned value, not in memory

    def test_root(self):
        calc = Calculator()
        calc.memory = 16
        calc.root(2)
        self.assertEqual(calc.memory, 4)
        self.assertEqual(calc.root(0), "Error: Root index cannot be zero")

    def test_reset(self):
        calc = Calculator()
        calc.memory = 100
        calc.reset()
        self.assertEqual(calc.memory, 0)


if __name__ == '__main__':
    unittest.main()
