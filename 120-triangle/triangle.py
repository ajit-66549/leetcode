class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Time complexity: O(n^2) and Space complexity: O(n)
        if len(triangle) == 1:
            return triangle[0][0]

        dp = triangle[-1][:]

        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col+1])

        return dp[0]