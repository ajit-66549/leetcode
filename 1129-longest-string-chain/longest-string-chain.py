class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # Time complexity: O(nlogn + nm^2)
        # Space complexity: O(n + m)
        best = {}
        words.sort(key=len)
        for word in words:
            best[word] = 1

        for i in range(len(words)):
            word = words[i]

            for j in range(len(word)):
                new_word = word[:j] + word[j+1:]
                if new_word in best:
                    best[word] = max(best[word], best[new_word] + 1)

        return max(best.values())