timePoints = ["09:30","23:00"]

timePoints.sort(key=lambda t:(int(t[:2]),int(t[3:])))

ans=float("inf")

time1=timePoints[0].split(":")
time2=timePoints[-1].split(":")

temp=abs((int(time1[0])*60 + int(time1[1])) - (int(time2[0])*60 + int(time2[1])))

ans=temp if temp<=720 else abs(temp-1440)

for i in range(0,len(timePoints)-1):
    time1=timePoints[i].split(":")
    time2=timePoints[i+1].split(":")
    temp=abs((int(time1[0])*60 + int(time1[1])) - (int(time2[0])*60 + int(time2[1])))
    x=temp if temp<=720 else abs(temp-1440)
    ans=min(ans,x)
    
print(ans)









def find_min_difference(timePoints):
    # If more times than minutes in a day, duplicates exist
    if len(timePoints) > 1440:
        return 0

    seen = [False] * 1440
    for t in timePoints:
        hh, mm = map(int, t.split(':'))
        minutes = hh * 60 + mm
        if seen[minutes]:
            return 0  # duplicate time => min diff 0
        seen[minutes] = True

    prev = None
    first = None
    min_diff = 1440  # max possible
    for m in range(1440):
        if not seen[m]:
            continue
        if first is None:
            first = m
        if prev is not None:
            min_diff = min(min_diff, m - prev)
        prev = m

    # circular difference between last (prev) and first
    min_diff = min(min_diff, (first + 1440) - prev)
    return min_diff

# Example
print(find_min_difference(["09:30", "23:00"]))  # 630