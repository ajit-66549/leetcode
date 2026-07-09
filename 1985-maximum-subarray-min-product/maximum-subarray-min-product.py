class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # Time and Space complexity: O(n)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        MOD = 10**9 + 7

        stack = []
        answer = 0
        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else 0

            while stack and current < nums[stack[-1]]:
                mid = stack.pop()

                left = stack[-1] if stack else -1
                right = i
                subarray_sum = prefix[right] - prefix[left + 1]

                answer = max(answer, nums[mid] * subarray_sum)

            stack.append(i)
        return answer % MOD