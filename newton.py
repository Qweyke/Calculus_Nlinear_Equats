"""
Суть метода Ньютона основана на принципе простых итераций, поиск решения осуществляется путём построения
последовательных приближений:
    Идея метода простой итерации состоит в том, чтобы задать уравнение phi(x) = x - f(x)/f'(x)
    Изначально необходимо найти начальное приближение, удовлетворяющее условию f'(x)*f"(x) > 0
    Далее нужно строить итерации по принципу x_(n+1) = x_n-1 - f(x_n-1)/f'(x_n-1).
    Остановка цикла происходит по достижению точности значения функции < eps

"""

from math import *

a = 0  # начало отрезка
b = 1  # конец отрезка
eps = 10**(-6)  # погрешность
i = 10


def f(x):  # функция
    return (0.75-x)*(exp(1)**(x/2)) - 0.5


def d_f(x):
    return -(1.25 + x) * exp(1)**(x / 2) / 2


def dd_f(x):
    return -(3.25 + x) * exp(1)**(x / 2) / 4


def solve2(func, d_func, dd_func, x0, x1, iteration):
    cnt = 0
    if d_func(x0) * dd_func(x0) > 0:
        curr_x = x0
        while abs(func(curr_x)) > eps and cnt <= iteration:
            prev_x = curr_x
            curr_x = prev_x - (func(prev_x) / d_func(prev_x))
            cnt += 1

    elif d_func(x1) * dd_func(x1) > 0:
        curr_x = x1
        while abs(func(curr_x)) > eps and cnt <= iteration:
            prev_x = curr_x
            curr_x = prev_x - (func(prev_x) / d_func(prev_x))
            cnt += 1

    else:
        print("Значений не найдено")
        return None

    print(f"Кол-во итераций метода Ньютона = {cnt}")
    print(f"Корень методом Ньютона: {round(curr_x, 5)}")  # вывод округления x до 5 знаков
    res = round(curr_x, 5)
    return round(abs((func(res) / eps)), 5)  # подстановка x в изначальную функцию, без 10^(-p)


if __name__ == "__main__":
    print(solve2(f, d_f, dd_f, a, b, i))
