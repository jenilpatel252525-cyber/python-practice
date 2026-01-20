arr = [1,2,3,4]

from collections import Counter

class Solution:
    def largestTimeFromDigits(self, arr):
        cnt = Counter(arr)

        # Try hours in descending order
        for h1 in range(2, -1, -1):
            if cnt[h1] == 0:
                continue

            cnt[h1] -= 1
            h2_limit = 3 if h1 == 2 else 9

            for h2 in range(h2_limit, -1, -1):
                if cnt[h2] == 0:
                    continue

                cnt[h2] -= 1

                # Greedily pick minutes
                for m1 in range(5, -1, -1):
                    if cnt[m1] == 0:
                        continue

                    cnt[m1] -= 1

                    for m2 in range(9, -1, -1):
                        if cnt[m2] > 0:
                            return f"{h1}{h2}:{m1}{m2}"

                    cnt[m1] += 1
                cnt[h2] += 1
            cnt[h1] += 1

        return ""






class Solution:
    def largestTimeFromDigits(self, arr):
        arr.sort(reverse=True)
        used = [False] * 4
        time = []

        def is_valid(pos, d, h1=None):
            if pos == 0:
                return d <= 2
            if pos == 1:
                return d <= (3 if h1 == 2 else 9)
            if pos == 2:
                return d <= 5
            return True

        def dfs(pos):
            if pos == 4:
                return True

            for i in range(4):
                if used[i]:
                    continue

                d = arr[i]
                if not is_valid(pos, d, time[0] if pos > 0 else None):
                    continue

                used[i] = True
                time.append(d)

                if dfs(pos + 1):
                    return True

                # rollback
                used[i] = False
                time.pop()

            return False

        if dfs(0):
            return f"{time[0]}{time[1]}:{time[2]}{time[3]}"
        return ""


arr = [1,2,3,4]

arr.sort(reverse=True)

used=[False]*4

time=[]

for i in range(4):
    if arr[i]<=2:
        time.append(arr[i])
        used[i]=True
        break
    
for i in range(4):
    if not used[i]:
        if time[0]==2:
            if arr[i]<=3:
                time.append(arr[i])
                used[i]=True
                break
        else:
            time.append(arr[i])
            used[i]=True
            break
    
        
for i in range(4):
    if not used[i]:
        if arr[i]<=5:
            time.append(arr[i])
            used[i]=True
            break
        
for i in range(4):
    if not used[i]:
        time.append(arr[i])
        used[i]=True
        break