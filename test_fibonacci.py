import unittest
import fibonacci
import pytest
#unittest
class TestCase(unittest.TestCase):
    def test_fib1(self):
        self.assertEqual(fibonacci.fibonacci(6), 8)

    def test_fib2(self):
        self.assertEqual(fibonacci.fibonacci(4), 3)

    def test_fib3(self):
        self.assertEqual(fibonacci.fibonacci(2), 1)

    def test_fib4(self):
        self.assertEqual(fibonacci.fibonacci(1), 1)

    def test_fib5(self):
        with self.assertRaises(TypeError):
            fibonacci.fibonacci("2")

    def test_fib6(self):
        with self.assertRaises(Exception):
            fibonacci.fibonacci(-2)


if __name__ == '__main__':
    unittest.main()

#pytest
def test_fibo1():
    assert fibonacci.fibonacci(0) == 0

def test_fibo2():
    assert fibonacci.fibonacci(6) == 8

def test_fibo3():
    with pytest.raises(Exception):
        fibonacci.fibonacci(-2)

def test_fibo3():
    with pytest.raises(TypeError):
        fibonacci.fibonacci("2")