class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time complexity: O(m+n) and Space complexity: O(1)
        write = m + n - 1
        nums1_index = m - 1
        nums2_index = n - 1

        while nums2_index >= 0:
            if nums1_index>= 0 and nums1[nums1_index] > nums2[nums2_index]:
                nums1[write] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[write] = nums2[nums2_index]
                nums2_index -= 1
                
            write -= 1