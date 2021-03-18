def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py", __name__)


"""
__name__ specjalna globalna zmienna zależna od miejsca gdzie się jest, pliku
w tym liku zwróci to __main__
w pliku gdzie się go wywoła (w code) będzie to mymodule czyli nazwa pliku
"""

import libs.mylib