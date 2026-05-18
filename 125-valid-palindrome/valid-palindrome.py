class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity: O(n) and Space complexity: O(1)
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1  
                continue
            
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1 
        return True