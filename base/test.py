# -*- coding: utf-8 -*-
import unittest
from BinaryTree import *

class TestBinaryTree(unittest.TestCase):
    def test_build_binary_tree_from_root_node(self):
        root = TreeNode(1)
        self.assertIsInstance(BinaryTree(root), BinaryTree)


    def test_raise_exception_when_fail_build_binary_tree(self):
        root = 'Jia Jun'
        self.assertRaises(TypeError, BinaryTree, root)



if __name__ == '__main__':
    unittest.main()
