class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Time complexity: O(n log n) and Space compelxity: O(n)
        minutes = []
        minMinute = float("inf")

        for time in timePoints:
            hour, minute = time.split(":")
            totalMinute = (int(hour) * 60) + int(minute)
            minutes.append(totalMinute)

        minutes.sort()
        first = minutes[0]
        last = minutes[-1]

        for i in range(1, len(minutes)):
            minMinute = min(minMinute, minutes[i] - minutes[i-1])

        minMinute = min(minMinute, 1440 + first - last)

        return minMinute