"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""
def oneAway(s1, s2):
    if len(s1) == len(s2):
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
            if diff > 1:
                return False
        return True

    elif abs(len(s1) - len(s2)) == 1:
        if len(s1) < len(s2):
            if s1 in s2:
                return True
        if len(s2) < len(s1):
            if s2 in s1:
                return True
    return False