class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(s2) < len(s1):
            return False

        s1_frequency = [0] * 26
        window_frequency = [0] * 26
        for i in range(len(s1)):
            s1_frequency[ord(s1[i]) - ord('a')] += 1
            window_frequency[ord(s2[i]) - ord('a')] += 1
        
        if s1_frequency == window_frequency:
            return True

        for right in range(len(s1), len(s2)):
            left = right - len(s1)

            window_frequency[ord(s2[left]) - ord('a')] -= 1
            window_frequency[ord(s2[right]) - ord('a')] += 1

            if s1_frequency == window_frequency:
                return True

        return False