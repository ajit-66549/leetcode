class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # Time and Space complexity: O(n)
        stack = []
        answer = 0

        for num in nums:
            steps = 0
            while stack and stack[-1][0] <= num:
                value, death_time = stack.pop()
                steps = max(steps, death_time)

            if stack:
                steps += 1
            else:
                steps = 0

            stack.append((num, steps))
            answer = max(answer, steps)

        return answer