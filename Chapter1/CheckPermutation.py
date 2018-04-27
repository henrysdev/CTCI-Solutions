"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""
def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    charmap = {}
    for ch in s1:
        if ch in charmap:
            charmap[ch] += 1
        else:
            charmap[ch] = 1
    for ch in s2:
        if ch not in charmap:
            return False
    return True