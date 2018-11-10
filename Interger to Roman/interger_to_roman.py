# -*- coding: utf-8 -*-
# This is a problem about bit mapping.
mapping = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

mapping = {
    '100': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    '10' : ['', 'x', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    '1' : ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
}


def intergerToRoman(num):
    return 'M'*int((num/1000)) + mapping['100'][int(num%1000/100)] + mapping['10'][int(num%100/10)] + mapping['1'][int(num%10)]


if __name__ == '__main__':
    assert 'III' == intergerToRoman(3)
    assert 'IV' == intergerToRoman(4)
    assert 'IX' == intergerToRoman(9)
    assert 'LVIII' == intergerToRoman(58)
    assert 'MCMXCIV' == intergerToRoman(1994)
