class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time and Space complexity: O(n)
        if len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        have = 0
        need_count = len(need)

        left = 0
        result = ""
        min_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result