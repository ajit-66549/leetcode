class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        originalNum = x
        reversedNum = 0

        while (x!=0):
            reversedNum = (reversedNum*10) + (x%10)
            x = x // 10
        
        if reversedNum == originalNum:
            return True
        else:
            return False