class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time and Space complexity: O(log n)
        if n == 0:
            return 1

        def power(x, exponent):
            if exponent == 0:
                return 1
            
            half = power(x, exponent // 2)

            if exponent % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / power(x, -n)
        
        return pow(x, n)