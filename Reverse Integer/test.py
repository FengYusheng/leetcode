# -*- coding: utf-8 -*-

import unittest

from reverse_interger import *


class TestReverseNumber(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverse(123), 321)


    def test_case_2(self):
        self.assertEqual(reverse(-123), -321)


    def test_case_3(self):
        self.assertEqual(reverse(120), 21)


if __name__ == '__main__':
    unittest.main()
