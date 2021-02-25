import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test_fib1(self):
        self.assertEqual(fibonacci.fibonacci(6), 8)
    def test_fib2(self):
        self.assertEqual(fibonacci.fibonacci(4), 3)
    def test_fib3(self):
        self.assertEqual(fibonacci.fibonacci(2), 1)
    def test_fib4(self):
        self.assertEqual(fibonacci.fibonacci(1), 1)





if __name__ == '__main__':
    unittest.main()