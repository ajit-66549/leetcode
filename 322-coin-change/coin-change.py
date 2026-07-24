class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time complexity: O(n^2) and Space complexity: O(n)
        if amount == 0:
            return 0

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for current_amt in range(1, amount+1):
            for coin in coins:
                if current_amt - coin >= 0:
                    remaining_amt = current_amt - coin
                    coins_needed = dp[remaining_amt] + 1

                    dp[current_amt] = min(dp[current_amt], coins_needed)

        if dp[amount] == float("inf"):
            return -1

        return dp[amount]