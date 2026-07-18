class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time and Space complexity: O(m*n)
        dp = [[0]*n for _ in range(m)]

        for row in range(m):
            dp[row][0] = 1

        for column in range(n):
            dp[0][column] = 1

        for row in range(1, m):
            for column in range(1, n):
                dp[row][column] = dp[row-1][column] + dp[row][column-1]

        return dp[m-1][n-1]