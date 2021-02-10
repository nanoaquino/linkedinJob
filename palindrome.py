def isPalindrome(str):
    revStr = reversed(str.lower())
    return list(str) == list(revStr)