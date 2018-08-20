# -*- coding: utf-8 -*-

import unittest

from longest_palindromic import *


class TestPalindromic(unittest.TestCase):
    def test_middle_index(self):
        self.assertEqual(find_middle_index('babad'), 2)
        self.assertEqual(find_middle_index('cbbd'), 2)


    def test_palindromic_1(self):
        self.assertEqual(find_palindromic('babad'), 'aba')
        self.assertEqual(find_palindromic('cbbd'), 'bb')



if __name__ == '__main__':
    unittest.main()
