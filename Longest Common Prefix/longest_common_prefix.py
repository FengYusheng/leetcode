# -*- coding: utf-8 -*-
# This is a problem about "Trie", "Binary Search" and "Divide and Conqure" tenchniqual.

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
def lcp0(strings):
    '''This is my first idea and it's really ugly.'''
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


@time_it
def lcp1(strings):
    '''This looks more comfortable.'''
    prefix, length, i = strings[0], len(strings[0]), 1
    while i < len(strings):
        while strings[i].find(prefix) != 0:
            if not length:
                break;

            length -= 1
            prefix = strings[0][:length]

        i += 1

    return prefix


@time_it
def lcp2(strings):
    '''This idea is the same to lcp0's and looks more compfortable.

    Trick: 'abc'[0:0] => ''
    '''
    prefix, length, i, j = strings[0], len(strings[0]), 0, 1
    while i < length:
        j = 1
        while j < len(strings):
            if i >= len(strings[j]) or strings[j][i] != prefix[i]:
                return prefix[:i]

            j += 1

        i += 1

    return prefix



@time_it
def lcp(strings):
    '''
    Divide and Conqure. This is identity to lcp0, but the structure of the codes
    looks more comfortable.
    '''
    def _merge(left, right):
        prefix = ''
        length = min(len(left), len(right))
        i = 0

        while i < length:
            if left[i] == right[i]:
                prefix += left[i]
                i += 1
            else:
                break

        return prefix


    def _lcp(l, r):
        if l >= r:
            return strings[l]

        mid = int((l+r)/2)
        left_common_prefix = _lcp(l, mid)
        right_common_prefix = _lcp(mid+1, r)
        return _merge(left_common_prefix, right_common_prefix)

    return _lcp(0, len(strings)-1)



if __name__ == '__main__':
    fmt = '{0} is expected, the actual result is {1}'

    actual = lcp(strings1)
    assert 'fl' == actual, fmt.format('fl', actual)

    actual = lcp(strings2)
    assert '' == actual, fmt.format('', actual)

    actual = lcp(strings3)
    assert 'lee' == actual, fmt.format('', actual)
