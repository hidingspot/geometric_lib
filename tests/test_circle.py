import unittest
from circle import area, perimeter
import math


class TestCircle(unittest.TestCase):
    # Положительные тесты для площади круга
    def test_circle_area(self):
        # Arrange
        radius = 3
        expected_area = math.pi * radius * radius  # π * 3^2

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, expected_area)

    # Положительные тесты для периметра круга
    def test_circle_perimeter(self):
        # Arrange
        radius = 3
        expected_perimeter = 2 * math.pi * radius  # 2π * 3

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected_perimeter)

    # Тест для нулевого значения (ожидаем ValueError)
    def test_zero_circle_area(self):
        # Arrange
        radius = 0

        # Act and Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_zero_circle_perimeter(self):
        radius = 0

        with self.assertRaises(ValueError):
            perimeter(radius)

    # Негативные тесты для отрицательного значения (ожидаем ValueError)
    def test_negative_circle_area(self):
        # Arrange
        radius = -3

        # Act and Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_negative_circle_perimeter(self):
        radius = -3
        with self.assertRaises(ValueError):
            perimeter(radius)


if __name__ == "__main__":
    unittest.main()
