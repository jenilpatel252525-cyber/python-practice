mat = [
    [0,1,1,1],
    [1,1,1,1],
    [1,0,1,0]
]

m, n = len(mat), len(mat[0])
dp = {}

def distance(i, j, visited):
    if (i, j) in dp:
        return dp[(i, j)]
    if mat[i][j] == 0:
        return 0

    visited.add((i, j))
    temp = float("inf")

    for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
            temp = min(temp, distance(ni, nj, visited) + 1)

    visited.remove((i, j))
    dp[(i, j)] = temp
    return temp

# Compute for all cells
for i in range(m):
    for j in range(n):
        distance(i, j, set())

print(dp)






from collections import deque

mat = [
    [0,1,1,1],
    [1,1,1,1],
    [1,0,1,0]
]

m, n = len(mat), len(mat[0])
dist = [[float('inf')] * n for _ in range(m)]
q = deque()

# Start BFS from all 0's
for i in range(m):
    for j in range(n):
        if mat[i][j] == 0:
            dist[i][j] = 0
            q.append((i, j))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    i, j = q.popleft()
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] > dist[i][j] + 1:
            dist[ni][nj] = dist[i][j] + 1
            q.append((ni, nj))

print(dist)
