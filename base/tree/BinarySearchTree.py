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
            raise TypeError(TYPEERROR_FMT.format(val, type(val)))

        self._left = val


    @property
    def right(self):
        return self._right


    @right.setter
    def right(self, val):
        if not isinstance(val, TreeNode):
            raise TypeError(TYPEERROR_FMT.format(val, type(val)))

        self._right = val


class BinarySearchTree:
    def __init__(self, root):
        if isinstance(root, TreeNode):
            self._root = root
        else:
            raise TypeError(TYPEERROR_FMT.format(root, type(root)))


    @property
    def root(self):
        return self._root


    @classmethod
    def buildTreeFromTreeNodes(cls, nodes):
        node_iterator = iter(nodes)
        tree = None
        for i in node_iterator:
            if tree:
                tree.insert(i)
            else:
                tree = cls(i)

        return tree


    def insert(self, node):
        if not isinstance(node, TreeNode):
            raise TypeError('A TreeNode object is expected.')

        if self.root is None:
            self.root = node
            return self.root.children

        pivot = self.root
        while pivot:
            pivot.children += 1
            if pivot.val >= node.val:
                if pivot.left is None:
                    pivot.left = node
                    break
                pivot = pivot.left
            else:
                if pivot.right is None:
                    pivot.right = node
                    break
                pivot = pivot.right

        return self.root.children



__all__ = [
    'TreeNode',
    'BinarySearchTree'
]
