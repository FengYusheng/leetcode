# -*- coding: utf-8 -*-

import sys
import unittest

from atoi import *


class TestAtoi(unittest.TestCase):
    def test_atoi_positive_number(self):
        self.assertEqual(atoi('42'), 42)


    def test_atoi_negative_number(self):
        self.assertEqual(atoi('-42'), -42)


    def test_atoi_positive_number2(self):
        self.assertEqual(atoi('+42'), 42)


    def test_atoi_invalid_characters(self):
        self.assertEqual(atoi('words and 987'), 0)


    def test_atoi_invalid_characters2(self):
        self.assertEqual(atoi('4193 with words'), 4193)


    def test_atoi_too_large_number(self):
        self.assertRaises(ValueError, atoi, '92233720368547758070')


if __name__ == '__main__':
    unittest.main()
