from abc import ABCMeta, abstractmethod

class AbstractCalculator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getValues(self, firstValue, secondValue):
        pass

    @abstractmethod
    def getFunction(self, function):
        pass

    @abstractmethod
    def addValues(self):
        pass

    @abstractmethod
    def subValues(self):
        pass

    @abstractmethod
    def multipleValues(self):
        pass

    @abstractmethod
    def divideValues(self):
        pass

    @abstractmethod
    def derivativeFunction(self):
        pass
