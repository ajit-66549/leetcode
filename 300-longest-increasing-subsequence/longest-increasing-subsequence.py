class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time complexity: O(n log n) and Space complexity: O(n)
        subsequence = []

        for num in nums:
            if not subsequence or num > subsequence[-1]:
                subsequence.append(num)
            else:
                #find the num in subsequence > num, and replace
                left = 0
                right = len(subsequence) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if subsequence[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                subsequence[left] = num
        return len(subsequence) 