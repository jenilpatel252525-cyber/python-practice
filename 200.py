def updateBoard(board, click):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    r, c = click

    if board[r][c] == 'M':
        board[r][c] = 'X'
        return board

    def dfs(x, y):
        if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] != 'E':
            return

        count = sum(
            1 for dx, dy in directions
            if 0 <= x+dx < len(board)
            and 0 <= y+dy < len(board[0])
            and board[x+dx][y+dy] == 'M'
        )

        if count > 0:
            board[x][y] = str(count)
        else:
            board[x][y] = 'B'
            for dx, dy in directions:
                dfs(x+dx, y+dy)

    dfs(r, c)
    return board
