class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # Base case: position == n
        next_dp = [[1] * 3 for _ in range(2)]

        for position in range(n - 1, -1, -1):
            curr_dp = [[0] * 3 for _ in range(2)]

            for absent in range(2):
                for late in range(3):

                    # Present (P)
                    total = next_dp[absent][0]

                    # Late (L)
                    if late < 2:
                        total += next_dp[absent][late + 1]

                    # Absent (A)
                    if absent < 1:
                        total += next_dp[absent + 1][0]

                    curr_dp[absent][late] = total % MOD

            # Move to the previous position
            next_dp = curr_dp

        return next_dp[0][0]
