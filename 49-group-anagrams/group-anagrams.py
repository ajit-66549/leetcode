class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time complexity: O(n * klog(k))
        # Space complexity: O(n*k), where n = number of words in strs, k = number of letters in each word

        map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in map.keys():
                map[sorted_word].append(word)
            else:
                map[sorted_word] = [word]
        
        return list(map.values())