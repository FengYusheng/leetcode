# -*- coding: utf-8 -*-
import time
import functools


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print('{0} costs {1:' '>4.3f} s'.format(func.__name__, time.time()-start))
        return ret
    return decorator



@time_it
def three_sum(array, target):
    arr = sorted(array)
    ret = []
    for i in range(0, len(arr)-2):
        t = target - arr[i]
        l, r = i+1, len(arr)-1
        while l < r:
            s = arr[l] + arr[r]
            if s == t:
                ret.append([arr[i], arr[l], arr[r]])
                break
            elif s < t:
                l += 1
            else:
                r -= 1

    return ret



if __name__ == '__main__':
    array = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, 0, 1], [-1, -1, 2]]
    actual = three_sum(array, 0)
    print(actual)
    assert expected[0] in actual and expected[1] in actual, '{0} is expected, but the actual result is {1}'.format(expected, actual)
