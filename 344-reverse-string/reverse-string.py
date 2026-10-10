class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time and Space complexity: O(n)
        def swapLetters(start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]

            swapLetters(start+1, end-1)

        swapLetters(0, len(s)-1)