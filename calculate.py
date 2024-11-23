import circle
import square

"""
Программа выполняет вычисление заданной функции (площадь или периметр) для указанной фигуры (круг или квадрат)
на основе переданных размеров фигуры.
Параметры: строка, строка, параметр фигуры.
Возвращаемое значение: площадь или периметр фигуры в виде числа.
"""

figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {"circle": 1, "square": 1}


def calc(fig: str, func: str, size: list) -> float:
    assert fig in figs, f"Figure '{fig}' is not supported."
    assert func in funcs, f"Function '{func}' is not supported."

    if len(size) != sizes[fig]:
        raise ValueError(
            f"Invalid number of arguments for {fig}. Expected {sizes[fig]}, got {len(size)}."
        )

    if any(s <= 0 for s in size):
        raise ValueError(f"All size parameters must be positive. Got: {size}")

    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(fig, 1):
        try:
            size = list(
                map(
                    float,
                    input(
                        f"Input {sizes[fig]} size(s) for {fig} separated by space:\n"
                    ).split(),
                )
            )
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    try:
        result = calc(fig, func, size)
        print(f"{func} of {fig} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
