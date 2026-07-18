class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Time and Space compelxity: O(n)
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for jump in range(1, 4):
                previous = i - jump
                
                if previous >= 0:
                    candidate = dp[previous] + costs[i - 1] + jump**2
                    dp[i] =min(dp[i], candidate)

        return dp[n]