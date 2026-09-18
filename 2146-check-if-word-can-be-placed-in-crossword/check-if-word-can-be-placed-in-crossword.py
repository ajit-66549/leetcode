class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):

                if board[row][col] == "#":
                    continue

                for dr, dc in directions:

                    # Check the cell BEFORE the word
                    before_row = row - dr
                    before_col = col - dc

                    if 0 <= before_row < m and 0 <= before_col < n:
                        if board[before_row][before_col] != "#":
                            continue

                    # Check whether every character can be placed
                    valid = True

                    for i, letter in enumerate(word):
                        new_row = row + i * dr
                        new_col = col + i * dc

                        # Outside the board
                        if (
                            new_row < 0
                            or new_row >= m
                            or new_col < 0
                            or new_col >= n
                        ):
                            valid = False
                            break

                        cell = board[new_row][new_col]

                        # Must be empty OR contain the same letter
                        if cell != " " and cell != letter:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check the cell AFTER the word
                    after_row = row + len(word) * dr
                    after_col = col + len(word) * dc

                    if 0 <= after_row < m and 0 <= after_col < n:
                        if board[after_row][after_col] != "#":
                            continue

                    return True

        return False