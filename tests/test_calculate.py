import unittest
from calculate import calc


class TestCalcFunction(unittest.TestCase):
    def test_valid_square_area(self):
        self.assertEqual(calc("square", "area", [4]), 16)

    def test_valid_square_perimeter(self):
        self.assertEqual(calc("square", "perimeter", [4]), 16)

    def test_valid_circle_area(self):
        self.assertAlmostEqual(
            calc("circle", "area", [3]), 28.274333882308138, places=5
        )

    def test_valid_circle_perimeter(self):
        self.assertAlmostEqual(
            calc("circle", "perimeter", [3]), 18.84955592153876, places=5
        )

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError) as cm:
            calc("triangle", "area", [3])
        self.assertEqual(str(cm.exception), "Figure 'triangle' is not supported.")

    def test_invalid_function(self):
        with self.assertRaises(AssertionError) as cm:
            calc("circle", "volume", [3])
        self.assertEqual(str(cm.exception), "Function 'volume' is not supported.")

    def test_invalid_size_length_square(self):
        with self.assertRaises(ValueError) as cm:
            calc("square", "area", [4, 5])
        self.assertEqual(
            str(cm.exception),
            "Invalid number of arguments for square. Expected 1, got 2.",
        )

    def test_invalid_size_length_circle(self):
        with self.assertRaises(ValueError) as cm:
            calc("circle", "perimeter", [3, 5])
        self.assertEqual(
            str(cm.exception),
            "Invalid number of arguments for circle. Expected 1, got 2.",
        )

    def test_negative_size_square(self):
        with self.assertRaises(ValueError) as cm:
            calc("square", "area", [-4])
        self.assertEqual(
            str(cm.exception), "All size parameters must be positive. Got: [-4]"
        )

    def test_zero_size_square(self):
        with self.assertRaises(ValueError) as cm:
            calc("square", "perimeter", [0])
        self.assertEqual(
            str(cm.exception), "All size parameters must be positive. Got: [0]"
        )

    def test_negative_size_circle(self):
        with self.assertRaises(ValueError) as cm:
            calc("circle", "area", [-3])
        self.assertEqual(
            str(cm.exception), "All size parameters must be positive. Got: [-3]"
        )

    def test_zero_size_circle(self):
        with self.assertRaises(ValueError) as cm:
            calc("circle", "perimeter", [0])
        self.assertEqual(
            str(cm.exception), "All size parameters must be positive. Got: [0]"
        )

    def test_non_numeric_size_square(self):
        with self.assertRaises(TypeError):
            calc("square", "area", ["not_a_number"])

    def test_non_numeric_size_circle(self):
        with self.assertRaises(TypeError):
            calc("circle", "perimeter", ["not_a_number"])


if __name__ == "__main__":
    unittest.main()
