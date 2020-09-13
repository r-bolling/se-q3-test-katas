import unittest
import random
import math
from katas import *

def rand_positive_int(num=0, num2=10000):
    return random.randrange(num, num2)

def rand_negative_int(num=-10000, num2=0):
    return random.randrange(num, num2)

def fraction():
    return random.random()

class TestKatas(unittest.TestCase):
    def test_add(self):
        '''Return the sum of two numbers'''
        num = rand_positive_int()
        num2 = rand_positive_int()
        neg_num = rand_negative_int()
        neg_num2 = rand_negative_int()
        self.assertEqual(add(9134, 4521), 13655)
        self.assertEqual(add(num, num2), num + num2)
        self.assertEqual(add(neg_num, num2), neg_num + num2)
        self.assertEqual(add(neg_num, neg_num2), neg_num + neg_num2)

    def test_multiply(self):
        '''Return the product of two numbers'''
        num = rand_positive_int()
        num2 = rand_positive_int()
        neg_num = rand_negative_int()
        neg_num2 = rand_negative_int()
        self.assertEqual(multiply(57, 10363), 590691)
        self.assertEqual(multiply(num, num2), num * num2)
        self.assertEqual(multiply(neg_num, num2), neg_num * num2)
        self.assertEqual(multiply(neg_num, neg_num2), neg_num * neg_num2)
        # self.fail("TODO: Write multiply unit test")

    def test_power(self):
        '''Return the input exponent of an input number'''
        num = rand_positive_int(1, 100)
        num2 = rand_positive_int(1, 100)
        self.assertRaises(ValueError, power, 5, rand_negative_int())
        self.assertRaises(ValueError, power, 5, fraction())
        self.assertEqual(power(9, 3), 729)
        self.assertEqual(power(num, num2), num ** num2)
        # self.fail("TODO: Write power unit test")

    def test_factorial(self):
        self.assertRaises(ValueError, factorial, rand_negative_int())
        self.assertEqual(factorial(5), 120)
        for n in range(0, 15):
            self.assertEqual(factorial(n), math.factorial(int(n)))

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
