class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(needle) > len(haystack):
            return -1

        for start in range(len(haystack)):
            if haystack[start:start+len(needle)] == needle:
                return start
        
        return -1