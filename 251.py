board=[
    ["A","B","A","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
    ]

word = "ABACED"

def find(i,j,k):
    if k>=len(word):
        return True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols= len(board),len(board[0])
    
    temp = board[i][j]
    board[i][j] = "#" 
    for dr, dc in directions:
        r, c = i + dr, j + dc
        if 0 <= r < rows and 0 <= c < cols:
            if board[r][c]==word[k]:
                if find(r,c,k+1):
                    return True
                
    board[i][j] = temp
    return False

flag=False

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]==word[0]:
            if find(i,j,1):
                flag=True
                break
    if flag:
        break
    
print(flag)