def isAnagram( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    return list(set(t)&set(s))

y = isAnagram(s = "anagram", t = "nagaram")
print(y)


