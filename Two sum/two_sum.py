# -*- coding: utf-8 -*-



def two_sum(numbers, target):
    indices = None

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                indices = (i, j)
                break

    return indices



__all__ = [
    "two_sum"
]



if __name__ == '__main__':
    indices = two_sum([2, 7, 11, 15], 26)
    print(indices)
