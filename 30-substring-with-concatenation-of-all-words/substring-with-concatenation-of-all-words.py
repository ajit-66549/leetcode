from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Time and Space complexity: O(n)
        word_length = len(words[0])
        word_count = len(words)
        result = []

        need = {}
        for word in words:
            need[word] = need.get(word, 0) + 1

        for start in range(word_length):
            left = start
            current = defaultdict(int)
            counter = 0

            for right in range(start, len(s)-word_length+1, word_length):
                word = s[right : right+word_length]

                if word in need:
                    current[word] += 1
                    counter += 1

                    while current[word] > need[word]:
                        left_word = s[left:left+word_length]
                        current[left_word] -= 1
                        counter -= 1
                        left += word_length

                    if counter == word_count:
                        result.append(left)
                else:
                    current.clear()
                    counter = 0
                    left = right + word_length
        return result