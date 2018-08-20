# -*- coding: utf-8 -*-

import os
import sys
import unittest

from two_sum import *


class TestTwoSum(unittest.TestCase):
    def test_case_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(numbers, target), (0, 1))


    def test_case_2(self):
        numbers = [2, 7, 11, 15]
        target = 13
        self.assertEqual(two_sum(numbers, target), (0, 2))


    def test_case_3(self):
        numbers = [2, 7, 11, 15]
        target = 17
        self.assertEqual(two_sum(numbers, target), (0, 3))


    def test_case_4(self):
        numbers = [2, 7, 11, 15]
        target = 18
        self.assertEqual(two_sum(numbers, target), (1, 2))


    def test_case_5(self):
        numbers = [2, 7, 11, 15]
        target = 22
        self.assertEqual(two_sum(numbers, target), (1, 3))


    def test_case_6(self):
        numbers = [2, 7, 11, 15]
        target = 26
        self.assertEqual(two_sum(numbers, target), (2, 3))



if __name__ == '__main__':
    unittest.main()
