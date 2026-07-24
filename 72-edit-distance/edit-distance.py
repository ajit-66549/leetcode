class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Time and Space complexity: O(rows * columns)
        rows = len(word1) + 1
        columns = len(word2) + 1

        dp = [[0] * columns for _ in range(rows)]

        for row in range(rows):
            dp[row][0] = row

        for column in range(columns):
            dp[0][column] = column

        for row in range(1, rows):
            for column in range(1, columns):
                if word1[row-1] == word2[column-1]:
                    dp[row][column] = dp[row-1][column-1]

                else:
                    dp[row][column] = 1 + min(dp[row-1][column-1], dp[row-1][column], dp[row][column-1])

        return dp[-1][-1]