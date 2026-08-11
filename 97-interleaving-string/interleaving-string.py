class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Time complexity: O(m*n) and Space complexity: O(n)
        m = len(s1)
        n = len(s2)

        if len(s3) != m+n:
            return False

        dp = [False] * (n+1)
        dp[n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    continue

                current = False
                if i < m and s1[i] == s3[i+j]:
                    current = dp[j]

                if j < n and s2[j] == s3[i+j]:
                    current = current or dp[j+1]
                
                dp[j] = current

        return dp[0]