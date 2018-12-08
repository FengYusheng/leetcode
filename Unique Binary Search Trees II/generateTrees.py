# -*- coding: utf-8 -*-
# This is a problem about dynamic programming and Binary Search Tree.
# Binary Search is an idea, and Binary Search Tree is the data struture to implement
# this idea.
# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31609/Simple-python-solution

# https://www.sohu.com/a/153858619_466939
# https://leetcode.com/articles/unique-binary-search-trees/

# You can get a sorted array if you in-order traverse a binary search tree. Every
# elmemnt in this sorted array can be selected as a root of a binary search tree.
# The elements before the selected consist of left tree. The elements after the
# selected consist of right tree.
import os
import sys
import time
import functools

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.tree.BinarySearchTree import *


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{0} costs {1:' '>4.3f}s'.format(func.__name__, end-start))
        return ret
    return decorator


def _generateTrees(num, start=1):
    ret = []
    if num < start:
        return [None]
    if num == start:
        return [TreeNode(start)]
    for i in range(start, num+1):
        left_trees = _generateTrees(i-1, start)
        right_trees = _generateTrees(num, i+1)
        for l in left_trees:
            for r in right_trees:
                root = TreeNode(i)
                root.left = l
                root.right = r
                ret.append(root)
    return ret


def generateTrees(num):
    return _generateTrees(num) if num else []



if __name__ == '__main__':
    # num = 3
    # actual = generateTrees()
    # expected = [
    #     [1, 3, 2],
    #     [3, 2, 1],
    #     [3, 1, 2],
    #     [2, 1, 3],
    #     [1, 2, 3]
    # ]
    # assert len(actual) == len(expected)
    # for i in actual:
    #     assert i in expected

    actual = generateTrees(3)
    print(len(actual))
    for i in actual:
        tree = BinarySearchTree(i)
        print(tree.prevOrderTraverse())

    actual = generateTrees(2)
    print(len(actual))
    for i in actual:
        tree = BinarySearchTree(i)
        print(tree.prevOrderTraverse())

    actual = generateTrees(0)
    print(actual)
