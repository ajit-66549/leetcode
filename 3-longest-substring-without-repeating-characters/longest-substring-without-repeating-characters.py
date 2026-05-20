class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time and Space complexity: O(n)
        max_length = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length