import unittest
import random
from katas import *


class TestKatas(unittest.TestCase):
    def test_add(self):
        '''Return the sum of two numbers'''
        num = random.randrange(0, 10000)
        num2 = random.randrange(0, 10000)
        neg_num = random.randrange(-10000, 0)
        neg_num2 = random.randrange(-10000, 0)
        self.assertEqual(add(num, num2), num + num2)
        self.assertEqual(add(neg_num, num2), neg_num + num2)
        self.assertEqual(add(neg_num, neg_num2), neg_num + neg_num2)

    def test_multiply(self):
        self.fail("TODO: Write multiply unit test")

    def test_power(self):
        self.fail("TODO: Write power unit test")

    def test_factorial(self):
        self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
