# -*- coding: utf-8 -*-
# http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
import sys
import os
import time
import functools

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.tree.BinarySearchTree import TreeNode

# prev = first = second = None

def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{0} costs {1:' '>4.3f}s.'.format(func.__name__, (end-start)*1000))
        return ret
    return decorator


def insert(root, node):
    if not root:
        return node

    pivot = root
    while pivot:
        if not pivot.left:
            pivot.left = node
            break
        elif not pivot.right:
            pivot.right = node
            break
        elif pivot.left:
            pivot = pivot.left
        else:
            pivot = pivot.right

    return root


def build(numbers):
    root = None
    for n in iter(numbers):
        root = insert(root, TreeNode(n)) if root else TreeNode(n)
    return root


def dft(root, ret=[]):
    if root:
        dft(root.left, ret)
        ret.append(root.val)
        dft(root.right, ret)
    return ret



@time_it
def recorverTree(root):
    '''
    I have spent too many hours to consider the cases which are beyond this problem itself.
    I should stop to focus on this problem itself. We can get a sorted array when we
    in-order traverse a binary search tree. Given the description of the problem, only two
    elements among this array should be swapped. These tow elements are either
    larger than the elments after them or smaller than the elements before them.

    Treat a binary search tree as a sorted arrary. Every element should be smaller
    than the elements before it.
    3, 2, 1: swap 3(first) and 1(second)
    1, 3, 2, 4: swap 3(first) and 2(second)
    The "deep first traverse" method finds out the two error elements.

    Note: I don't know why my submission failed when I implmented this method with global variables.
    '''
    def _dft(pivot, elements=[None, None, None]):
        # global prev, first, second
        if pivot:
            _dft(pivot.left, elements)
            if elements[0]:
                if elements[0].val > pivot.val and not elements[1]:
                    elements[1] = elements[0]
                    elements[2] = pivot
                elif elements[0].val > pivot.val:
                    elements[2] = pivot

            elements[0] = pivot
            _dft(pivot.right, elements)

    elements = [None, None, None]
    _dft(root, elements)
    if elements[1]:
        elements[1].val, elements[2].val = elements[2].val, elements[1].val


if __name__ == '__main__':
    root = build([1,2,3])
    # print(dft(root))
    recorverTree(root)
    # print(dft(root, ret=[]))
