# -*- coding: utf-8 -*-
# This is a problem about bitmap.

mapping = {
    'I'  : 1,
    'IV' : 4,
    'V'  : 5,
    'IX' : 9,
    'X'  : 10,
    'XL' : 40,
    'L'  : 50,
    'XC' : 90,
    'C'  : 100,
    'CD' : 400,
    'D'  : 500,
    'CM' : 900,
    'M'  : 1000
}

def RomanToInterger(roman):
    i = num = 0
    while i < len(roman)-1:
        if roman[i] == 'C' and roman[i+1] == 'M':
            i += 1
            num += mapping['CM']
        elif roman[i] == 'C' and roman[i+1] == 'D':
            i += 1
            num += mapping['CD']
        elif roman[i] == 'X' and roman[i+1] == 'C':
            i += 1
            num += mapping['XC']
        elif roman[i] == 'X' and roman[i+1] == 'L':
            i += 1
            num += mapping['XL']
        elif roman[i] == 'I' and roman[i+1] == 'X':
            i += 1
            num += mapping['IX']
        elif roman[i] == 'I' and roman[i+1] == 'V':
            i += 1
            num += mapping['IV']
        else:
            num += mapping[roman[i]]

        i += 1

    if i < len(roman):
        num += mapping[roman[i]]

    return num


if __name__ == '__main__':
    assert 3 == RomanToInterger("III")
    assert 4 == RomanToInterger("IV")
    assert 9 == RomanToInterger('IX')
    assert 58 == RomanToInterger('LVIII')
    assert 1994 == RomanToInterger('MCMXCIV')
