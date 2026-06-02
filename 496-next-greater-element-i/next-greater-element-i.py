class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time complexity: O(n2) and Space complexity: O(1)
        result = []

        for num in nums1:
            position = nums2.index(num)
            greater_element = -1
            
            for i in range(position+1, len(nums2)):
                if nums2[i] > num:
                    greater_element = nums2[i]
                    break
            result.append(greater_element)
        
        return result