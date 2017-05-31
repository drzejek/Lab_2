class DivisionByZeroException(Exception):
    def __str__(self):
        return repr("Division By Zero")

class NotANumberException(Exception):
    def __str__(self):
        return repr("Value is not a Number")

class NumberIsNegative(Exception):
    def __str__(self):
        return repr("Number is lower than 0")

class NotAFunction(Exception):
    def __str__(self):
        return  repr("Argument is not function")

