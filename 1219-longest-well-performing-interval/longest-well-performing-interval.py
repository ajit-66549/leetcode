class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # Time and Space complexity: O(n)
        prefix = [0]
        for hour in hours:
            score = 1 if hour > 8 else -1
            prefix.append(prefix[-1] + score)

        stack = []
        for i, num in enumerate(prefix):
            if not stack or num < prefix[stack[-1]]:
                stack.append(i)

        answer = 0
        for right in range(len(prefix)-1, -1, -1):
            while stack and prefix[right] > prefix[stack[-1]]:
                answer = max(answer, right - stack[-1])
                stack.pop()
            
        return answer