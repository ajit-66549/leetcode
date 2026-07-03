class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # Time and Space complexity: O(n)
        stack = [inf]
        result = 0

        for num in arr:
            while num > stack[-1]:
                mid = stack.pop()
                result += mid * min(stack[-1], num)
            stack.append(num)

        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        return result