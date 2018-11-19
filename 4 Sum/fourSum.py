# -*- coding: utf-8 -*-
# This is a prolem about Subset Sum Problem.
# https://en.wikipedia.org/wiki/Subset_sum_problem
import time
import functools


def time_it(func):
    @functools.wraps(func)
    def decorater(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{0} costs {1:' '>4.3f}s'.format(func.__name__, end-start))
        return ret
    return decorater



def fourSum(array, target):
    return []



if __name__ == '__main__':
    array = [1, 0, -1, 0, -2, 2]
    target = 0
    actual = fourSum(array, target)
    expected = [
        [-1, 0, 0, 1],
        [-2, -1, 1, 2],
        [-2, 0, 0, 2]
    ]

    assert len(actual) == 3
    for i in actual:
        assert i in expected
