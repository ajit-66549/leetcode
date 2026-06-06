class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Time and Space complexity: O(n)
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        total = 0

        for i in range(n + 1):
            current = arr[i] if i < n else 0

            while stack and current < arr[stack[-1]]:
                mid = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                left_count = mid - left
                right_count = right - mid

                total += arr[mid] * left_count * right_count

            stack.append(i)

        return total % MOD