from unittest import TestCase
from  Calculator import *

class TestCalculator(TestCase):
    def test_addValues(self):
        calc = Calculator()
        firstValue = 3.0
        secondValue = 2.0
        expectValue = 5.0
        calc.getValues(firstValue, secondValue)

        self.assertEqual(calc.addValues(), expectValue)

    def test_subValues(self):
        calc = Calculator()
        firstValue = 6.0
        secondValue = 2.0
        expectValue = 4.0
        calc.getValues(firstValue, secondValue)

        self.assertEqual(calc.subValues(), expectValue)

    def test_multipleValues(self):
        calc = Calculator()
        firstValue = 3
        secondValue = 2
        expectValue = 6
        calc.getValues(firstValue, secondValue)

        self.assertEqual(calc.multipleValues(), expectValue)

    def test_divideValues(self):
        calc = Calculator()
        firstValue = 8
        secondValue = 4
        expectValue = 2
        calc.getValues(firstValue, secondValue)

        self.assertEqual(calc.divideValues(), expectValue)

    def test_derivativeFunction(self):
        self.fail()


if __name__ == '__main__':
    test = TestCalculator()
    test.test_addValues()
    test.test_subValues()
    test.test_multipleValues()
    test.test_divideValues()