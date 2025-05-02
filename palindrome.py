def polindrome(s):
    rev="".join(reversed(s))
    #Reverse the string and join it back
    return s==rev
#compare the original string with the reversed string
#Example usage:
print(polindrome("racecar"))
#True
print(polindrome("hello"))
#False
