# -*- coding: utf-8 -*-
import unittest

from get_meidan import *


class TestMeidan(unittest.TestCase):
    def test_merge_1(self):
        l1 = [1, 3]
        l2 = [2]

        self.assertEqual(len(merge([], [])), len([]))

        merge_ret = merge(l1, l2)
        for i in range(len(merge_ret)-1):
            self.assertTrue(merge_ret[i] <= merge_ret[i+1])


    def test_merge_2(self):
        l1 = [1, 2]
        l2 = [3, 4]

        merge_ret = merge(l1, l2)
        for i in range(len(merge_ret)-1):
            self.assertTrue(merge_ret[i], merge_ret[i+1])


    def test_median_1(self):
        numbers1 = [1, 3]
        numbers2 = [2]

        self.assertEqual(median(numbers1, numbers2), 2)


    def test_median_2(self):
        numbers1 = [1, 2]
        numbers2 = [3, 4]

        self.assertEqual(median(numbers1, numbers2), 2.5)


if __name__ == '__main__':
    unittest.main()
