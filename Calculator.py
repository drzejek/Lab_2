from  AbstractCalculator import *

class Calculator(AbstractCalculator):
    def __init__(self):
        print("Calculator")

    def getValues(self, firstValue, secondValue):
        self.firstValue = firstValue
        self.secondValue = secondValue

    def getFunction(self, function):
        self.function = function
        self.degreeList = []
        for degree, coef in enumerate(reversed(self.function)):
            self.degreeList.append(degree)

        self.degreeList.reverse()

    def addValues(self):
        sum = self.firstValue + self.secondValue
        print(str(self.firstValue) + "+" + str(self.secondValue) + "=", end='')
        return sum

    def subValues(self):
        difference = self.firstValue - self.secondValue
        print(str(self.firstValue) + "-" + str(self.secondValue) + "=", end='')
        return difference

    def multipleValues(self):
        product = self.firstValue*self.secondValue
        print(str(self.firstValue) + "*" + str(self.secondValue) + "=", end='')
        return product

    def divideValues(self):
        try:
            quotient = self.firstValue/self.secondValue
            print(str(self.firstValue) + "/" + str(self.secondValue) + "=", end='')
            return quotient
        except ZeroDivisionError:
            print("Dzielenie przez - - niedozwolone")

    def __printFunction(self):
        for ix, coef in enumerate(self.function):
            if coef == 0:
                continue
            if self.degreeList[ix] == 1:
                print(str(coef) + "x", end=" + ")
            elif self.degreeList[ix] == 0:
                print(str(coef))
            else:
                print(str(coef) + "x^" + str(self.degreeList[ix]), end=" + ")

    def derivativeFunction(self):
        print("Funkcja:", end=' ')
        self.__printFunction()

        self.function.pop(-1)
        self.degreeList.pop(0)

        print("Pochodna: ", end=' ')
        self.__printFunction()
        return self.function
