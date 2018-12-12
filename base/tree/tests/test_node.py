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


class TestTreeNodeInRedBlackBST(unittest.TestCase):
    def test_set_tree_node_color(self):
        node = TreeNodeInRedBlackBST(1)
        self.assertEqual(node.color, Color.RED)
        node.color = Color.BLACK
        self.assertEqual(node.color, Color.BLACK)


    def test_raise_type_error_when_assign_invalid_color(self):
        node = TreeNodeInRedBlackBST(1)
        with self.assertRaises(TypeError):
            node.color = 'Green'


    def test_a_tree_node_in_red_black_bst_is_red(self):
        self.assertTrue(TreeNodeInRedBlackBST(1))



if __name__ == '__main__':
    unittest.main()
