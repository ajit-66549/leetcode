class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time complexity: o(n) and Space complexity: O(n)
        map = {}
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in map:
                return [map[complement]+1, i+1]
            else:
                map[numbers[i]] = i
            