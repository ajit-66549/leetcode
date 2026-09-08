class MyCalendar:
# Time and Space complexity: O(n)
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        for existing_start, existing_end in self.events:
            if startTime < existing_end and endTime > existing_start:
                return False

        self.events.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)