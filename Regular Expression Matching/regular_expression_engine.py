# -*- coding: utf-8 -*-

# Build my own armory: dynamic program 动态规划
# https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/

# http://www.hawstein.com/posts/dp-novice-to-advanced.html

def isMatch(sequence, pattern):
    """
    1. pattern doesn't contain "*", this is the simplest case, just compare two strings.
    2. Pattern contains "*", "*" makes this problem complicatedself.
        (1) ".*" always matches any strings.
        (2) If "*" comes after a character, it matches all the preceding characters.
    """
    def _dp(i, j):
        if j < len(pattern) and i < len(sequence):
            if j+1 < len(pattern) and pattern[j+1] == '*':
                matched = pattern[j] in (sequence[i], '.')

                if matched:
                    matched = _dp(i+1, j)
                elif j+2 < len(pattern):
                    matched = pattern[j+2] in (sequence[i], '.')
                    if matched and j+3 < len(pattern) and pattern[j+3] == '*':
                        matched = _dp(i+1, j+2)
                    elif matched and j+3 < len(pattern) and pattern[j+3] != '*':
                        matched = _dp(i+1, j+3)

            else:
                matched = pattern[j] in (sequence[i], '.') and _dp(i+1, j+1)

        else:
            matched = i == len(sequence)

        return matched

    return _dp(0, 0)



__all__ = [
    'isMatch'
]
