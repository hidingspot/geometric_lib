import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        # Arrange
        a, b, c = 5, 6, 7  # Стороны треугольника
        expected_area = 14.696938456699069  # Ручной расчет или известный результат

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, expected_area, places=7)

    def test_triangle_perimeter(self):
        # Arrange
        a, b, c = 5, 6, 7
        expected_perimeter = 18

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_perimeter)

    def test_invalid_triangle_area(self):
        # Arrange
        a, b, c = 1, 2, 3  # Эти стороны не образуют треугольник

        # Act and Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_invalid_triangle_perimeter(self):
        a, b, c = 1, 2, 3
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_negative_sides_area(self):
        # Arrange
        a, b, c = -5, 6, 7  # Отрицательная сторона

        # Act and Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_negative_sides_perimeter(self):
        # Arrange
        a, b, c = -5, 6, 7  # Отрицательная сторона

        # Act and Assert
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_zero_sides_area(self):
        # Arrange
        a, b, c = 0, 6, 7  # Сторона равна нулю

        # Act and Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_zero_sides_perimeter(self):
        a, b, c = 0, 6, 7
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
