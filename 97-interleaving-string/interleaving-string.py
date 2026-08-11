class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Time and Space complexity: O(m*n)
        m = len(s1)
        n = len(s2)

        if len(s3) != m+n:
            return False

        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    continue

                if (i < m and s1[i] == s3[i+j]):
                    dp[i][j] = dp[i+1][j]

                if (j < n and s2[j] == s3[i+j]):
                    dp[i][j] = dp[i][j] or dp[i][j+1]

        return dp[0][0]