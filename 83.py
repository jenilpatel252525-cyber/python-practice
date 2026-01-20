a=[[0,1],[0,0]]
m=len(a)
n=len(a[0])

def canmoveright(a,i,j,n):
    if j<n-1:
        if a[i][j+1]==1:
            return False
        else:
            return True
    else:
        return False
    
def canmovedown(a,i,j,m):
    if i<m-1:
        if a[i+1][j]==1:
            return False
        else:
            return True
    else:
        return False
    
i=0
j=0
count=0

def countpath(a,i,j,m,n):
    global count
    if i==m-1 and j==n-1:
        count+=1
    if canmoveright(a,i,j,n):
        countpath(a,i,j+1,m,n)
    if canmovedown(a,i,j,m):
        countpath(a,i+1,j,m,n)
        
countpath(a, i, j, m, n)

print(count)