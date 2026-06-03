class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time and Space complexity: O(n)
        stack = []
        answer = [0]*len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                previous_temp = stack.pop()
                answer[previous_temp] = index - previous_temp
            stack.append(index)
        return answer