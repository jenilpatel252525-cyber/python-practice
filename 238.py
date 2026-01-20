temperatures = [30,40,50,60]

ans=[0]*len(temperatures)

for i in range(len(temperatures)-1,0,-1):
    if temperatures[i]>temperatures[i-1]:
        ans[i-1]=1
    else:
        curr=i+ans[i]
        prev=i
        while curr!=prev:
            if temperatures[curr]>temperatures[i-1]:
                ans[i-1]=curr-(i-1)
                break
            else:
                prev=curr
                curr=curr+ans[curr]
    
print(ans)









temperatures = [73,74,75,71,69,72,76,73]
n = len(temperatures)
ans = [0] * n

for i in range(n-2, -1, -1):  # go backwards
    j = i + 1
    while j < n and temperatures[j] <= temperatures[i]:
        if ans[j] > 0:
            j = j + ans[j]  # jump ahead using precomputed result
        else:
            j = n  # no warmer day exists
    if j < n:
        ans[i] = j - i

print(ans)










from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []  # stores indices of decreasing temperatures

    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer