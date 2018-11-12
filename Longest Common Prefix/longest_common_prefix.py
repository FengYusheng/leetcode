# -*- coding: utf-8 -*-
# This is a problem about "Trie"

import functools
import time

strings1 = [
    'flower',
    'flow',
    'fligth'
]

strings2 = [
    'dog',
    'racecar',
    'car'
]

strings3 = [
    'leetcode',
    'leets',
    'leet',
    'leed'
]


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print('{0} costs {1:' '>4.3f} s'.format(func.__name__, time.time()-start))
        return ret

    return decorator


@time_it
def lcp(strings):
    '''This function is really ugly.'''

    shortest, i, j = len(strings[0]), 0, 1
    prefix = ''

    for s in strings:
        if len(s) < shortest:
            shortest = len(s)

    while i < shortest:
        j = 0
        while j < len(strings):
            if strings[j][i] != strings[0][i]:
                break

            j += 1

        if j == len(strings):
            prefix += strings[0][i]

        if len(prefix) == 0:
            break

        i += 1

    return prefix





if __name__ == '__main__':
    fmt = '{0} is expected, the actual result is {1}'

    actual = lcp(strings1)
    assert 'fl' == actual, fmt.format('fl', actual)

    actual = lcp(strings2)
    assert '' == actual, fmt.format('', actual)

    actual = lcp(strings3)
    assert 'lee' == actual, fmt.format('', actual)
