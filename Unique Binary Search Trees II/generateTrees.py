# -*- coding: utf-8 -*-
# This is a problem about dynamic programming and Binary Search Tree.
# https://www.sohu.com/a/153858619_466939
# https://leetcode.com/articles/unique-binary-search-trees/
import os
import sys
import time
import functools

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.tree import BinarySearchTree


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{0} costs {1:' '>4.3f}s'.format(func.__name__, end-start))
        return ret
    return decorator


@time_it
def generateTrees(num):
    return []



if __name__ == '__main__':
    print('hhh')
