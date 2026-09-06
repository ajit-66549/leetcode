class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Time complexity: O(np+nlogn) and Space complexity: O(n)
        def get_power(x):
            operations = 0
            while x != 1:
                if x % 2 == 0:
                    x = x// 2
                else:
                    x = 3 * x + 1
                operations += 1
            return operations
        
        store = []
        for start in range(lo, hi+1):
            powers = get_power(start)
            store.append((powers, start))

        sorted_store = sorted(store)

        _, num = sorted_store[k-1]
        return num