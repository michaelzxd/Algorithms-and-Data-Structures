

from test import testEqual
def removeWhite(s):
    s.replace(" ", "")
    s.replace("‘", "")
    return s

def isPal(s):
    if len(s) == 1 or len(s) == 0:
        return True
    
    for i in range(len(s)//2):
        if s[i] == s[-1-i]:
            return True
        else:
            return False

testEqual(isPal(removeWhite("x")),True)
testEqual(isPal(removeWhite("radar")),True)
testEqual(isPal(removeWhite("hello")),False)
testEqual(isPal(removeWhite("")),True)
testEqual(isPal(removeWhite("hannah")),True)
testEqual(isPal(removeWhite("madam i'm adam")),True)
