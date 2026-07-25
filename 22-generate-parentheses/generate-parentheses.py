class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(current_parentheses, open_count, close_count):
            if open_count == n and close_count == n:
                result.append(current_parentheses)
                return

            if open_count < n:
                generate(current_parentheses + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                generate(current_parentheses + ")", open_count, close_count + 1)

        generate("", 0, 0)
        return result