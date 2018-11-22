# -*- coding: utf-8 -*-
import time
import functools


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{0} costs {1:' '>4.3f}s'.format(func.__name__, end-start))
        return ret
    return decorator


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, values):
        pass


    @classmethod
    def buildTree(cls, values):
        pass



@time_it
def inorderTraversal(root):
    '''
    :type root: TreeNode
    :rtype: List[int]
    '''
    return []


if __name__ == '__main__':
    expected = [1, 3, 2]
    actual = inorderTraversal([])
    assert expected == actual, '{0} is expected, but the actual result is {1}'.format(expected, actual)
