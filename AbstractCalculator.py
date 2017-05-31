from abc import ABCMeta, abstractmethod

class AbstractCalculator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def addValues(self, firstVal, secondVal):
        pass

    @abstractmethod
    def subValues(self, firstVal, secondVal):
        pass

    @abstractmethod
    def multipleValues(self, firstVal, secondVal):
        pass

    @abstractmethod
    def divideValues(self, firstVal, secondVal):
        pass

    @abstractmethod
    def derivativeFunction(self, function, x0, dx):
        pass
