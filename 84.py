a=[[1,3,1],[1,5,1],[4,2,1]]

m=len(a)
n=len(a[0])

i=0
j=0

path=float('inf')
count=0

def canmoveright(j,n):
    if j<n-1:
        return True
    else:
        return False
    
def canmovedown(i,m):
    if i<m-1:
        return True
    else:
        return False
    
def countpath(a,i,j,m,n,count):
    global path
    count+=a[i][j]
    if i==m-1 and j==n-1:
        path=min(count,path)
        return
    if canmoveright(j,n):
        countpath(a,i,j+1,m,n,count)
    if canmovedown(i,m):
        countpath(a,i+1,j,m,n,count)
        
countpath(a, i, j, m, n,count)
        
print(path)

# a = [[1, 3, 1],
#      [1, 5, 1],
#      [4, 2, 1]]

# m = len(a)
# n = len(a[0])

# # Create DP table
# dp = [[0]*n for _ in range(m)]

# # Fill the top-left corner
# dp[0][0] = a[0][0]

# # Fill first row
# for j in range(1, n):
#     dp[0][j] = dp[0][j-1] + a[0][j]

# # Fill first column
# for i in range(1, m):
#     dp[i][0] = dp[i-1][0] + a[i][0]

# # Fill the rest of the grid
# for i in range(1, m):
#     for j in range(1, n):
#         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + a[i][j]

# # Final result
# print(f"Minimum path sum: {dp[m-1][n-1]}")
