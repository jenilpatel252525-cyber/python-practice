wall = [
    [1,2,2,1],
    [3,1,2],
    [1,3,2],
    [2,4],
    [3,1,2],
    [1,3,1,1]
    ]

total=sum(wall[0])

dp=[0]*total

for i in range(len(wall)):
    temp=0
    for j in range(len(wall[i])-1):
        temp+=wall[i][j]
        dp[temp]+=1

print(len(wall)-max(dp))








from collections import defaultdict

wall = [
    [1,2,2,1],
    [3,1,2],
    [1,3,2],
    [2,4],
    [3,1,2],
    [1,3,1,1]
]

edge_counts = defaultdict(int)

for row in wall:
    pos = 0
    for brick in row[:-1]:  # exclude last brick
        pos += brick
        edge_counts[pos] += 1

# Maximum edges a line can pass through
max_edges = max(edge_counts.values(), default=0)

# Minimum bricks crossed
min_crossed = len(wall) - max_edges
print(min_crossed)  # Output: 2