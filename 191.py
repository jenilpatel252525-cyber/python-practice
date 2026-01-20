mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

m=len(mat)-1
n=len(mat[0])-1

ans=[]

p=m+n

lists = [[] for _ in range(p+1)]

for i in range(m+1):
    for j in range(n+1):
        lists[i+j].append(mat[i][j])
        
for k in range(len(lists)):
    if k%2==0:
        ans.extend(lists[k][::-1]) 
    else:
        ans.extend(lists[k])  
        
print(ans)








def findDiagonalOrder(mat):
    if not mat:
        return []
        
    m, n = len(mat), len(mat[0])
    ans = []
    
    i, j = 0, 0  # starting position
    up = True    # direction flag
    
    for _ in range(m * n):
        ans.append(mat[i][j])
        
        if up:
            # moving up-right
            if j == n - 1:       # right border
                i += 1
                up = False
            elif i == 0:         # top border
                j += 1
                up = False
            else:
                i -= 1
                j += 1
        else:
            # moving down-left
            if i == m - 1:       # bottom border
                j += 1
                up = True
            elif j == 0:         # left border
                i += 1
                up = True
            else:
                i += 1
                j -= 1
    
    return ans
