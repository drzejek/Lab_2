from AbstractCalculator import *
from Functions import *
from scipy.misc import derivative

class Calculator(AbstractCalculator):
    def __init__(self):
        pass

    def addValues(self, firstVal, secondVal):
        isArgumentNumber(firstVal)
        isArgumentNumber(secondVal)

        return firstVal + secondVal

    def subValues(self, firstVal, secondVal):
        isArgumentNumber(firstVal)
        isArgumentNumber(secondVal)

        return firstVal - secondVal

    def multipleValues(self, firstVal, secondVal):
        isArgumentNumber(firstVal)
        isArgumentNumber(secondVal)

        product = firstVal * secondVal
        return product

    def divideValues(self, firstVal, secondVal):
        isArgumentNumber(firstVal)
        isArgumentNumber(secondVal)
        isDivisionByZero(secondVal)

        return firstVal/secondVal

    def derivativeFunction(self, function, x0, dx):
        isAFunction(function)
        isArgumentNumber(x0)
        isNumberNegative(x0)
        isFloatInstance(dx)

        return derivative(function, x0, dx)