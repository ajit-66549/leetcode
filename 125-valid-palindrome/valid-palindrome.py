class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time and Space complexities: O(n)
        new_s = "".join([letter for letter in s if letter.isalnum()]).lower()
        start = 0
        end = len(new_s) - 1
        while start < end:
            if new_s[start] != new_s[end]:
                return False
            else:
                start += 1
                end -= 1

        return True