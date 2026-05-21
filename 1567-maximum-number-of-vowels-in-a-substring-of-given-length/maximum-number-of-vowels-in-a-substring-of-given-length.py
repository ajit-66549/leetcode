class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Time and Space complexity: O(n)
        vowel = set("aeiou")
        count = 0

        for i in range(k):
            if s[i] in vowel:
                count += 1
        
        result = count

        for right in range(k, len(s)):
            left = right - k
            if s[left] in vowel:
                count -= 1
            if s[right] in vowel:
                count += 1
            result = max(result, count)

        return result