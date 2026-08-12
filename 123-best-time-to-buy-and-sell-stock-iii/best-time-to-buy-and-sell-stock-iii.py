class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time and complexity: O(n) and Space complexity: O(1)
        firstBuy = -float("inf")
        firstSell = 0

        secondBuy = -float("inf")
        secondSell = 0

        for price in prices:
            firstBuy = max(firstBuy, -price)
            firstSell = max(firstSell, firstBuy + price)

            secondBuy = max(secondBuy, firstSell - price)
            secondSell = max(secondSell, secondBuy + price)

        return secondSell