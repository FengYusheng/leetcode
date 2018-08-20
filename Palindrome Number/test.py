# -*- coding: utf-8 -*-

import unittest

from palindrome_number import *


class TestPalindromeNumber(unittest.TestCase):
    def test_positive_number(self):
        self.assertTrue(palindrome(121))


    def test_negative_number(self):
        self.assertFalse(palindrome(-121))


    def test_positive_number_2(self):
        self.assertFalse(palindrome(10))


if __name__ == '__main__':
    unittest.main()
