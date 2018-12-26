# -*- coding: utf-8 -*-
from collections import deque
from enum import Enum, auto

TYPEERROR_FMT = 'A TreeNode object is epxtected, but the argument {0} is {1}'


class Color(Enum):
    BLACK = 0
    RED = auto()


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = 0
        self._left = None
        self._right = None


    def __len__(self):
        return self.children + 1


    @property
    def left(self):
        return self._left


    @left.setter
    def left(self, val):
        if not isinstance(val, TreeNode) and val is not None:
            raise TypeError(TYPEERROR_FMT.format(val, type(val)))

        self._left = val


    @property
    def right(self):
        return self._right


    @right.setter
    def right(self, val):
        if not isinstance(val, TreeNode) and val is not None:
            raise TypeError(TYPEERROR_FMT.format(val, type(val)))

        self._right = val


class TreeNodeInRedBlackBST(TreeNode):
    def __init__(self, val):
        super().__init__(val)
        self._color = Color.RED


    @property
    def color(self):
        return self._color


    @color.setter
    def color(self, color):
        if not isinstance(color, Color):
            raise TypeError("A Color enum memenber is expected.")

        self._color = color


class ThreadedTreeNode(TreeNode):
    def __init__(self, val):
        super().__init__(val)


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
        aux = set()
        stack = deque()
        stack.append(self.root)
        while len(stack):
            pivot = stack.pop()
            if pivot.right and pivot.right not in stack:
                stack.append(pivot.right)
            if pivot.left and pivot.left not in aux:
                stack.append(pivot)
                stack.append(pivot.left)
            if pivot.left is None or pivot.left in aux:
                ret.append(pivot.val)
                aux.add(pivot)
        return ret


    def postOrderTraverse(self):
        def _postOrderTraverse(root, ret=[]):
            if root:
                _postOrderTraverse(root.left)
                _postOrderTraverse(root.right)
                ret.append(root.val)
            return ret
        return _postOrderTraverse(self.root)


    def postOrderTraverseInLoop(self):
        ret = []
        aux = set()
        stack = deque()
        stack.append(self.root)
        while len(stack):
            pivot = stack.pop()
            if (pivot.left and pivot.left not in aux) \
            or (pivot.right and pivot.right not in aux):
                stack.append(pivot)
            if pivot.right and pivot.right not in aux:
                stack.append(pivot.right)
            if pivot.left and pivot.left not in aux:
                stack.append(pivot.left)
            if (pivot.left is None or pivot.left in aux) \
            and (pivot.right is None or pivot.right in aux):
                ret.append(pivot.val)
                aux.add(pivot)
        return ret


    def bft(self):
        ret = []
        queue = deque()
        queue.append(self.root)
        while len(queue):
            pivot = queue.popleft()
            pivot.left and queue.append(pivot.left)
            pivot.right and queue.append(pivot.right)
            ret.append(pivot.val)
        return ret


    @staticmethod
    def height(pivot):
        if not pivot:
            return 0

        if not isinstance(pivot, TreeNode):
            raise TypeError('A TreeNode object is expected.')

        return 1 + max([BinarySearchTree.height(pivot.left), BinarySearchTree.height(pivot.right)])



class RedBlackBST(BinarySearchTree):
    def __init__(self, root):
        if not isinstance(root, TreeNodeInRedBlackBST):
            raise TypeError('A TreeNodeInRedBlackBST is expected.')

        self._root = root
        # The color of root is always black in a RedBlackBST.
        self._root.color = Color.BLACK


    @property
    def root(self):
        return self._root


    @root.setter
    def root(self, node):
        if not isinstance(node, TreeNodeInRedBlackBST):
            raise TypeError('A TreeNodeInRedBlackBST is expected')

        self._root = node
        self.root.color = Color.BLACK


    @staticmethod
    def rotateLeft(node):
        x = node.right
        node.right = x.left
        x.left = node
        x.children = node.children
        x.color = node.color
        left_length = len(node.left) if node.left else 0
        right_length = len(node.right) if node.right else 0
        node.children = left_length + right_length
        node.color = Color.RED
        return x


    @staticmethod
    def rotateRight(node):
        x = node.left
        node.left = x.right
        x.right = node
        x.children = node.children
        x.color = node.color
        node.color = Color.RED
        left_length = len(node.left) if node.left else 0
        right_length = len(node.right) if node.right else 0
        node.children = left_length + right_length
        return x


    @staticmethod
    def isRed(node):
        if node is None or not isinstance(node, TreeNodeInRedBlackBST):
            return False
        return node.color is Color.RED


    def insert(self, node):
        # super().insert(node)
        # We need to locate where to insert the new node by using dft. Then we
        # must rotate every node in the RedBlackBST. So rescurion is our approach
        # to implement this method.
        def _insert(pivot):
            if node.val == pivot.val:
                return pivot

            pivot.children += 1
            if node.val > pivot.val:
                if not pivot.right:
                    pivot.right = node
                else:
                    # NOTE: I made a mistake here when I write RedBlackBST
                    pivot.right = _insert(pivot.right)
            else:
                if not pivot.left:
                    pivot.left = node
                else:
                    # NOTE: I made a mistake here when I write RedBlackBST
                    pivot.left = _insert(pivot.left)

            if self.isRed(pivot.right) and not self.isRed(pivot.left):
                pivot = self.rotateLeft(pivot)
            if self.isRed(pivot.left) and self.isRed(pivot.left.left):
                pivot = self.rotateRight(pivot)
            if self.isRed(pivot.left) and self.isRed(pivot.right):
                pivot.left.color = Color.BLACK
                pivot.right.color = Color.BLACK
                pivot.color = Color.RED

            return pivot

        if not isinstance(node, TreeNode):
            raise TypeError('A TreeNode object is expected.')

        if self.root is None:
            self.root = node
            self.root.color = Color.BLACK
        else:
            # The structure of the tree is modified. So _insert() should return a
            # new tree.
            self.root = _insert(self.root)

        return self.root.children


    def inOrderTraverse(self):
        # Traversal means perfoming any actions on the node.
        def _inOrderTraverse(pivot, ret=[]):
            if pivot:
                _inOrderTraverse(pivot.left)
                ret.append((pivot.val, pivot.color))
                _inOrderTraverse(pivot.right)
            return ret
        return _inOrderTraverse(self.root)



__all__ = [
    'Color',
    'TreeNodeInRedBlackBST',
    'TreeNode',
    'BinarySearchTree',
    'RedBlackBST'
]
