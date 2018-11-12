# -*- coding: utf-8 -*-

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


def lcp(strings):
    return ''


if __name__ == '__main__':
    fmt = '{0} is expected, the actual result is {1}'

    actual = lcp(strings1)
    assert 'fl' == actual, fmt.format('fl', actual)

    actual = lcp(strings2)
    assert '' == actual, fmt.format('', actual)

    actual = lcp(strings3)
    assert 'lee' == actual, fmt.format('', actual)
