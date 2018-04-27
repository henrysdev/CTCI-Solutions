"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
def isUnique(s):
    if len(s) == 1:
        return True
    list(s).sort()
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True