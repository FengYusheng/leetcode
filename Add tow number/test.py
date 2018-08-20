# -*- coding: utf-8 -*-

import unittest

from add_two_number import *



class TestAddTwoNumbers(unittest.TestCase):
    def test_build_link(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]

        i = 0
        current_node = buildLink(l1)
        while current_node is not None:
            self.assertEqual(current_node.val, l1[i])
            i += 1
            current_node = current_node.next

        i = 0
        current_node = buildLink(l2)
        while current_node is not None:
            self.assertEqual(current_node.val, l2[i])
            i += 1
            current_node = current_node.next


    def test_add_two_number_links(self):
        link1 = buildLink([2, 4, 3])
        link2 = buildLink([5, 6, 4])
        result = [7, 0, 8]
        i = 0

        current_node = add_two_number_links(link1, link2)
        while current_node is not None:
            self.assertEqual(current_node.val, result[i])
            i += 1
            current_node = current_node.next



if __name__ == '__main__':
    unittest.main()
