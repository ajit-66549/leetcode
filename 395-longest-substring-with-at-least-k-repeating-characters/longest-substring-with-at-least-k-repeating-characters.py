class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Time complexity: O(n2)and Space complexity: O(n)
        if len(s) < k:
            return 0

        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1

        for char in char_dict:
            if char_dict[char] < k:
                result = 0

                parts = s.split(char)
                for part in parts:
                    result = max(result, self.longestSubstring(part, k))

                return result
        return len(s)