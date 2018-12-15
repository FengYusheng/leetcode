# -*- coding: utf-8 -*-
import sys
import os
import time
import functools

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.tree.BinarySearchTree import TreeNode


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{0} costs {1:' '>4:3f}s.'.format(func.__name__, (end-start)*1000))
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



@time_it
def recorverTree(root):
    return []



if __name__ == '__main__':
    root = build([1,2,3,4,5])
