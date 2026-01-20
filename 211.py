from collections import Counter

def leastInterval(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = list(freq.values()).count(max_freq)
    print(freq)
    print(max_freq)
    print(max_count)
    # Formula
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)


print(leastInterval(["A","A","A","B","B","B"], 2)) 


tasks = ["A","C","A","B","D","B"]
n = 4

s = {}
prev = {}   # cooldown tracker
ans = []    # schedule result

# Step 1: count frequencies
for i in tasks:
    s[i] = s.get(i, 0) + 1

# Step 2: while tasks remain
time = 0
while s:
    # Step 2a: pick valid task (not in cooldown and still left)
    candidates = [task for task, count in s.items() if count > 0 and (task not in prev or prev[task] <= time)]
    
    if candidates:
        # Pick the task with max remaining frequency
        task = max(candidates, key=lambda x: s[x])
        
        ans.append(task)
        s[task] -= 1
        if s[task] == 0:
            del s[task]
        
        # set next available time for this task
        prev[task] = time + n + 1
    else:
        ans.append("idle")
    
    time += 1

print("Schedule:", ans)
print("Total Intervals:", len(ans))
