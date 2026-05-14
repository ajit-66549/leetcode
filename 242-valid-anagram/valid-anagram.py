class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity: O(n) and Space complexity: O(n)
        if len(s) != len(t):
            return False

        map = {}

        for letter in s:
            map[letter] = map.get(letter, 0) + 1
        
        for letter in t:
            if letter not in map:
                return False
            
            map[letter] -= 1

            if map[letter] < 0:
                return False
        
        return True