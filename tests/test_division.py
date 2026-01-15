import unittest
from cal import div


class TestDivision(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(div(10, 2), 5.0)

    def test_negative_integers(self):
        self.assertEqual(div(-10, -2), 5.0)

    def test_mixed_sign_integers(self):
        self.assertEqual(div(-10, 2), -5.0)

    def test_floats(self):
        self.assertEqual(div(10.5, 2), 5.25)
        self.assertAlmostEqual(div(1.0, 3.0), 0.3333333333, places=7)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            div("10", 2)
        with self.assertRaises(TypeError):
            div(10, "2")
        with self.assertRaises(TypeError):
            div(None, 2)


if __name__ == "__main__":
    unittest.main()
