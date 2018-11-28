# -*- coding: utf-8 -*-

TYPEERROR_FMT = 'A TreeNode object is epxtected, but the argument {0} is {1}'

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = 0
        self._left = None
        self._right = None


    @property
    def left(self):
        return self._left


    @left.setter
    def left(self, val):
        if not isinstance(val, TreeNode):
            raise TypeError(TYPEERROR_FMT.fomart(val, type(val)))


class BinaryTree:
    def __init__(self, root):
        if isinstance(root, TreeNode):
            self.root = root
        else:
            raise TypeError(TYPEERROR_FMT.format(root, type(root)))


    @classmethod
    def buildTreeFromTreeNodes(cls, nodes):
        node_iterator = iter(nodes)
        return cls(next(node_iterator))


    def insert(self, node):
        if not isinstance(node, TreeNode):
            raise TypeError('A TreeNode object is expected.')

        pivot = self.root




__all__ = [
    'TreeNode',
    'BinaryTree'
]
