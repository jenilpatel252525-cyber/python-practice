a=[
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]

target = 14

row=0
col=0

for i in range(len(a[0])):
    if a[0][i]>target:
        break
    col=i
    
for i in range(len(a)):
    if a[i][0]>target:
        break
    row=i
    
flag=False
    
for i in range(row+1):
    if a[i][col]==target:
        print(i,col)
        flag=True   
        break
    
if not flag:
    for i in range(col+1):
        if a[row][i]==target:
            print(row,i) 
            break
        
        
        
        
        
def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    
    row = 0
    col = m - 1
    
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return None








def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n * m - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        val = matrix[row][col]

        if val == target:
            return (row, col)
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1

    return None