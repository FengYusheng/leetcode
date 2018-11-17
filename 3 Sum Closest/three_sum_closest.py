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



@time_it
def threeSumClosest(array, target):
    arr = sorted(array)
    ret = []
    for i in range(0, len(arr)-2):
        l, r = i+1, len(arr)-1
        minDeviation = abs(target-arr[i]-arr[l]-arr[r])
        ret = sorted([arr[i], arr[l], arr[r]])
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            deviation = abs(target-arr[i]-arr[l]-arr[r])

            if s == target:
                return sorted([arr[i], arr[l], arr[r]])

            if minDeviation < deviation:
                minDeviation = deviation
                ret = sorted([arr[i], arr[l], arr[r]])

            if s < target:
                l += 1
            else:
                r -= 1

    return ret



if __name__ == '__main__':
    array = [-1, 2, 1, -4]
    expected = [-1, 1, 2]
    target = 1
    actual = threeSumClosest(array, target)
    assert expected == actual, '{0} is expected, but the actual result is {1}.'.format(expected, actual)
