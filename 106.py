a=[[2],[3,10],[16,15,1],[4,13,16,3]]

path=float('inf')

curr=[]

def minpath(i,j):
    global path
    if i>=len(a):
        path=min(path,sum(curr))
        return
    for k in range(len(a[i])):
        if k==j or k==j+1:
            curr.append(a[i][k])
            minpath(i+1,k)
            curr.pop()
            
minpath(0,0)

print(path)





a = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

# Start from the second-last row and go upward
for i in range(len(a) - 2, -1, -1):
    for j in range(len(a[i])):
        # Add the min of the two adjacent numbers from the row below
        a[i][j] += min(a[i + 1][j], a[i + 1][j + 1])

# Result is now at the top of the triangle
print(a[0][0])