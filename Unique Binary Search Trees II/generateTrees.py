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


def sequenceGenerate(num, start=1, ret=[]):
    sequence = ['-'] + [i for i in range(start, num+1)]
    ret = []
    if num < start:
        return ret
    
    return ret


@time_it
def generateTrees(num):
    return []



if __name__ == '__main__':
    num = 3
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

    # Let's think about it from the simplest case
    seq = [1,2]
    actual = sequenceGenerate(2)
    expected = [[1,2], [2,1]]
    seq = [1, 2, 3]
    actual = sequenceGenerate(3)
    expected = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
