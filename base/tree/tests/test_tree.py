# -*- coding: utf-8 -*-
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BinaryTree import *

class TestBinaryTree(unittest.TestCase):
    def test_build_binary_tree_from_root_node(self):
        root = TreeNode(1)
        self.assertIsInstance(BinaryTree(root), BinaryTree)


    def test_raise_exception_when_fail_build_binary_tree(self):
        root = 'Jia Jun'
        self.assertRaises(TypeError, BinaryTree, root)


    def test_build_binary_tree_from_tree_nodes(self):
        nodes = [TreeNode(i) for i  in range(5)]
        self.assertIsInstance(BinaryTree.buildTreeFromTreeNodes(nodes), BinaryTree)


    def test_raise_exception_when_fail_build_binary_tree_from_tree_nodes(self):
        self.assertRaises(TypeError, BinaryTree.buildTreeFromTreeNodes, 0x00)


    def test_insert_Tree_Node_Into_Binary_Tree(self):
        root = TreeNode(0)
        leaves = [TreeNode(i) for i in range(1, 4)]
        tree = BinaryTree(root)
        tree.insert(leaves[0])



if __name__ == '__main__':
    unittest.main()
