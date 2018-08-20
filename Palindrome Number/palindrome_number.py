# -*- coding: utf-8 -*-

def palindrome(number):
    isPalindrome = False
    reversedNumber = 0
    _number = number

    if number < 0:
        isPalindrome = False
    elif number % 10 == 0:
        isPalindrome = False
    else:
        while _number > 0:
            reversedNumber = reversedNumber * 10 + _number % 10
            _number = int(_number/10)

        isPalindrome = reversedNumber == number

    return isPalindrome


__all__ = [
    'palindrome'
]
