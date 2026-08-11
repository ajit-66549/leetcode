class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(prices) <= 1:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(maxProfit, prices[i] - minPrice)

        return maxProfit