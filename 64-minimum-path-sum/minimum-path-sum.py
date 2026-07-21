class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time complexity: O(rows * columns) and Space complexity: O(columns)
        rows = len(grid)
        columns = len(grid[0])

        dp = [0] * columns
        dp[0] = grid[0][0]

        # first row 
        for column in range(1, columns):
            dp[column] = dp[column-1] + grid[0][column]

        for row in range(1, rows):
            for column in range(columns):
                if column == 0:
                    dp[column] = dp[column] + grid[row][column]
                    continue

                dp[column] = grid[row][column] + min(dp[column], dp[column-1])

        return dp[-1]