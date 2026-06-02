class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Time ans Space complexity: O(n)
        result = [-1] * len(nums)
        stack = []

        for i in range(2 * len(nums)):
            index = i % len(nums)
            while stack and nums[index] > nums[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = nums[index]

            if i < len(nums):
                stack.append(i)

        return result