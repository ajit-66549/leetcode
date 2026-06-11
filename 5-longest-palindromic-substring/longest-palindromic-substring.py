class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time complexity: O(n2) and Space complexity: O(1)
        result = ""

        def checkPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        for i in range(len(s)):
            odd = checkPalindrome(i, i)
            even = checkPalindrome(i, i+1)

            if len(odd) > len(result):
                result = odd
            
            if len(even) > len(result):
                result = even
        
        return result