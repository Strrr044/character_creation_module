from math import sqrt


message = ('Добро пожаловать в самую лучшую программу для вычисления '

           'квадратного корня из заданного числа')


def Calculate_SquareRoot(number):

    """ Вычисляет квадратный корень"""

    return sqrt(number)


def calc(your_number):

    if your_number <= 0:

        return
    res = Calculate_SquareRoot(your_number)

    print(f'Мы вычислили квадратный корень из введённого вами числа. Это будет:{res}')


print(message)

calc(25.5)