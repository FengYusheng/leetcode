# -*- coding: utf-8 -*-
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""

import functools
import time


def time_it(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print("{0} costs {1:.3} s".format(func.__name__, time.time()-start))
        return ret
    return decorator


@time_it
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area, i, j = 0, 0, 1
    while i < len(height):
        j = i + 1
        while j < len(height):
            area = max(area, min(height[i], height[j])*(j-i))
            j += 1

        i += 1

    return area


@time_it
def maxArea2(height):
    """
    :type height: List[int]
    :rtype: int

    The area is limited by the width and the height of the shorter line. We start from the
    widest case, the length of the height array. Then shorten the width and  increase the height.
    """
    area, i, j = 0, 0, len(height)-1
    while i < j:
        area = max(area, min(height[i], height[j])*(j-i))
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1


    return area




if __name__ == '__main__':
    data = [1,8,6,2,5,4,8,3,7]
    container = maxArea(data)
    print(container)

    container = maxArea2(data)
    print(container)
