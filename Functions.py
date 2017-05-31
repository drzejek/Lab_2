from Exceptions import *

def isIntInstance(value):
    return isinstance(value, int)

def isFloatInstance(value):
    return isinstance(value, float)

def isArgumentNumber(value):
    if not (isIntInstance(value) or isFloatInstance(value)):
        raise NotANumberException

def isNumberNegative(value):
    if value < 0:
        raise NumberIsNegative

def isDivisionByZero(value):
    if value==0:
        raise DivisionByZeroException

def isAFunction(function):
    if not callable(function):
        raise NotAFunction