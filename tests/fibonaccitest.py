import unittest
from fibonacci_calculator import views

class TestFibonacci(unittest.TestCase):
    def testCaseNegativeInteger(self):
        msg = "Number cannot be zero or negative"
        self.assertTrue(views.getfibonacci(-1), msg=msg)
        self.assertTrue(views.getfibonacci(0), msg)

    def testCaseNone(self):
        msg = "Cannot be None"
        self.assertTrue(views.getfibonacci(None), msg=msg)

    def testCaseNonInteger(self):
        msg = "Number has to be an integer"
        self.assertTrue(views.getfibonacci(1.2), msg)

    def testCaseFibonacci(self):
        self.assertTrue(views.getfibonacci(1), 1)
        self.assertTrue(views.getfibonacci(2), 1)
        self.assertTrue(views.getfibonacci(6), 8)

if __name__ == "__main__":
    unittest.main()

