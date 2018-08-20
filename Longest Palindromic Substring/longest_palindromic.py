# -*- coding: utf-8 -*-

# Build my armory: recursion, divide and conquer.


def find_middle_index(sequence):
    return int(len(sequence)/2) if len(sequence) >= 3 else 0


def find_palindromic(sequence):
    length = len(sequence)
    i = 1
    j = 0

    if length == 1:
        palindromic = sequence[0]
    elif length == 2:
        palindromic = sequence if sequence[0] == sequence[1] else ''
    else:
        mid = find_middle_index(sequence)
        if length % 2 > 0:
            while mid-i >= 0 and mid+i < length and sequence[mid-i] == sequence[mid+i]:
                i += 1

            palindromic = sequence[mid-i+1:mid+i]
        else:
            while mid-i >= 0 and sequence[mid-i] == sequence[mid+j]:
                i += 1
                j += 1

            palindromic = sequence[mid-i+1:mid+j]

        p1 = find_palindromic(sequence[:mid])
        p2 = find_palindromic(sequence[mid:])
        print(p1, p2)

    return palindromic



__all__ = [
    'find_palindromic',
    'find_middle_index'
]
