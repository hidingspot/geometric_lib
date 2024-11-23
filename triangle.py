import math


def area(a, b, c):
    # Проверка сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The provided sides do not form a triangle")

    # Формула Герона
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    # Проверка сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The provided sides do not form a triangle")

    return a + b + c
