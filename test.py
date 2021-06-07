import example
import unittest


class TestCase(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract1(self):
        self.assertEqual(example.subtract(3, 2), 1)

    def test_multiply1(self):
        self.assertEqual(example.multiply(3, 2), 6)

    def test_divide1(self):
        self.assertEqual(example.divide(6, 2), 3)


if __name__ == '__main__':
    unittest.main()
