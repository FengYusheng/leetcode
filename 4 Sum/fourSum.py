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


@time_it
def fourSum(array, target):
    arr = sorted(array)
    length = len(array)
    ret = []

    for i in range(0, length-2):
        for j in range(i+1, length-1):
            t = target - arr[i] - arr[j]
            l, r = j+1, length-1
            while l < r:
                if t == arr[l] + arr[r]:
                    arr_ = sorted([arr[i], arr[j], arr[l], arr[r]])
                    arr_ in ret or ret.append(sorted([arr[i], arr[j], arr[l], arr[r]]))
                    break
                elif t < arr[l] + arr[r]:
                    r -= 1
                else:
                    l += 1

    return ret



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
