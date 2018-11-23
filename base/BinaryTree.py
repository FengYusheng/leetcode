# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = 0
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        if isinstance(root, TreeNode):
            self.root = root
        else:
            raise TypeError('A TreeNode object is epxtected, but the argument {0} is {1}'.format(root, type(root)))


    @classmethod
    def buildTreeFromTreeNodes(cls, nodes):
        node_iterator = iter(nodes)
        return cls(next(node_iterator))


    def insert(self, node):
        pass



__all__ = [
    'TreeNode',
    'BinaryTree'
]
