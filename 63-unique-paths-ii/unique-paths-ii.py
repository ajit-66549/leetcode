class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time and Space complexity: O(rows * columns)
        if obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = 1

        # initialize first row
        for column in range(1, columns):
            if obstacleGrid[0][column] == 0:
                dp[0][column] = dp[0][column-1]
            
        # initialize first column
        for row in range(1, rows):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row-1][0]

        # calculate remaining cells
        for row in range(1, rows):
            for column in range(1, columns):
                if obstacleGrid[row][column] == 1:
                    dp[row][column] = 0
                else:
                    dp[row][column] = dp[row-1][column] + dp[row][column-1]

        return dp[rows-1][columns-1]