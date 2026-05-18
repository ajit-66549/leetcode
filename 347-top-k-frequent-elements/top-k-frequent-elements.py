class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []

        for num in nums:
            map[num] = map.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums)+1)]

        for num, count in map.items():
            bucket[count].append(num)
        
        for count in range(len(bucket)-1, 0, -1):
            for num in bucket[count]:
                result.append(num)
                if len(result) == k:
                    return result
