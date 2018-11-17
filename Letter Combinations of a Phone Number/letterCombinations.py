# -*- coding: utf-8 -*-
# This is a problem about backtracing.
# https://en.wikibooks.org/wiki/Algorithms/Backtracking
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
    mapping = {
        '0' : '',
        '1' : '',
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
    }

    return []


if __name__ == '__main__':
    phone_num = '23'
    expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    actual = letterCombinations(phone_num)
    assert expected == actual, '{0} is expected, but the actual result is {1}'.format(expected, actual)
