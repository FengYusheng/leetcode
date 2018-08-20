# -*- coding: utf-8 -*-

# Build my own armory: clear repeated characters.

def find_longest_substring(s=''):
    substring  = ''
    current = ''

    for i in s:
        if i not in current:
            current += i
        else:
            substring = current if len(substring) < len(current) else substring
            current = i

    return substring, len(substring)



__all__ = [
    'find_longest_substring'
]


if __name__ == '__main__':
    substring, _ = find_longest_substring('pwwkew')
    print(substring)
