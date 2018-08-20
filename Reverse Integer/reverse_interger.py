# -*- coding: utf-8 -*-

def reverse(number):
    """
    :type number: int
    :rtype: int
    """
    negative = number < 0
    number = abs(number)
    new_number = 0
    digits = []

    while number > 0:
        digits.append(number%10)
        number = int(number/10)

    for i in digits:
        new_number = new_number * 10 + i

    if negative:
        new_number = 0 - new_number

    return new_number



__all__ = [
    'reverse'
]
