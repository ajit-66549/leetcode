class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        counts = [0] * numSlots
        memo = {}
        def solve(i, counts):
            if i == len(nums):
                return 0

            key = (i, tuple(counts))
            if key in memo:
                return memo[key]

            choice_score = 0
            for slot in range(1, numSlots+1):
                if counts[slot - 1] == 2:
                    continue

                counts[slot - 1] += 1
                choice_score = max(choice_score, (nums[i] & slot) + solve(i+1, counts))
                counts[slot - 1] -= 1

            memo[key] = choice_score
            return choice_score

        return solve(0, counts)