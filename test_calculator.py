import unittest
import mock
import math
from Calculator import Calculator
from Exceptions import *

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addValues(self):
        firstValue = 3
        secondValue = 2
        expectValue = 5

        self.assertEqual(self.calculator.addValues(firstValue, secondValue), expectValue)

    def test_subValues(self):
        firstValue = 6
        secondValue = 2
        expectValue = 4

        self.assertEqual(self.calculator.subValues(firstValue, secondValue), expectValue)

    def test_subValuesString(self):
        firstValue = "2"
        secondValue = "2"
        self.assertRaises(NotANumberException, self.calculator.subValues, firstValue, secondValue)

    def test_multipleValues(self):
        firstValue = 3.0
        secondValue = 2.0
        expectValue = 6.0

        self.assertEqual(self.calculator.multipleValues(firstValue, secondValue), expectValue)

    def test_divideValues(self):
        firstValue = 8.0
        secondValue = 4.0
        expectValue = 2.0

        self.assertEqual(self.calculator.divideValues(firstValue, secondValue), expectValue)


    def test_divideValueByZero(self):
        firstValue = 5
        secondValue = 0
        self.assertRaises(DivisionByZeroException, self.calculator.divideValues, firstValue, secondValue)

    def __func(self, x):
        return 3 * x ** 2 + 2 * x + 2


    def test_derivativeNotFunction(self):
        x = 1.0
        func = "2*x"
        dx = 0.1
        self.assertRaises(NotAFunction, self.calculator.derivativeFunction, func, x, dx)

    @mock.patch("Calculator.Calculator.derivativeFunction", return_value = 7.999999999994678)
    def test_derivativeFunction(self, mock_value):
        x = 1.0
        dx = 1e-4
        expectedValue = 7.999999999994678
        self.assertEqual(self.calculator.derivativeFunction(self.__func, x, dx), expectedValue)

if __name__ == '__main__':
    unittest.main()