# -*- coding: utf-8 -*-
from collections import deque

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


    def __len__(self):
        return self.root.children + 1 if self.root else 0


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


    def rescureInsert(self, node):
        def _insert(pivot):
            if pivot is None:
                pivot = node
            elif pivot.val >= node.val:
                pivot.children += 1
                _insert(pivot.left)
            else:
                pivot.children += 1
                _insert(pivot.right)
            return pivot.children

        return _insert(self.root)


    def prevOrderTraverse(self):
        def _prevOrderTraverse(root,ret=[]):
            if root:
                ret.append(root.val)
                _prevOrderTraverse(root.left, ret)
                _prevOrderTraverse(root.right, ret)
            return ret

        return _prevOrderTraverse(self.root)


    def prevOrderTraverseInLoop(self):
        ret = []
        stack = deque()
        stack.append(self.root)
        while len(stack):
            pivot = stack.pop()
            ret.append(pivot.val)
            # Push the right node first, then push the left node.
            pivot.right and stack.append(pivot.right)
            pivot.left and stack.append(pivot.left)
        return ret


    def inOrderTraverse(self):
        def _inOrderTraverse(root, ret=[]):
            if root:
                _inOrderTraverse(root.left)
                ret.append(root.val)
                _inOrderTraverse(root.right)
            return ret
        return _inOrderTraverse(self.root)


    def inOrderTraverseInLoop(self):
        ret = []
        

        return ret


__all__ = [
    'TreeNode',
    'BinarySearchTree'
]
