class Solution:
    def reverseWords(self, s: str) -> str:
        # Time and Space complexity: o(n)
        right = len(s) - 1
        result = []

        while right >= 0:
            while right >= 0 and s[right] == " ":
                right -= 1

            if right < 0:
                break

            end = right
            start = right

            while start >= 0 and s[start] != " ":
                start -= 1

            word = s[start+1 : end+1]
            result.append(word)

            right = start

        return " ".join(result)
