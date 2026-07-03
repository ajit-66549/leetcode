class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Time complexity: O(n) and Space compexity: O(1)
        n = len(arr)

        # find sorted prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:    # array is sorted
            return 0

        # find sorted suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1


        answer = min(n - left - 1, right)
        i = 0
        j = right

        while i <= left and j < n:
            if arr[i] <= arr[j]:
                answer = min(answer, j - i - 1)
                i += 1
            else:
                j += 1

        return answer