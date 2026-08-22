class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(start) == 1 and start != result:
            return False

        i = 0
        j = 0

        while i < len(start) or j < len(result):
            while i < len(start) and start[i] == 'X':
                i += 1
            
            while j < len(result) and result[j] == 'X':
                j += 1

            if i == len(start) and j == len(result):
                return True

            if i == len(start) or j == len(result):
                return False

            if (start[i] == result[j] == 'L') and (j <= i):
                i += 1
                j += 1
            elif (start[i] == result[j] == 'R') and (j >= i):
                i += 1
                j += 1
            else:
                return False

        return True