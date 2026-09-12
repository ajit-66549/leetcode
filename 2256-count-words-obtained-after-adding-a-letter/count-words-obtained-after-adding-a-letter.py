class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set()
        count = 0
        for word in startWords:
            sorted_word = "".join(sorted(word))
            start_set.add(sorted_word)

        for word in targetWords:
            sorted_word = "".join(sorted(word))

            for i in range(len(sorted_word)):
                new_word = sorted_word[:i] + sorted_word[i+1:]
                 
                if new_word in start_set:
                    count += 1
                    break
        
        return count