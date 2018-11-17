# -*- coding: utf-8 -*-
import time
import functools


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        return ret
    return decorator


@time_it
def letterCombinations(phone_num):
    return []


if __name__ == '__main__':
    phone_num = '23'
    expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    actual = letterCombinations(phone_num)
    assert expected == actual, '{0} is expected, but the actual result is {1}'.format(expected, actual)
