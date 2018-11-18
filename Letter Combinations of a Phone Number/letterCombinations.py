# -*- coding: utf-8 -*-
# This is a problem about backtracing.
# https://en.wikibooks.org/wiki/Algorithms/Backtracking(depth first search or branch and bound)
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution
import time
import functools
from collections import deque


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{0} costs {1:' '>4.3f}s.'.format(func.__name__, end-start))
        return ret
    return decorator


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



@time_it
def letterCombinations(phone_num):
    ret = []

    if len(phone_num) == 0:
        ret = []
    elif len(phone_num) == 1:
        ret = [i for i in mapping[phone_num[0]]]
        # ret = list(mapping[phone_num[0]])
    elif len(phone_num) > 1:
        prev = letterCombinations(phone_num[:-1])
        ret = [i+j for i in prev for j in mapping[phone_num[-1]]]

    return ret


if __name__ == '__main__':
    phone_num = '23'
    expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    actual = letterCombinations(phone_num)
    assert expected == actual, '{0} is expected, but the actual result is {1}'.format(expected, actual)
