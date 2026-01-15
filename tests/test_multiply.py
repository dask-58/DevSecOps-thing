import unittest
from cal  import multiply


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 5), -10)

    def test_zero(self):
        self.assertEqual(multiply(0, 10), 0)


if __name__ == "__main__":
    unittest.main()

