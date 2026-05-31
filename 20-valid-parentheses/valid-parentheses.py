class Solution:
    def isValid(self, s: str) -> bool:
        # Time and Space complexity: O(n)
        stackList = []
        bracketMapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for bracket in s:
            if bracket in "({[":
                stackList.append(bracket)
            else:
                if not stackList or stackList[-1] != bracketMapping[bracket]:
                    return False
                stackList.pop()
        
        return len(stackList) == 0