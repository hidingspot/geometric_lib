import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    # Положительные тесты для площади квадрата
    def test_square_area(self):
        # Arrange
        side = 4
        expected_area = side * side  # 4 * 4 = 16

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected_area)

    # Положительные тесты для периметра квадрата
    def test_square_perimeter(self):
        # Arrange
        side = 4
        expected_perimeter = 4 * side  # 4 * 4 = 16

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected_perimeter)

    # Тест для нулевого значения (ожидаем ValueError)
    def test_zero_square_area(self):
        # Arrange
        side = 0

        # Act and Assert
        with self.assertRaises(ValueError):
            area(side)

    def test_zero_square_perimeter(self):
        side = 0
        with self.assertRaises(ValueError):
            perimeter(side)

    # Негативные тесты для отрицательного значения (ожидаем ValueError)
    def test_negative_square_area(self):
        # Arrange
        side = -4

        # Act and Assert
        with self.assertRaises(ValueError):
            area(side)

    def test_negative_square_perimeter(self):
        side = -4
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
