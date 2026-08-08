class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Time complexity: O(n^2) and Space complexity: O(n)
        row = [1]

        for i in range(1, rowIndex+1):
            row.append(1)

            for j in range(i-1, 0, -1):
                row[j] = row[j] + row[j-1]

        return row