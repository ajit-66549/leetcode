class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # Time complexity: O(Sm + Tm) and Space complexity: O(S), S = len(startWords) and m = maximum word length
        start_set = set()
        count = 0
        for word in startWords:
            mask = 0
            for letter in word:
                bit = ord(letter) - ord('a')
                mask |= (1 << bit)  # turn one each letter in word
            start_set.add(mask)

        for word in targetWords:
            mask = 0
            for letter in word:
                bit = ord(letter) - ord('a')
                mask |= (1 << bit)  # turn one each letter in word

            for letter in word:
                bit = ord(letter) - ord('a')
                new_mask = mask ^ (1 << bit)  # XOR operation to remove the letter

                if new_mask in start_set:
                    count += 1
                    break
        
        return count