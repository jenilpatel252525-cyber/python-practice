class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Step 1: check triple booking
        for s, e in self.overlaps:
            if startTime < e and endTime > s:
                return False

        # Step 2: record new double bookings
        for s, e in self.booked:
            if startTime < e and endTime > s:
                self.overlaps.append((max(startTime, s), min(endTime, e)))

        # Step 3: store event
        self.booked.append((startTime, endTime))
        return True








import bisect

class MyCalendar:
    def __init__(self):
        # store intervals sorted by start time
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Find position where this event should be inserted
        i = bisect.bisect_left(self.booked, (startTime, endTime))
        count=0
        
        # Check with the previous interval
        if i > 0 and self.booked[i-1][1] > startTime:
            count+=1

        if i-1 > 0 and self.booked[i-2][1] > startTime:
            count+=1

        # Check with the next interval
        if i < len(self.booked) and self.booked[i][0] < endTime:
            count+=1
        
        if i+1 < len(self.booked) and self.booked[i+1][0] < endTime:
            count+=1
            
        if count>1:
            return False

        # Insert the interval at the correct position
        self.booked.insert(i, (startTime, endTime))
        return True
    
cal = MyCalendar()
print(cal.book(10,20))  # True (booked = [(10,20)])
print(cal.book(50,60))  # False (overlaps with 10-20)
print(cal.book(10,40))  # True (adjacent but not overlapping)
print(cal.book(5,15))
print(cal.book(5,10))
print(cal.book(25,55))