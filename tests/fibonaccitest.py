import unittest
from fibonacci_calculator import views


class TestFibonacci(unittest.TestCase):
    def test_negative_integer(self):
        msg = "Number cannot be zero or negative"
        self.assertTrue(views.get_fibonacci(-1), msg=msg)
        self.assertTrue(views.get_fibonacci(0), msg)

    def test_none(self):
        msg = "Cannot be None"
        self.assertTrue(views.get_fibonacci(None), msg=msg)

    def test_non_Integer(self):
        msg = "Number has to be an integer"
        self.assertTrue(views.get_fibonacci(1.2), msg)

    def test_fibonacci(self):
        self.assertTrue(views.get_fibonacci(1), 1)
        self.assertTrue(views.get_fibonacci(2), 1)
        self.assertTrue(views.get_fibonacci(6), 8)


if __name__ == "__main__":
    unittest.main()

