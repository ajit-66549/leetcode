class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Time and Space complexity: O(n^2)
        answer = []
        previousRow = [1]

        for i in range(numRows):
            currentRow = [1] * (i + 1)

            for j in range(1, i):
                currentRow[j] = previousRow[j - 1] + previousRow[j]

            answer.append(currentRow)
            previousRow = currentRow

        return answer