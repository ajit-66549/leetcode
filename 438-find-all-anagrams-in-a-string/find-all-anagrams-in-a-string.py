class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Time and Space complexity: O(n)
        if len(p) > len(s):
            return []
        count = [0] * 26
        window_count = [0] * 26
        result = []

        for i in range(len(p)):
            count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1

        if count == window_count:
            result.append(0)
        
        for right in range(len(p), len(s)):
            left = right - len(p)

            window_count[ord(s[left]) - ord('a')] -= 1
            window_count[ord(s[right]) - ord('a')] += 1

            if count == window_count:
                result.append(left+1)

        return result