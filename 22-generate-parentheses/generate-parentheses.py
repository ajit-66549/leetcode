class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time and Space complexity: O(nCn​)
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]

        for i in range(1, n+1):
            for inside_pairs in range(i):
                remaining_pairs = i - 1 - inside_pairs

                for inside_string in dp[inside_pairs]:
                    for remaining_string in dp[remaining_pairs]:
                        new_string = ("(" + inside_string + ")" + remaining_string)

                        dp[i].append(new_string)

        return dp[n]