# -*- coding: utf-8 -*-
# Build my own armory: numbers in Python

import sys
import string

SIGN_BIT = 0

def atoi(digits):
    def _checkSignBit():
        global SIGN_BIT
        SIGN_BIT = 0

        if digits[0] == '-':
            SIGN_BIT = SIGN_BIT | (1<<31)
        elif digits[0] == '+':
            SIGN_BIT = SIGN_BIT | (1<<30) # Skip '+'
        elif digits[0] == 0 and digits[1] in 'xX':
            SIGN_BIT = SIGN_BIT | (1<<29) # hex
        elif digits[0] == 0 and digits[1] in string.digits:
            SIGN_BIT = SIGN_BIT | (1<<28) # oct
        elif digits[0] not in string.digits:
            SIGN_BIT = SIGN_BIT | (1<<27)

    number = 0

    _checkSignBit()

    isNegative = ((SIGN_BIT >> 31)&1) > 0
    if isNegative or ((SIGN_BIT >> 30)&1) > 0:
        digits = digits[1:]

    if ((SIGN_BIT)>>27) & 1 == 0:
        for i in digits:
            if i not in string.digits:
                break

            number = number * 10 + (ord(i) - ord('0'))
            if number > sys.maxsize:
                raise ValueError('"digits" is beyond sys.maxsize')

    number = 0 - number if isNegative else number

    return number



__all__ = [
    'atoi'
]
