class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Time and Space complexity: O(n)
        stack = []
        seen = set()
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in s:
            freq[char] -= 1

            if char in seen:
                continue

            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                removedChar = stack.pop()
                seen.remove(removedChar)

            stack.append(char)
            seen.add(char)

        return "".join(stack)