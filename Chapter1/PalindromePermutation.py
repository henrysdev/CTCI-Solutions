"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""
def palindromePerm(s):
    if len(s) == 1:
        return True
    charmap = {}
    for ch in s:
        if ch in charmap:
            charmap[ch] += 1
        else:
            charmap[ch] = 1
    midletter = len(s) % 2
    for key in charmap:
        if charmap[key] % 2 != 0:
            if midletter:
                midletter = 0
            else:
                return False
    return True