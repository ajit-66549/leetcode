class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        # Time and Space complexity: O(sqrt(finalSum))
        if finalSum % 2 != 0:
            return []

        current = 2
        remaining = finalSum
        answer = []

        while current <= remaining:
            answer.append(current)
            remaining -= current
            current += 2

        if remaining != 0:
            answer[-1] = answer[-1] + remaining

        return answer