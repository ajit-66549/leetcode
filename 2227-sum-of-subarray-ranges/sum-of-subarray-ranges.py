class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # Time and Space complexity: O(n)
        if len(nums) == 1:
            return 0

        answer = 0
        maximum_stack = []

        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else float("inf")

            while maximum_stack and current >= nums[maximum_stack[-1]]:
                mid = maximum_stack.pop()
                left = maximum_stack[-1] if maximum_stack else -1
                left_choices = mid - left
                right_choices = i - mid
                answer += nums[mid] * left_choices * right_choices

            maximum_stack.append(i)

        minimum_stack = []

        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else float("-inf")

            while minimum_stack and current <= nums[minimum_stack[-1]]:
                mid = minimum_stack.pop()
                left = minimum_stack[-1] if minimum_stack else -1
                left_choices = mid - left
                right_choices = i - mid
                answer -= nums[mid] * left_choices * right_choices
            
            minimum_stack.append(i)

        return answer