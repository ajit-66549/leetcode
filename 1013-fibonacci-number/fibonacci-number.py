class Solution:
    def fib(self, n: int) -> int:
        # Time and Space complexity: O(n)
        memo = {}

        def fibonacciNum(n):
            if n == 0:
                return 0
            if n == 1:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = fibonacciNum(n - 1) + fibonacciNum(n - 2)
            return memo[n]

        return fibonacciNum(n)