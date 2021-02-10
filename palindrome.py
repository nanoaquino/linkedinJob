def isPalindrome(str):
    strLower = str.lower()
    revStr = reversed(str.lower())
    return list(revStr) == list(strLower)