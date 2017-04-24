from Exceptions import *

def getCoefficientOfPolynomialFromString(function):
    coefficientList = list(function)
    coefficientList[:] = (value for value in coefficientList if value != ' ')

    for coefficient in coefficientList:
        try:
            int(coefficient)
        except ValueError:
            coefficientList.remove(coefficient)

    coefficientList = [int(x) for x in coefficientList]

    return coefficientList

def getValues(option):

    firstValue = float(input("Podaj pierwsza liczbe: "))
    secondValue = float(input("Podaj druga liczbe: "))

    return (firstValue, secondValue)

def getFunction(option):
    print("Podaj wartosci wspolczynnikow wielomianu [np. 2 3 4 -> 2x^2 + 3x + 4]")
    function = input()
    function = getCoefficientOfPolynomialFromString(function)
    return function

def options(calc, option):
    calcMethodOption = {
        1: calc.addValues,
        2: calc.subValues,
        3: calc.multipleValues,
        4: calc.divideValues,
        5: calc.derivativeFunction
    }

    return calcMethodOption[option]()

def doLoopContinue():
    while True:
        try:
            print("Czy chcesz kontynuowac? (t/n)")
            contin = input()
            if contin == 't':
                return True
            elif contin == 'n':
                print("Do zobaczenia :)")
                return False
            else:
                raise WrongCharacterException
        except WrongCharacterException:
            print("Litea nie jest ani y ani n. Sprobuj jeszcze raz")