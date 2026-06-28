class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Time and Space complexity: O(n)
        stack = []
        left = len(nums)
        right = -1

        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(j)

        if right == -1:
            return 0

        return right - left + 1