grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]

visited=set()

ans=0

def island(i,j):
    if (i,j) in visited or grid[i][j]==0:
        return 0
    visited.add((i,j))
    total=1
    if i-1>=0:
        total+=island(i-1,j)
    if i+1<len(grid):
        total+=island(i+1,j)
    if j-1>=0:
        total+=island(i,j-1)
    if j+1<len(grid[0]):
        total+=island(i,j+1)
    return total

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            ans=max(ans,island(i,j))
            
print(ans)







def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        # base case: out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0  # mark as visited
        area = 1
        # explore 4 directions
        area += dfs(r+1, c)
        area += dfs(r-1, c)
        area += dfs(r, c+1)
        area += dfs(r, c-1)
        return area
    
    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    
    return max_area