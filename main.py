from Calculator import *
from Exceptions import *

from Functions import *

def main():
    calc = Calculator()

    info =("Wybierz jedno z mozliwych opcji\n"
    "1: Dodawanie\n"
    "2: Oddejmowanie\n"
    "3: Mnozenie\n"
    "4: Dzielenie\n"
    "5: Pochodna funkcji\n")

    while True:
        try:
            print(info)
            option = input()

            try:
                option = int(option)
            except ValueError:
                print("To nie jest liczba. Sprobuj jeszcze raz")
                continue

            if(1 <= option <= 4):
                val = getValues(option)
                calc.getValues(val[0], val[1])
            elif option == 5:
                calc.getFunction(getFunction(option))
            else:
                raise WrongNumberException

            score = options(calc, option)
            print(str(score))

            doContinue = doLoopContinue()

            if doContinue: continue
            else: break

        except NotANumberException:
            print("Dana wartosc nie jest liczba. Sprobuj jeszcze raz")
        except WrongNumberException:
            print("Dana liczba nie miesci sie w przedziale [1,5]. Sprobuj jeszcze raz")


if __name__ == '__main__':
    main()