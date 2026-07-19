class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time complexity: O(rows * columns) and Space complexity: O(columns)
        if obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        dp = [0] * columns
        dp[0] = 1

        for row in range(rows):
            for column in range(columns):
                if obstacleGrid[row][column] == 1:
                    dp[column] = 0
                elif column > 0:
                    dp[column] = dp[column] + dp[column-1]

        return dp[-1]