# -*- coding: utf-8 -*-
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BinarySearchTree import *

class TestBinaryTree(unittest.TestCase):
    def test_build_binary_tree_from_root_node(self):
        root = TreeNode(1)
        self.assertIsInstance(BinarySearchTree(root), BinarySearchTree)


    def test_raise_exception_when_fail_build_binary_tree(self):
        root = 'Jia Jun'
        self.assertRaises(TypeError, BinarySearchTree, root)


    def test_build_binary_search_tree_from_tree_nodes(self):
        nodes = [TreeNode(i) for i  in range(5)]
        tree = BinarySearchTree.buildTreeFromTreeNodes(nodes)
        self.assertIsInstance(tree, BinarySearchTree)
        self.assertEqual(tree.root.children, 4)


    def test_raise_exception_when_fail_build_binary_tree_from_tree_nodes(self):
        self.assertRaises(TypeError, BinarySearchTree.buildTreeFromTreeNodes, 0x00)


    def test_insert_tree_node_into_binary_search_tree(self):
        root = TreeNode(0)
        tree = BinarySearchTree(root)
        for i in range(1, 4):
            self.assertEqual(tree.insert(TreeNode(i)), i)


    def test_rescure_insert_tree_node_into_binary_search_tree(self):
        root = TreeNode(0)
        tree = BinarySearchTree(root)
        for i in range(1, 4):
            self.assertEqual(tree.rescureInsert(TreeNode(i)), i)


    def test_get_length_of_a_binary_tree(self):
        tree = BinarySearchTree(TreeNode(0))
        self.assertEqual(len(tree), 1)
        tree.insert(TreeNode(1))
        tree.insert(TreeNode(2))
        tree.insert(TreeNode(3))
        self.assertEqual(len(tree), 4)



if __name__ == '__main__':
    unittest.main()
