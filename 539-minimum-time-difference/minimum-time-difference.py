class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Time complexity: O(n) and Space compelxity: O(1)
        seen = [False] * 1440
        minMinute = float("inf")
        previous = -1
        first = -1

        for time in timePoints:
            hour, minute = time.split(":")
            totalMinute = (int(hour) * 60) + int(minute)

            if seen[totalMinute]:
                return 0
            seen[totalMinute] = True

        for i in range(1440):
            if seen[i]:
                if previous == -1:
                    previous = i
                    first = i
                else:
                    minMinute = min(minMinute, i - previous)
                    previous = i

        minMinute = min(minMinute, 1440 + first - previous)

        return minMinute