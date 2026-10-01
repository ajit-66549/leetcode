class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # Time complexity: O(nlogn + n + n^2m^2)
        # Space complexity: O(n + m)
        best = {}
        words.sort(key=len)
        for word in words:
            best[word] = 1

        for i in range(len(words)):
            start = words[i]
            for j in range(i+1, len(words)):
                word = words[j]
                if abs(len(word) - len(start)) != 1:
                    continue

                for k in range(len(word)):
                    new_word = word[:k] + word[k+1:]
                    if new_word in best:
                        best[word] = max(best[word], best[new_word] + 1)

        return max(best.values())