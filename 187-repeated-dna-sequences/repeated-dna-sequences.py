class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #Time and Space complexity: O(n)
        result = []
        word_dict = {}

        for start in range(len(s) - 9):
            word = s[start:start+10]
            word_dict[word] = word_dict.get(word, 0) + 1

        for key, value in word_dict.items():
            if value > 1:
                result.append(key)

        return result