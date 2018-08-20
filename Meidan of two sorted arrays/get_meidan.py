# -*- coding: utf-8 -*-

# Build my own armory: Merge sort


def merge(l1, l2):
    """
    :type l1: number list
    :type l2: number list
    :rtype: number list
    """
    length1, length2 = len(l1), len(l2)
    p1 = p2 = 0
    ret = []

    while p1 < length1 or p2 < length2:
        if p1 < length1 and p2 < length2 and l1[p1] <= l2[p2]:
            ret.append(l1[p1])
            p1 += 1
        elif p1 < length1 and p2 < length2 and l2[p2] < l1[p1]:
            ret.append(l2[p2])
            p2 += 1
        elif p1 == length1:
            ret.append(l2[p2])
            p2 += 1
        else:
            ret.append(l1[p1])
            p1 += 1

    return ret



def median(numbers1, numbers2):
    """
    :type numbers1: list
    :type numbers2: list
    :rtype: int
    """
    median = 0
    merge_array = merge(numbers1, numbers2)
    length = len(merge_array)

    if length == 1:
        median = merge_array[0]
    elif length % 2 > 0:
        median = merge_array[int(length/2)]
    else:
        median = round((merge_array[int(length/2)-1]+merge_array[int(length/2)])/2, 1)

    return median



__all__ = [
    'median',
    'merge'
]
