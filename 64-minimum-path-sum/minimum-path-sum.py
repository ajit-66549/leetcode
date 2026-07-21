class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time and Space complexity: O(rows * columns)
        rows = len(grid)
        columns = len(grid[0])

        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # first row
        for column in range(1, columns):
            dp[0][column] = grid[0][column] + dp[0][column-1]

        # first columns
        for row in range(1, rows):
            dp[row][0] = grid[row][0] + dp[row-1][0]

        # remaining cells
        for row in range(1, rows):
            for column in range(1, columns):
                dp[row][column] = grid[row][column] + min(dp[row-1][column], dp[row][column-1])

        return dp[rows-1][columns-1]