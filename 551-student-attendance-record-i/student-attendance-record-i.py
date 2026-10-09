class Solution:
    def checkRecord(self, s: str) -> bool:
        # Time complexity: O(n) and Space complexity: O(1)
        absent_count = 0
        late_count = 0

        for char in s:
            if char == "L":
                late_count += 1
            else:
                late_count = 0

            if char == "A":
                absent_count += 1

            if late_count >= 3 or absent_count >= 2:
                return False

        return True