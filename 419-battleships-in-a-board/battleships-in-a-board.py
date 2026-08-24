class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Time complexity: O(m*n) and Space complexity: O(1)
        battleships = 0
        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    continue

                if (r==0 or board[r-1][c] != 'X') and (c==0 or board[r][c-1] != 'X'):
                    battleships += 1

        return battleships