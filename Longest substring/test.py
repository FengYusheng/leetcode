# -*- coding: utf-8 -*-

import unittest

from longest_substring import *

class TestLongestSubstring(unittest.TestCase):
    def test_case_1(self):
        substring, length = find_longest_substring('abcabcbb')
        self.assertEqual(substring, 'abc')


    def test_case_2(self):
        substring, _ = find_longest_substring('bbbbb')
        self.assertEqual(substring, 'b')


    def test_case_3(self):
        substring, _ = find_longest_substring('pwwkew')
        self.assertEqual(substring, 'wke')


if __name__ == '__main__':
    unittest.main()
