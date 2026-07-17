class Solution:
    def climbStairs(self, n: int) -> int:
        # Time and Space complexity: O(n)
        memo = {0: 1, 1: 1}

        def solve(current):
            if current in memo:
                return memo[current]

            memo[current] = (solve(current - 1) + solve(current - 2))
            return memo[current]

        return solve(n)