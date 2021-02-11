def isPalindrome(strIn):
    str = strIn.replace(' ','')
    strLower = str.lower()
    revStr = reversed(str.lower())
    return list(revStr) == list(strLower)
