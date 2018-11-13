# -*- coding: utf-8 -*-

def mid(array):
    return 0


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    mid_num = mid(array)
    assert mid_num == 3

    array = [1,2,3,4,5,6,7]
    mid_num = mid(array)
    assert mid_num == 4

    array = [1]
    mid_num = mid(array)
    assert mid_num == 1

    array = [1, 2]
    mid_num = mid(array)
    assert mid_num == 1
