class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        numtoString = str(x)
        reverseNum = int(numtoString[::-1])
        
        if reverseNum == x:
            return True
        else:
            return False