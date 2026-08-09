class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Time and Space complexity: O(mn)
        if p == ".*":
            return True

        dp = {}
        def match(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if j == len(p):
                return i == len(s)

            firstMatch = (i < len(s)) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j+1] == "*":
                result = match(i, j+2) or (firstMatch and match(i+1, j))
            else:
                result = firstMatch and match(i+1, j+1)

            dp[(i, j)] = result
            return result

        return match(0, 0)