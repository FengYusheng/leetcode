# -*- coding: utf-8 -*-

import unittest

from regular_expression_engine import *


class TestRegularExpressionEngine(unittest.TestCase):
    def test_case_1(self):
        self.assertFalse(isMatch('aa', 'a'))


    def test_case_2(self):
        self.assertTrue(isMatch('aa', 'a*'))


    def test_case_3(self):
        self.assertTrue(isMatch('ab', '.*'))


    def test_case_4(self):
        self.assertTrue(isMatch('aab', 'c*a*b'))


    def test_case_5(self):
        self.assertFalse(isMatch('mississippi', 'mis*is*p*.'))


if __name__ == '__main__':
    unittest.main()
