class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Time complexity: O(n + (k*m*logn)), where n = len(s), k = len(words), m = avg no. char in word
        # Space complexity: O(n)
        position = {}
        for index, char in enumerate(s):
            if char not in position:
                position[char] = []
            position[char].append(index)

        answer = 0

        for word in words:
            current = -1
            valid = True
            for char in word:
                if char not in position:
                    valid = False
                    break

                positions = position[char]
                candidate = -1
                left = 0
                right = len(positions) - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    if positions[mid] > current:
                        candidate = positions[mid]
                        right = mid - 1
                    else:
                        left = mid + 1

                if candidate == -1:
                    valid = False
                current = candidate

            if valid:
                answer += 1

        return answer