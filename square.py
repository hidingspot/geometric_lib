def area(side: float) -> float:
    if side <= 0:
        raise ValueError("Side length must be positive")
    return side * side


def perimeter(side: float) -> float:
    if side <= 0:
        raise ValueError("Side length must be positive")
    return 4 * side
