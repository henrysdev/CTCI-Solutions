"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
def stringCompression(s):
    cnt = 0
    currletter = s[0]
    newstr = ""

    for char in s:
        if char != currletter:
            newstr += currletter + str(cnt)
            if len(newstr) >= len(s):
                return s
            cnt = 0
        cnt += 1
        currletter = char

    newstr += currletter + str(cnt)
    if len(newstr) >= len(s):
        return s

    return newstr