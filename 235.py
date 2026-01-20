class MyCalendar:
    def __init__(self):
        # List to store booked intervals as [start, end)
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.booked:
            # Check if [startTime, endTime) overlaps with any existing interval
            if startTime < end and endTime > start:
                # Overlap detected, cannot book
                return False
        
        # No overlap, safe to book
        self.booked.append([startTime, endTime])
        return True










import bisect

class MyCalendar:
    def __init__(self):
        # store intervals sorted by start time
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Find position where this event should be inserted
        i = bisect.bisect_left(self.booked, (startTime, endTime))

        # Check with the previous interval
        if i > 0 and self.booked[i-1][1] > startTime:
            return False

        # Check with the next interval
        if i < len(self.booked) and self.booked[i][0] < endTime:
            return False

        # Insert the interval at the correct position
        self.booked.insert(i, (startTime, endTime))
        return True