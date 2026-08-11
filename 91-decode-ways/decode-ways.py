class Solution:
    def numDecodings(self, s: str) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        next1 = 1
        next2 = 0

        for i in range(len(s) - 1, -1, -1):
            current = 0

            if s[i] != "0":
                current = next1

            if i + 1 < len(s):
                if "10" <= s[i:i+2] <= "26":
                    current += next2

            next2 = next1
            next1 = current

        return next1