board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]

def find(i, j):
    a = [0, 0]  # a[0] = dead count, a[1] = live count

    rows = len(board)
    cols = len(board[0])

    # Top
    if i - 1 >= 0:
        if board[i-1][j] == 0 or board[i-1][j] ==2:
            a[0] += 1
        else:
            a[1] += 1

    # Bottom
    if i + 1 < rows:
        if board[i+1][j] == 0 or board[i+1][j] ==2:
            a[0] += 1
        else:
            a[1] += 1

    # Left
    if j - 1 >= 0:
        if board[i][j-1] == 0 or board[i][j-1] ==2:
            a[0] += 1
        else:
            a[1] += 1

    # Right
    if j + 1 < cols:
        if board[i][j+1] == 0 or board[i][j+1] ==2:
            a[0] += 1
        else:
            a[1] += 1

    # Top-left
    if i - 1 >= 0 and j - 1 >= 0:
        if board[i-1][j-1] == 0 or board[i-1][j-1] ==2:
            a[0] += 1
        else:
            a[1] += 1

    # Top-right
    if i - 1 >= 0 and j + 1 < cols:
        if board[i-1][j+1] == 0 or board[i-1][j+1] ==2:
            a[0] += 1
        else:
            a[1] += 1

    # Bottom-left
    if i + 1 < rows and j - 1 >= 0:
        if board[i+1][j-1] == 0 or board[i+1][j-1] ==2:
            a[0] += 1
        else:
            a[1] += 1

    # Bottom-right
    if i + 1 < rows and j + 1 < cols:
        if board[i+1][j+1] == 0 or board[i+1][j+1] == 2:
            a[0] += 1
        else:
            a[1] += 1

    return a

for i in range(len(board)):
    for j in range(len(board[0])):
        a=find(i,j)
        if board[i][j]==1:
            if a[1]<2:
                board[i][j]=3
            elif a[1]>3:
                board[i][j]=3
        else:
            if a[1]==3:
                board[i][j]=2
                
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]==3:
            board[i][j]=0
                
        elif board[i][j]==2:
            board[i][j]=1
            
print(board)