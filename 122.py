a=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

visited=set()

count=0

def isadj(i,j):
    if (i,j) in visited:
        return
    visited.add((i,j))
    if i-1>=0 and a[i-1][j]=="1":
        isadj(i-1,j)
    if i+1<len(a) and a[i+1][j]=="1":
        isadj(i+1,j)
    if j-1>=0 and a[i][j-1]=="1":
        isadj(i,j-1)
    if j+1<len(a[0]) and a[i][j+1]=="1":
        isadj(i,j+1)
    
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]=="1" and (i,j) not in visited:
            isadj(i,j)
            count+=1
            
print(count)





def numIslands(grid):
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
            return
        grid[i][j] = "0"  # mark visited
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)

    return count