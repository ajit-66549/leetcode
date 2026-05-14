class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time complexity: O(n * k)
        # Space complexity: O(n * k), where n = number of words in strs, k = number of letters in each word

        map = {}

        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in map.keys():
                map[key] = []
            map[key].append(word)
        
        return list(map.values())