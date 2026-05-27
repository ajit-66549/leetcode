class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        count = {}
        max_frequency = 0
        result = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        return result