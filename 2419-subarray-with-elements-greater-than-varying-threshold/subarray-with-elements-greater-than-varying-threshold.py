class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        # Time and Space complexity: O(n)
        stack = []

        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else 0

            while stack and current <= nums[stack[-1]]:
                mid = stack.pop()
                left = stack[-1] if stack else -1
                width = i - left - 1

                if nums[mid] * width > threshold:
                    return width

            stack.append(i)

        return -1