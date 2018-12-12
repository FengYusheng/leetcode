# -*- coding: utf-8 -*-
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BinarySearchTree import *


class TestTreeNode(unittest.TestCase):
    def test_get_and_set_left_node(self):
        node = TreeNode('JiaJun')
        left = TreeNode('WangYan')
        node.left = left
        self.assertEqual(node.left, left)


    def test_left_node_validation(self):
        node = TreeNode('JiaJun')
        with self.assertRaises(TypeError):
            node.left = 1


    def test_get_and_set_right_node(self):
        node = TreeNode('JiaJun')
        right = TreeNode('WangYan')
        node.right = right
        self.assertEqual(node.right, right)


    def test_right_node_validation(self):
        node = TreeNode('JiaJun')
        with self.assertRaises(TypeError):
            node.right = 1


class TestColorEnum(unittest.TestCase):
    def test_color_value(self):
        self.assertTrue(bool(Color.RED.value))
        self.assertFalse(bool(Color.BLACK.value))



if __name__ == '__main__':
    unittest.main()
