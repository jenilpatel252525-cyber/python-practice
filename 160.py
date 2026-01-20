board = [
  ["X", ".", "X", "X", ".", ".", "X"],
  ["X", ".", ".", ".", ".", ".", "X"],
  [".", ".", ".", ".", ".", ".", "."],
  ["X", "X", ".", "X", ".", "X", "X"],
  [".", ".", ".", "X", ".", ".", "."]
]

def countBattleships(board):
    m, n = len(board), len(board[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                # Check if it's the start of a new battleship
                if (i == 0 or board[i - 1][j] != 'X') and \
                   (j == 0 or board[i][j - 1] != 'X'):
                    count += 1

    return count




def countBattleships(board):
    m, n = len(board), len(board[0])
    visited = set()
    count = 0

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X' and (i, j) not in visited:
                count += 1
                visited.add((i, j))

                # Explore right if exists
                if j + 1 < n and board[i][j + 1] == 'X':
                    y = j + 1
                    while y < n and board[i][y] == 'X':
                        visited.add((i, y))
                        y += 1
                # Else explore down if exists
                elif i + 1 < m and board[i + 1][j] == 'X':
                    x = i + 1
                    while x < m and board[x][j] == 'X':
                        visited.add((x, j))
                        x += 1

    return count