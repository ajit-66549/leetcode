from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Time complexity: O(nlog(k)) and Space complexity: O(n)
        window = SortedList()
        output = []

        for i, num in enumerate(nums):
            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])

            if len(window) == k:
                if k % 2 == 1:
                    median = window[k//2]
                else:
                    median = (window[k//2-1]+window[k//2]) / 2
                output.append(median)
        
        return output