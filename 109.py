board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]

def issurrounded(i, j):
    rows, cols = len(board), len(board[0])

    # UP
    flag = False
    if board[i-1][j] == "X":
        flag = True
    elif board[i-1][j] == "O":
        k = 2
        while i - k >= 0:
            if board[i - k][j] == "X":
                flag = True
                break
            elif board[i - k][j] == "O":
                k += 1
            else:
                break
    if not flag:
        return False

    # DOWN
    flag = False
    if board[i+1][j] == "X":
        flag = True
    elif board[i+1][j] == "O":
        k = 2
        while i + k < rows:
            if board[i + k][j] == "X":
                flag = True
                break
            elif board[i + k][j] == "O":
                k += 1
            else:
                break
    if not flag:
        return False

    # LEFT
    flag = False
    if board[i][j-1] == "X":
        flag = True
    elif board[i][j-1] == "O":
        k = 2
        while j - k >= 0:
            if board[i][j - k] == "X":
                flag = True
                break
            elif board[i][j - k] == "O":
                k += 1
            else:
                break
    if not flag:
        return False

    # RIGHT
    flag = False
    if board[i][j+1] == "X":
        flag = True
    elif board[i][j+1] == "O":
        k = 2
        while j + k < cols:
            if board[i][j + k] == "X":
                flag = True
                break
            elif board[i][j + k] == "O":
                k += 1
            else:
                break
    if not flag:
        return False

    return True

for i in range(1,len(board)-1):
    for j in range(1,len(board[0])-1):
        if board[i][j]=="O":
            if issurrounded(i,j):
                board[i][j]="X"
                
print(board)






def solve(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'T'  # Temporarily mark
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    # Step 1: Mark border-connected 'O's
    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols-1)
    for j in range(cols):
        dfs(0, j)
        dfs(rows-1, j)

    # Step 2: Flip unmarked 'O's to 'X', and 'T' back to 'O'
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'