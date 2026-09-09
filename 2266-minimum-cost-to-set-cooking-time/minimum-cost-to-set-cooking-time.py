class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # Time complexity: O(n) and Space complexity: O(1), n = total time combinations
        minCost = float("inf")
        for minutes in range(100):
            second = targetSeconds - (minutes * 60)

            if 0 <= second <= 99:
                minute = str(minutes)
                sec = str(second).zfill(2)
                
                digits = (minute + sec).lstrip("0")

                current = str(startAt)
                cost = 0

                for digit in digits:
                    if digit == current:
                        cost += pushCost
                    else:
                        cost += moveCost + pushCost
                        current = digit

                minCost = min(minCost, cost)

        return minCost