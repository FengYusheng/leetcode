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


    def test_prev_order_traversal(self):
        data = ['S', 'E', 'X', 'A', 'R', 'C', 'H', 'M']
        tree = BinarySearchTree(TreeNode(data[0]))
        [tree.insert(TreeNode(i)) for i in data[1:]]
        # map returns a iterator in Python3 instead of a list in Python2.
        # for i in a:
        #     print(i)
        expected = ['S', 'E', 'A', 'C', 'R', 'H', 'M', 'X']
        self.assertEqual(tree.prevOrderTraverse(), expected)
        self.assertEqual(tree.prevOrderTraverseInLoop(), expected)

        data = ['H', 'C', 'S', 'A', 'E', 'R', 'X']
        expected = ['H', 'C', 'A', 'E', 'S', 'R', 'X']
        tree = BinarySearchTree(TreeNode(data[0]))
        [tree.insert(TreeNode(i)) for i in data[1:]]
        self.assertEqual(tree.prevOrderTraverse(), expected)
        self.assertEqual(tree.prevOrderTraverseInLoop(), expected)


    def test_in_order_traversal(self):
        data = ['S', 'E', 'X', 'A', 'R', 'C', 'H', 'M']
        tree = BinarySearchTree(TreeNode(data[0]))
        [tree.insert(TreeNode(i)) for i in data[1:]]
        expected = ['A', 'C', 'E', 'H', 'M', 'R', 'S', 'X']
        self.assertEqual(tree.inOrderTraverse(), expected)
        self.assertEqual(tree.inOrderTraverseInLoop(), expected)

        data = ['H', 'C', 'S', 'A', 'E', 'R', 'X']
        expected = ['A', 'C', 'E', 'H', 'R', 'S', 'X']
        tree = BinarySearchTree(TreeNode(data[0]))
        [tree.insert(TreeNode(i)) for i in data[1:]]
        self.assertEqual(tree.inOrderTraverse(), expected)
        self.assertEqual(tree.inOrderTraverseInLoop(), expected)


    def test_post_order_traversal(self):
        data = ['S', 'E', 'X', 'A', 'R', 'C', 'H', 'M']
        tree = BinarySearchTree(TreeNode(data[0]))
        [tree.insert(TreeNode(i)) for i in data[1:]]
        expected = ['C', 'A', 'M', 'H', 'R', 'E', 'X', 'S']
        self.assertEqual(tree.postOrderTraverse(), expected)
        self.assertEqual(tree.postOrderTraverseInLoop(), expected)

        data = ['H', 'C', 'S', 'A', 'E', 'R', 'X']
        expected = ['A', 'E', 'C', 'R', 'X', 'S', 'H']
        tree = BinarySearchTree(TreeNode(data[0]))
        [tree.insert(TreeNode(i)) for i in data[1:]]
        self.assertEqual(tree.postOrderTraverse(), expected)
        self.assertEqual(tree.postOrderTraverseInLoop(), expected)


    def test_broad_first_traversal(self):
        data = ['S', 'E', 'X', 'A', 'R', 'C', 'H', 'M']
        tree = BinarySearchTree(TreeNode(data[0]))
        [tree.insert(TreeNode(i)) for i in data[1:]]
        expected = ['S', 'E', 'X', 'A', 'R', 'C', 'H', 'M']
        self.assertEqual(tree.bft(), expected)


class TestRedBlackBST(unittest.TestCase):
    def test_create_a_red_black_bst_from_an_valid_tree_node(self):
        root = TreeNodeInRedBlackBST(1)
        self.assertIsInstance(RedBlackBST(root), RedBlackBST)
        with self.assertRaises(TypeError):
            RedBlackBST(TreeNode(1))


    def test_rotate_left(self):
        node1 = TreeNodeInRedBlackBST(3)
        node1.color = Color.BLACK
        node2 = TreeNodeInRedBlackBST(6)
        node1.right = node2
        node1 = RedBlackBST.rotateLeft(node1)
        self.assertEqual(node1.val, 6)
        self.assertEqual(node1.left.val, 3)
        self.assertTrue(node1.color is Color.BLACK)
        self.assertTrue(node1.left.color is Color.RED)
        self.assertIsNone(node1.right)


    def test_rotate_right(self):
        node1 = TreeNodeInRedBlackBST(3)
        node1.color = Color.BLACK
        node2 = TreeNodeInRedBlackBST(2)
        node1.left = node2
        node1 = RedBlackBST.rotateRight(node1)
        self.assertEqual(node1.val, 2)
        self.assertEqual(node1.right.val, 3)
        self.assertTrue(node1.color is Color.BLACK)
        self.assertTrue(node1.right.color is Color.RED)
        self.assertIsNone(node1.left)


    def test_insert_a_tree_node_into_a_red_black_bst(self):
        root = TreeNodeInRedBlackBST(0)
        tree = RedBlackBST(root)
        self.assertTrue(tree.root.color, Color.BLACK)
        for i in range(1, 4):
            self.assertEqual(tree.insert(TreeNodeInRedBlackBST(i)), i)


if __name__ == '__main__':
    unittest.main()
