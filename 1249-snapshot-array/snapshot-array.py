class SnapshotArray:

    def __init__(self, length: int):
        # Time complexity: O(n) and Space complexity: O(n)
        self.history = [[(0, 0)] for _ in range(length)]
        self.curr_snap_id = 0

    def set(self, index: int, val: int) -> None: # S = number of entries
        # Time complexity: O(1) and Space complexity: O(n + S)
        element = self.history[index][-1]
        if element[0] == self.curr_snap_id:
            self.history[index][-1] = (self.curr_snap_id, val)
        else:
            self.history[index].append((self.curr_snap_id, val))

    def snap(self) -> int:
        # Time complexity: O(1) and Space complexity: O(1)
        self.curr_snap_id += 1
        return self.curr_snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:  # k = avg len(index_history)
        # Time complexity: O(log k) and Space complexity: O(1)
        index_history = self.history[index]

        left = 0
        right = len(index_history) - 1
        candidate = (0, 0)

        while left <= right:
            mid = left + (right - left) // 2
            id, val = index_history[mid]
            if id <= snap_id:
                candidate = (id, val)
                left = mid + 1
            else:
                right = mid - 1
        
        return candidate[1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)