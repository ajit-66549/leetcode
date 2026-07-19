class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time complexity: O(m*n) and Space complexity: O(n)
        dp = [1] * n

        for row in range(1, m):
            for column in range(1, n):
                dp[column] = dp[column] + dp[column - 1]

        return dp[n-1]