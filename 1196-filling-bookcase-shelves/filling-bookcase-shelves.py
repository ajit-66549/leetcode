class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Time complexity: O(n*m) and Space complexity: O(n), where n = len(books) and m = shelfWidth
        dp = [0] * (len(books)+1)

        for i in range(len(books)-1, -1, -1):
            max_height = 0
            curr_width = shelfWidth
            dp[i] = float("inf")

            for j in range(i, len(books)):
                width, height = books[j]
                if curr_width < width:
                    break

                max_height = max(max_height, height)
                dp[i] = min(dp[i], dp[j+1]+max_height)
                curr_width -= width

        return dp[0]